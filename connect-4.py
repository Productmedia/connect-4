import random # need random to create power ups on a chance based
# import math  # need to use for the computer to decide on what move is the best move
from board_utils.board import * 


# initialising the game board   
board = create_board(6, 7)

# initialising the players and valid spaces and power ups
players = ['1', '2'] # what each player represents
valid_space = ['0','%','X'] # valid spaces for the player to choose from 
player_1 = players[0] # what represents player 1 move 
player_2 = players[1] # what represents player 2 move 
switch_player = 1 # deciding which player is current playing. value of 1 for player1 or -1 for player2
upside_down = False # power up that will draw the board upside down confusing the players 
clear_a_column = False # active the power up to clear a column
turn = 0 # counts the turns for the power ups
playing = True # stating that we are playing the game for the main game loop
pieces = [] # stores removed pieces from the board  

# defines the scoring for the minimax algorithm to decide what is a good move for the computer 
scores = {
  "1": -20, # if player 1 wins the game the computer gets a negative score 
  "2": 10, # if player 2 wins give the computer a postive score
  "none": 0 # if none player wins give a score that is not negative or postive
}

#clears the whole input column back to empty spaces
def clear_column(column, board):
  """clears a whole column"""
  print("clearing a column")
  for row in range(0, len(board)): # goes through each row
    board[row][column] = '0' # at each row and the column assign makes each value back to 0

# places and decides the power up on the board
def create_power_up(board):
  """creates and places the power up on the board"""
  power_up = random.randint(1, 2) # deciding what power up should it be 
  column = random.randint(0, len(board[0]) - 1) # get a random column
  for row in range(len(board) - 1, 0, -1): # starting from the bottom of the board, if the bottom of the board is taken go to the next level 
    if board[row][column] == "0": # if the current board choice is valid
      board[row][column] = valid_space[power_up] # places the power up on the board
      break # breaks out of the loop
  
# checks if a move is valid, returns true if the move is valid else returns false
def valid_move(choice, board):
  """checks if a move is valid. returns either true or false"""
  for row in range(len(board) - 1, -1, -1): # starting from the bottom of the board, if the bottom of the board is taken go to the next level 
    if board[row][choice] in valid_space: # if the current board choice is valid
      return True # move is valid return true
    if row == 0: # reached the top
      return False # return false if there is no space availabe

# checking if the user input is valid, if not keep looping over until desired input is done, also handles valid_move()
def valid_input(input_string, board):
  """checks if the user input is valid, if not keep looping over until desired input is done"""
  not_valid = True # easier to read and understand the while loop
  while not_valid:
    is_number = input_string.isdigit() # checking if the input_string has a number in the string
    if is_number: # if is_number is true
      number = int(input_string) - 1 #convert input string to a int and store it to the number variable
      
      if number > (len(board[0]) - 1) or number < 0: # if the number is not the desired options 
        print("invalid number") # informing the player, that the last input was a invalid number
        input_string = input("pick a column from 1 - 7: ") # asking user for a new input
        continue # loops back with the new input that has been stored in the input_string

      elif valid_move(number, board) == False: # if the move is not valid 
        print("invalid space")
        input_string = input("pick a column from 1 - 7: ") # asking user for a new input
        continue

      else: # if the number is valid then return the number and leaves the loop
        return number 

    else: # if the is_number is false / input is not a number
      print("invalid input") # informs the player, the previous input was not valid
      input_string = input("pick a column from 1 - 7: ") # loops back with the new input that has been stored in the input_string

