N = 9

def safe(grid, row, col, num):
  for i in range(N):
    if grid[row][i] == num:
      return False
    
  for i in range(N):
    if grid[i][col] == num:
      return False
  
  startRow = (row // 3) * 3
  startCol = (col // 3) * 3
  
  for i in range(startRow, startRow + 3):
    for j in range(startCol, startCol + 3):
      if grid[i][j] == num:
        return False
      
  return True

def valid(grid):
  if (len(grid) != 9):
    return False
  for row in grid:
    if (len(row) != 9):
      return False
  
  for i in range(N):
    for j in range(N):
      num = grid[i][j]
      
      if type(num) != int or num < 0 or num > 9:
        return False
      
      if num != 0:
        grid[i][j] = 0
        
        if not safe(grid, i, j, num):
          grid[i][j] = num
          return False
        
        grid[i][j] = num
  return True

def solve(grid):
  for row in range(N):
    for col in range(N):
      if (grid[row][col] == 0):
        for num in range(1,10):
          if safe(grid, row, col, num):
            grid[row][col] = num
            
            if solve(grid):
              return True
            
            grid[row][col] = 0
        return False
  return True

def print_grid(grid):
  for row in grid:
    print(" ".join(str(num) for num in row))
    
# Main
grid = []

print("Enter 9 rows of the Sudoku puzzle, with 0 for empty cells:")
try:
  for i in range(9):
    row = list(map(int, input().split()))
    grid.append(row)
  
  if not valid(grid):
    print("Invalid Sudoku grid. Please ensure it is a 9x9 grid with numbers between 0 and 9.")
    
  elif solve(grid):
    print("Solved Sudoku grid:")
    print_grid(grid)
  
  else:
    print("No solution exists for the given Sudoku puzzle.")
    
except (ValueError, EOFError):
  print("Invalid input")