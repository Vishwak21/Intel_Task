# 9×9 Sudoku Solver

## Overview

A Python program that solves a standard **9×9 Sudoku puzzle** using **recursive backtracking**. It validates the initial grid before solving and handles invalid input and puzzles with no solution.

## Problem Statement

Fill the empty cells of a 9×9 Sudoku grid so that:

- Each row contains digits 1–9 exactly once.
- Each column contains digits 1–9 exactly once.
- Each 3×3 subgrid contains digits 1–9 exactly once.
- Initially filled values remain unchanged.

**Input convention:** Use `0` to represent an empty cell.

## Implementation

The solution uses four functions:

| Function | Purpose |
| --- | --- |
| `safe(grid, row, col, num)` | Checks whether a digit is absent from the target row, column, and 3×3 subgrid. |
| `valid(grid)` | Checks grid dimensions, integer values within 0–9, and duplicate nonzero values in rows, columns, or subgrids. |
| `solve(grid)` | Finds empty cells and uses recursive backtracking to fill them with valid digits. |
| `print_grid(grid)` | Prints the resulting grid, one space-separated row per line. |

### Backtracking Steps

1. Find the next empty cell (`0`).
2. Try digits from 1 to 9.
3. Place a digit only if `safe()` confirms it satisfies Sudoku constraints.
4. Recursively solve the remaining cells.
5. If a choice does not lead to a solution, reset that cell to `0` and try the next digit.
6. Return success when no empty cells remain, or failure if no valid assignment exists.

## Input and Output

The program prompts for **9 lines**, each containing **9 space-separated integers**.

### Sample Input

```text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

### Expected Output

```text
Solved Sudoku grid:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

## Edge Cases Handled

| Case | Program Behavior |
| --- | --- |
| Valid, incomplete 9×9 Sudoku | Solves and prints the completed grid. |
| Already solved, valid Sudoku | Prints the same grid as the solution. |
| Row contains too many or too few numbers | Reports an invalid Sudoku grid. |
| Duplicate nonzero digit in a row, column, or 3×3 subgrid | Reports an invalid Sudoku grid. |
| Number outside the range 0–9 | Reports an invalid Sudoku grid. |
| Non-integer input | Prints `Invalid input`. |
| Input ends before 9 rows are provided | Prints `Invalid input`. |
| Valid initial grid with no solution | Prints `No solution exists for the given Sudoku puzzle.` |
| Completely empty 9×9 grid | Uses backtracking to find a valid solution. |

**Note:** An input containing a non-integer causes an input error; the solver does not accept decimal or text entries. The program reads exactly nine rows, so extra lines after those rows are not processed.

## How to Run

**Requirement:** Python 3 (no external packages required).

1. Clone the repository:

   ```bash
   git clone https://github.com/Vishwak21/Intel_Task.git
   ```

2. Open the project folder:

   ```bash
   cd Intel_Task
   ```

3. Run the submitted file:

   ```bash
   python "Sudoku(1).py"
   ```

4. Enter the Sudoku as nine rows of space-separated numbers, using `0` for blank cells.

## Complexity

- **Time:** In the worst case, up to **O(9^E)** possibilities may be explored, where `E` is the number of empty cells.
- **Auxiliary space:** **O(E)** for the recursion stack, excluding the stored grid.

## Conclusion

The project demonstrates recursive backtracking, Sudoku constraint checking, input validation, and error handling in Python. It requires no third-party libraries.