# user gives input and then will have to check if a piece is already there, then go higher <- loop till space
# Triggers the colliding with power ups
def move(board, choice, player, is_main):
  """given (int)choice which is the column position and player(which player) will be placed on the board"""
  # starting from the bottom of the board. if the board place has been taken then check the next one above
  previous_piece = {} # is a holder to place a valid piece back in postion for the minimax algo
  for row in range(len(board) - 1, -1, -1): 
    if board[row][choice] in valid_space: # if the current board choice is in valid space
      if board[row][choice] == valid_space[1]: # picked up power 1 / creates the board upside down
        global upside_down # changing the value for upside down to True
        global turn # for some reason i have to declare a global variable that is already global :\ 
        previous_piece["piece"] = valid_space[1] # storing our value/character into a dictonary
        previous_piece["row"] = row # storing the row postion
        previous_piece["col"] = choice # storing the column position
        pieces.append(previous_piece) # add the new previous piece to the pieces list
        if is_main: # triggers the power up if only its the main board
          upside_down = True # state that the upside down power up is now true
          turn = 0 # setting the turn variable to 0 cause i only want the upside down to only be for certain amount of turns
      elif board[row][choice] == valid_space[2]: # picked up power up 3 which is the clearing a column
        previous_piece["piece"] = valid_space[2] # storing our value/character into a dictonary
        previous_piece["row"] = row # storing the row postion
        previous_piece["col"] = choice # storing the column postion
        pieces.append(previous_piece) # add the previous piece to the list 
        global clear_a_column
        if is_main: # triggers the power up if only its the main board
          clear_a_column = True # state that the clearing column is true and is activated
      board[row][choice] = player # replacing the space for the player piece 
      break

# undo a move depending if the top player is the player given
def undo_move(board, choice, player): 
  """given (int)choice which is the column position and player(which player) will be removed from the board only if its the top piece on the column"""
  # starting from the bottom of the board. if the board place has been taken then check the next one above
  for row in range(0, len(board)): # loops through the board row array
    if board[row][choice] == player: # if the current board choice is in valid space
      if len(pieces) > 0: # if the pieces has got at least 1 or more values in the list
        for recent_piece in range(len(pieces) - 1, -1, -1): # starting from the back of the list so got the most recent piece
          if pieces[recent_piece]["col"] == choice and pieces[recent_piece]["row"] == row: # if the piece is a match with the row and column
            board[row][choice] = pieces[recent_piece]["piece"] # change the postion we are on back to the previous piece that was once there
            pieces.pop() # remove the piece from the list
            break #break we are done with the current postion no longer need to look through the piece list
        else: # if the current postion wasn't a match with the list 
          board[row][choice] = "0" # give the postion a blank spot/ "0"
      else: # if the length of pieces is less than 1 
        board[row][choice] = "0" # replacing the space back to a zero
      break # break out of the loop we have found the player and replaced that spot 

#prints the options to the screen easier for player to see their options and what number is the column
def draw_options(board):
  """draws a number for each column in the board"""
  print(" ", end ="") # giving our options some space to align up with the board columns
  for column in range(1, len(board[0]) + 1): #counts from 1 and goes up to the length of the board column 
    print(" ", column, end = "") #prints the options to the board
  print() # seperates the options to the board
  print("  ", end =" ") # makes the under score align
  for column in range(1, len(board[0]) + 1): #counts from 1 and goes up to the length of the board column 
    print("_", end = "  ") # prints the underscores to seperate the board to the options
  print() # seperates the options to the board.

#draws the upside down board, confusing the players 
def draw_reverse_board(board):
  """prints the upside down to the console"""
  for row in range(len(board) - 1, 0, -1): # reverses the print statement of how to draw the board so it is now upside down to the player 
    print("|" ,end="") # draws a vertical line at left edge of board, for each row
    for column in board[row]: # loops through each column in the current row 
      print(" ", column, end= "") # gives space between each column value
    print("  |") # draws a vertical line at the right edge of the board, for each row

    print("| " ,end="") # draws a vertical line at left edge of board, for each row
    for column in range(0, 10): # draws 10 dashes between each row
      print(" -", end= "") # draw a dash roughly under each column  
    print("  |") # draws a vertical line at the right edge of the board, for each row
      
