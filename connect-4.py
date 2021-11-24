import random # need random for the computer to place a move

# initialising the game board and players  
board = [ # 0 is a empty space then 1 is player1 and 2 is player2
  ['0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0'],
  ['0','0','0','#','0','0','0'],
  ['0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0'],
]


players = ["1", "2"]
valid_space = ['0','#','%', "X"] # valid spaces for the player to choose from 
player_1 = '1' # what represents player 1 move 
player_2 = '2' # what represents player 2 move 
switch_player = 1 # deciding which player is current playing. value of 1 for player1 or -1 for player2
upside_down = False # power up that will draw the board upside down confusing the players 
turn = 0 # counts the turns

# checks if a move is valid, returns true if the move is valid else returns false
def valid_move(choice):
  """checks if a move is valid. returns either true or false"""
  for row in range(len(board) - 1, -1, -1): # starting from the bottom of the board, if the bottom of the board is taken go to the next level 
    if board[row][choice] in valid_space: # if the current board choice is valid
      return True # move is valid return true
    if row == 0: # reached the top
      return False # return false if there is no space availabe

# checking if the user input is valid, if not keep looping over until desired input is done, also handles valid_move()
def valid_input(input_string):
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

      elif valid_move(number) == False: # if the move is not valid
        print("invalid space")
        input_string = input("pick a column from 1 - 7: ") # asking user for a new input
        continue

      else: # if the number is valid then return the number and leaves the loop
        return number 

    else: # if the is_number is false / input is not a number
      print("invalid input") # informs the player, the previous input was not valid
      input_string = input("pick a column from 1 - 7: ") # loops back with the new input that has been stored in the input_string

# user gives input and then will have to check if a piece is already there, then go higher <- loop till space
def move(choice, player):
  """given (int)choice which is the row position and player(which player) will be placed on the board"""
  # starting from the bottom of the board. if the board place has been taken then check the next one above
  for row in range(len(board) - 1, -1, -1):
    if board[row][choice] in valid_space: # if the current board choice is in valid space
      board[row][choice] = player # replacing the empty space for the player piece 
      break

#prints the options to the screen easier for player to see their options and what number is the column
def draw_options():
  for column in range(1, len(board[0]) + 1): #counts from 1 and goes up to the length of the board column 
    print(f"  {column}  ", end = "")
  print("") # seperates the options to the board.

# draws the board in a 2d grid easier for player to see the game
def draw_board():
  """prints the board to the console"""
  draw_options() # calls the draw options for the player

  for row in board: 
    print(row) #gets each row from the board and prints it, presenting a 2d board

#draws the upside down board, confusing the players 
def draw_reverse_board():
  """prints the upside down to the console"""
  draw_options() # calls the draw options for the player    
  for row in range(len(board) - 1, -1, -1): # reverses the print statement of how to draw the board so it is now upside down to the player 
    print(board[row]) 

# check if any win condition is met either horizontally, verically or diagonal
def check_win_state():
  """check the board if there is a win condition"""
  for row in range(len(board) - 1, -1, -1): # looping over the rows and starting from the bottom
    for col in range(0, 7): # looping over the horizontal
      if board[row][col] in players: # don't consider a valid spaces as a winnable state.
        if col < 3: # making sure i don't go out of bounds in the column array
          # we have a winning state horizontally 
          if board[row][col] == board[row][col + 1] and board[row][col] == board[row][col + 2] and board[row][col] == board[row][col + 3]:
            print("horizontal winner")
            return True

          # we have a right diagonal winner
          if board[row][col] == board[row - 1][col + 1] and board[row][col] == board[row - 2][col + 2] and board[row][col] == board[row - 3][col + 3]:
            print("right diagonal winner")
            return True; 

        if col > 3: # making sure i don't go out of bounds in the columns array
          # we have a winning state going left diagonal 
           if board[row][col] == board[row - 1][col - 1] and board[row][col] == board[row - 2][col - 2] and board[row][col] == board[row - 3][col - 3]:
            print("left diagonal winner")
            return True; 

        # we have a winning state going vertically 
        if board[row][col] == board[row - 1][col] and board[row][col] == board[row - 2][col] and board[row][col] == board[row - 3][col]:
          print("vertical winner")
          return True
  
  return False # if none of the conditions were met return false 

#clears the column chosen back to empty spaces
def clear_column(column):
  """clears a whole column"""
  for row in range(0, len(board)):
    board[row][column] = '0'


# Game starts from here
print("\n" * 55) # clears the command screen so easier to see/read 
print("WELCOME TO CONNECT 4") # introduction and game title
print("connect four of your pieces to win! either horizontally, vertially or diagonally.") # instructions on how to win
print("Oh by the way, this game has power ups that can be collected.")

# is_computer_playing = input("Do you want to play with the computer? 'y' or 'n': ") # if we are playing with the computer or another person
# if is_computer_playing.lower() == "y":
#   computer = True # the computer is playing 
# else:
#   computer = False # the computer is not playing

computer = False
playing = True #stating that we are playing the game

# main game loop 
while playing:
  print("\n" * 55) # clears the command screen so easier to see/read
  # which player is currently taking their turn and stores it in current_player
  if switch_player == 1:  
    current_player = player_1 
    print("PLAYER 1's TURN") # stating who's turn it is on the screen
  else: 
    current_player = player_2
    print("PLAYER 2's TURN")

  if upside_down: # if this power up is activated 
    draw_reverse_board()
  else:
    draw_board() # draws the board for the player to see the game 
  
  if turn == 2:
    clear_column(0)
  elif turn > 8:
    upside_down = True

  #get user input from a range from 1 - 7 / need to make sure they do not put any letters
  # if the computer = true and player = player2 then let the computer decide a number 
  if computer and current_player == 2: # getting a computer to pick a random number between 1 - 7
    choice = random.randint(0, 6)
  else:
    choice = valid_input(input("pick a column from 1 - 7: "))

  move(choice, current_player)# the move was valid and placed
  if check_win_state() == True:   # checks the win state from the new move if not continue
    playing = False
    break
  else:
    turn += 1
    switch_player = -switch_player #if the new move was not the winning move then switch player
  
  #checks if the game board is filled and no more spaces available
  if '0' in board[0]:
    continue # there is still space on the board so continue
  else:
    break # its a tie 


if check_win_state() == True:
  print("\n" * 45)
  draw_board()
  print(f"\ncongratulations to player {current_player} for winning the game")
else:
  print("\n" * 45)
  draw_board()
  print("It's a tie!")
