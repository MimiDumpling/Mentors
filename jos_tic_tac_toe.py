def winner(board):
    # Check row-wins
    for i in range(3):
        if board[i][0] and (board[i][0] == board[i][1] == board[i][2]):
          return board[i][0]
      
    # Check column-wins
    for i in range(3):
        if board[0][i] and (board[0][i] == board[1][i] == board[2][i]):
          return board[0][i]

    # Check diagonal-wins
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


board1 = [
['X', 'O', None],
['X', None, 'O'],
['X', None, 'O'],
]
board2 = [
['O', 'O', None],
['X', 'O', 'O'],
['X', None, 'O'],
]

print(winner(board1))
print(winner(board2))