# check if a win condition is met either horizontally, verically or diagonal, returns a string character or boolean value
def check_win_state(board, want_character):
  """check the board if there is a win condition. either returns the winning character or True. If no winstate returns False/'none' """
  for row in range(len(board) - 1, -1, -1): # looping over the rows and starting from the bottom
    for col in range(0, 7): # looping over the horizontal
      if board[row][col] in players: # only consider a player spaces as a winnable state.
        if col < 4: # making sure I don't go out of bounds in the column array when checking if statements  
          # we have a winning state horizontally by checking the next 3 column is all equal to each other 
          if equals(board[row][col], board[row][col + 1], board[row][col + 2], board[row][col + 3]): 
            if want_character: # if we want the winning string character
              return board[row][col] # returns the winning string character
            print("horizontal winner") # tells the players how they won
            return True 

          # making sure we don't wrap around the board and we have a right diagonal winner.
          if row > 2 and equals(board[row][col], board[row - 1][col + 1], board[row- 2][col + 2], board[row -3][col + 3]):
            if want_character:  # if we want the winning string character
              return board[row][col] # returns the winning string character
            print("right diagonal winner") # tells the players how they won
            return True; 

        if col > 2 and row > 2: # making sure i don't go out of bounds in the columns array
          # we have a winning state going left diagonal 
           if equals(board[row][col], board[row - 1][col - 1], board[row - 2][col - 2], board[row - 3][col - 3]):
            if want_character: # if we want the winning string character
              return board[row][col] # if we want the winning string character
            print("left diagonal winner") # tells the players how they won
            return True; 

        # we have a winning state going vertically 
        if row > 2 and equals(board[row][col], board[row - 1][col], board[row - 2][col], board[row - 3][col]):
          if want_character: # if we want the winning string character
            return board[row][col] # returns the winning string character
          print("vertical winner") # tells the players how they won
          return True; 
 
  # if none of the above were True give a final return which is false or none
  if want_character: # if we want the winning string character
    return "none" # tells that there was no winner
  return False # if none of the conditions were met return false. No winner

# recusion function that takes in the board and counts the depth and determines who is the maximizing player 
# is used for the computer decision and uses creates future boards to determine the score 
def minimax(board, depth, maximizing_player):
  """returns a score value, depth determines how far forward to work from"""
  result = check_win_state(board, True) # results on who is winning the game to determine the score 
  if depth == 0 or result != "none": # when the depth has hit 0 it will return a score or when the result not none
    score = scores[result] # checks the result winning character and puts into the scores dictonary and determines the score
    return score # returns score 
  
  if maximizing_player: # if its the maximizing turn 
    best_score = -math.inf  # setting the best score to be -infinity 
    for col in range(0, len(board[0])): # loops through the column
      if valid_move(col, board) == True: # if the spot is available
        move(board, col, player_2, False)# places the ai in the first spot 
        score = minimax(board, depth - 1, False) # checks the score by going further predicting game states
        undo_move(board, col, player_2) # removes the player from that spot 
        best_score = max(score, best_score) # compares the new score to the old best_score and chooses the higher score
    return best_score # returns the best score that it has calculated

  else: # its not the maximizing player so going to make the best move for the player so lower score for the ai 
    best_score = math.inf # sets the score to the + infinity 
    for col in range(0, len(board[0])): # loops through the columns to choose from
      if valid_move(col, board) == True: # if the move is valid
        move(board, col, player_1, False) # places the player piece to 
        score = minimax(board, depth - 1, True) # checks the score by going further predicting game states
        undo_move(board, col, player_1) # removes the player piece from the board so it loops to the next column position 
        best_score = min(score, best_score) # compares the new score to the old best score and chooses the lower score 
    return best_score # returns the best score that it has calculated

