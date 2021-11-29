import math

score = {
  "1": -1,
  "2": 3,
  "tie": 0
}

def minimax(postition, depth, maximizing_player):
  """minimax algorithm for the ai to be a better opponent"""
  if depth == 0: # or game over state
    return postition
  
  if maximizing_player:
    max_eval = -math.inf # assigning max_eval to negative infinity
    for child in postition: # this needs to loop over the positions in the connect-4
      eval = minimax(child, depth - 1, False)
      max_eval = max(max_eval, eval)
      # alpha = max(alpha, eval)
      # if beta <= alpha:
      #   break
    return max_eval
  
  else:
    min_eval = math.inf
    for child in postition:
      eval = minimax(child, depth - 1, True)
      min_eval = min(min_eval, eval)
      # beta = min(beta, eval)
      # if beta <= alpha:
      #   break
    return min_eval


