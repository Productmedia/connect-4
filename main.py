board = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
]
computer = False # if we are playing the game 1 player 
player_1 = 1
player_2 = 2

#prints the board
for row in board: 
  print(row)


# user gives input and then will have to see where it lands if a piece is already there go higher <- loop till space

def move(choice, player):
  """given row choice(int) and player(which player) will be placed on the board"""
  # coming from the bottom of the board. if the board place has been taken then check the next one above
  for column in range(len(board) - 1, 0, -1):
    if board[column][choice] == 0:
      board[column][choice] = player
      break
  else:
    return False # return false if there is no space availabe

playing = True


# game loop 
while playing:
  print(f"PLAYER 1 TURN")
  for row in board: 
    print(row)
  
  choice = int(input("pick a column from 1 - 7: ")) -1 
  move(choice, player_1)

  # check_win_state()
  
  
  