# best move for the computer to make
def best_move(board):
  """returns a column to choose from. Uses the minimax algorithm to determine where to go"""
  best_score = -math.inf # best score is set to -infinity 
  coords = {} # creates the coords to return to the player
  score = -math.inf # score has to be defined and is set to -infinity 

  for column in range(0, len(board[0])): # loops through the columns
    print("working on it...") # tells the player that the ai is working on a move to make
    if valid_move(column, board) == True: # if the spot is available
      move(board, column, player_2, False)# places the ai in the first spot 
      score = minimax(board, 2, False) # checks the score by going deeper 
      undo_move(board, column, player_2) # removes the player from that spot 

    if score > best_score: # when the score is greater than the best score replace it
      best_score = score # replacing the best score to score value
      coords["col"] = column # storing the column value to the coords with a key of "col"
  return coords["col"] # returns the value of column postion 

# Game starts from here
print("\n" * 55) # clears the command screen so easier to see/read 
print("WELCOME TO CONNECT 4") # introduction and game title
print("connect four of your pieces to win! either horizontally, vertially or diagonally.") # instructions on how to win
print("Oh by the way, this game has power ups that can be collected.") # informing the player, that there is power ups in the game

is_computer_playing = input("Do you want to play with the computer? 'y' or 'n': ") # if we are playing with the computer or another person
if is_computer_playing.lower() == "y":
  computer = True # the computer is playing 
else: # the computer is not playing
  computer = False # the computer is not playing


while playing: # main game loop 
  print("\n" * 55) # clears the command screen so easier to see/read
  print("CONNECT 4") # presenting the game title 
  print("=========") # underlining the game title
  # which player is currently taking their turn and stores it in current_player
  if switch_player == 1:  # if switch_player equal to 1
    current_player = player_1 # sets the current player to player 1
    print("PLAYER 1's TURN") # stating who's turn it is on the screen
  else: # if switch_player equal to -1
    current_player = player_2 # sets the current player to player 1
    print("PLAYER 2's TURN") # stating who's turn it is on the screen
  print("---------------") # uderlining whos currently playing

  # creates and places a power up on the board
  chance = random.random() # creates a floating number between 0 - 1
  if chance < 0.16 and turn > 3: # only create the power ups on a chance below 20% and turn is higher than 3
    create_power_up(board) # creates and places the power up on the board for the player to land on
 
  # draws the board either normal or upside down
  if upside_down and turn <= 6: # if this power up is True and the turn amount is less than 6 
    draw_options(board)
    draw_reverse_board(board) # draws the board upside down
  else: # draws the board normally 
    draw_options(board)
    draw_board(board) # draws the board for the player to see the game 
  
  # handles the user and computer input and checks if the move was valid
  # if the computer = true and player = player2 then let the computer decide a number 
  if computer and current_player == '2': # getting a computer to pick a random number between 1 - 7
    choice = best_move(board) # chooses the best move for the computer to go 
  else: # get player(s) to give input
     # get user input from a range from 1 - 7
     # asks the player(s) their move. checks valid input and handles it
    choice = valid_input(input("pick a column from 1 - 7: "), board)

  move(board, choice, current_player, True)# the move was valid and placed
  if check_win_state(board, False) == True: # checks the win state from the new move if not continue
    playing = False # we are no longer playing. the main game loop is now finished
    print("\n" * 45) # gives a clean screen 
    draw_board(board) # draws the final board
    check_win_state(board, False) # prints how they won
    print(f"\ncongratulations to player {current_player} for winning the game") # congrats the player for winning the game
  else: # the new move was not the winning move so continuing the game and swich players
    turn += 1 # increases the turn counter
    switch_player = -switch_player # switches player
  
  if clear_a_column == True: # if the clear a column power up was activatedd
    column = random.randint(0, len(board[0]) -1) # selects a random column
    clear_column(column, board) # clears the random column chosesn
    clear_a_column = False # set the trigger back to false

  #checks if the game board is filled and no more spaces available
  for avaiable_space in valid_space: # checks if any of the valid space is available in the game still
    if avaiable_space in board[0]: # only has to check the top row if there is any available spaces
      break # there is still space on the board so continue
    else: # its a tie
      playing = False # exit the main game loop
      print("\n" * 45) # gives a clean screen
      draw_board(board) # draws the final board
      print("It's a tie!") # tell the player(s) it's a tie
      break # break out the loop
