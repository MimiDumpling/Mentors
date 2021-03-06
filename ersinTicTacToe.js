// def winner(board):
//     # Check row-wins
//     for i in range(3):
//         if board[i][0] and (board[i][0] == board[i][1] == board[i][2]):
//           return board[i][0]
      
//     # Check column-wins
//     for i in range(3):
//         if board[0][i] and (board[0][i] == board[1][i] == board[2][i]):
//           return board[0][i]

//     # Check diagonal-wins
//     if board[0][0] == board[1][1] == board[2][2]:
//         return board[0][0]

//     if board[0][2] == board[1][1] == board[2][0]:
//         return board[0][2]

//     return None

// board1 = [
// ['X', 'O', None],
// ['X', None, 'O'],
// ['X', None, 'O'],
// ]
// board2 = [
// ['O', 'O', None],
// ['X', 'O', 'O'],
// ['X', None, 'O'],
// ]

// print(winner(board1))
// print(winner(board2))


function winner(board) {
  const range = [0, 1, 2]

  // Check row-wins
  for (const index in range) {
    if (board[index][0] && (board[index][0] === board[index][1] && board[index][1] === board[index][2])) {
      return board[index][0]
    }
  }

  // Check column-wins
  for (const index in range) {

    if (board[0][index] && (board[0][index] === board[1][index] && board[1][index] === board[2][index])) {
      return board[0][index]
    }
  }

  // Check diagonal-wins
  if (board[0][0] === board[1][1] && board[1][1] === board[2][2]) {
    return board[0][0]
  }

  if (board[0][2] === board[1][1] && board[1][1] === board[2][0]) {
    return board[0][2]
  }

  return console.log("No winner. Cat's Game.")

}

board1 = [
['X', 'O', undefined],
['X', undefined, 'O'],
['X', undefined, 'O'],
]
board2 = [
['O', 'O', undefined],
['X', 'O', 'O'],
['X', undefined, 'O'],
]

console.log(winner(board1))
console.log(winner(board2))