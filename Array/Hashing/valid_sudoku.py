def valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = {}

    for i in range(9):
        for j in range(9):
            val = board[i][j]

            if val =='.':
                continue

            if val in rows[i]:
                return False
            
            rows[i].add(val)

            if val in cols[j]:
                return False
            
            cols[j].add(val)

            box_key = (i//3, j//3)

            if box_key not in boxes:
                boxes[box_key] =set()

            if val in boxes[box_key]:
                return False
            
            boxes[box_key].add(val)
    
    return True

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(valid_sudoku(board))  # Output: True