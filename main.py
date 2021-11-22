import random # need random for the computer to place a move

# initialising the game board and players  
board = [ # 0 is a empty space then 1 is player1 and 2 is player2
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0],
]
player_1 = 1 # what represents player 1 move 
player_2 = 2 # what represents player 2 move 
switch_player = 1 # deciding which player is current playing. value of 1 for player1 or -1 for player2

# checks if a move is valid, returns true if the move is valid else returns false
def valid_move(choice):
  """checks if a move is valid. returns either true or false"""
  for row in range(len(board) - 1, -1, -1): # starting from the bottom of the board, if the bottom of the board is taken go to the next level 
    if board[row][choice] == 0: # if the board is a empty space
      return True # move is valid return true
    if row == 0: # reached the top
      return False # return false if there is no space availabe

# user gives input and then will have to check if a piece is already there, then go higher <- loop till space
def move(choice, player):
  """given (int)choice which is the column position and player(which player) will be placed on the board"""
  # starting from the bottom of the board. if the board place has been taken then check the next one above
  for column in range(len(board) - 1, -1, -1):
    if board[column][choice] == 0: # if the board is a empty space
      board[column][choice] = player # replacing the empty space for the player piece 
      break

# draws the board in a 2d grid easier for player to see the game
def draw_board():
  """print's the board to the console"""
  print(" 1  2  3  4  5  6  7") # can easily see what number represents the column for the player
  for row in board: 
    print(row) #gets each row from the board and prints it, presenting a 2d board

# check if any win condition is met either horizontally, verically or diagonal
def check_win_state():
  """check the board if there is a win condition"""
  for row in range(len(board) - 1, -1, -1): # looping over the rows and starting from the bottom
    for col in range(0, 7): # looping over the horizontal
      if board[row][col] != 0: # don't consider a 0 as a winnable state.
        if col < 4: # making sure i don't go out of bounds in the column array
          # we have a winning state horizontally 
          if board[row][col] == board[row][col + 1] and board[row][col] == board[row][col + 2] and board[row][col] == board[row][col + 3]:
            return True

          # we have a right diagonal winner
          if board[row][col] == board[row - 1][col + 1] and board[row][col] == board[row - 2][col + 2] and board[row][col] == board[row - 3][col + 3]:
            return True; 

        if col > 2: # making sure i don't go out of bounds in the columns array
          # we have a winning state going left diagonal 
           if board[row][col] == board[row - 1][col - 1] and board[row][col] == board[row - 2][col - 2] and board[row][col] == board[row - 3][col - 3]:
            return True; 

        # we have a winning state going vertically 
        if board[row][col] == board[row - 1][col] and board[row][col] == board[row - 2][col] and board[row][col] == board[row - 3][col]:
          return True
  
  return False # if none of the conditions were met return false 

# checking if the user input is valid, if not keep looping over until desired input is done, also handles valid_move()
def valid_input(input_string):
  """checks if the user input is valid, if not keep looping over until desired input is done"""
  not_valid = True # easier to read and understand the while loop
  while not_valid:
    is_number = input_string.isdigit() # checking if the input_string has a number in the string
    if is_number: # if is number is true
      number = int(input_string) - 1 #convert input string to a int and store it to the number variable
      
      if number > 6 or number < 0: # if the number is not the desired options 
        print("invalid number") # informing the player, that the last input was a invalid number
        input_string = input("pick a column from 1 - 7: ") # asking user for a new input
        continue # loops back with the new input that has been stored in the input_string

      elif valid_move(number) == False: # if the move is not valid
        print("invalid space")
        input_string = input("pick a column from 1 - 7: ") # asking user for a new input
        continue

      else:
        return number # if the number is valid then return the number and leaves the loop

    else: # if the is_number is false
      print("invalid input") # informs the player, the previous input was not valid
      input_string = input("pick a column from 1 - 7: ") # loops back with the new input that has been stored in the input_string

# Game starts from here
print("\n" * 55) # clears the command screen so easier to see/read 
print("WELCOME TO CONNECT 4") # introduction and game title
print("connect four of your pieces to win! either horizontally, vertially or diagonally") # instructions on how to win

is_computer_playing = input("Do you want to play with the computer? 'y' or 'n': ") # if we are playing with the computer or another person
if is_computer_playing.lower() == "y":
  computer = True
else:
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

  draw_board() # draws the board for the player to see the game 
  
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
    switch_player = -switch_player #if the new move was not the winning move then switch player
  
  #checks if the game board is filled and no more spaces available
  if 0 in board[0]:
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
