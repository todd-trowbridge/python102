board = [
  ['_','_','_'],
  ['_','x','_'],
  ['_','_','o']
]

# print(board[1][1])
# print(board[2][2])

while True:
  row_index = 0
  for row in board:
    col_index = 0
    for col in row:
      if col == ' ':
        print(row, col, end=' ')
      else:
        print(col, end='     ')
      col_index += 1
    print('')
    print('')
    row_index += 1

  pos_row = int(input('which row? '))
  pos_col = int(input('which column? '))

  board[pos_row][pos_col] = 'X'