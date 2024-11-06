def solveNQueens(n: int, first_queen_col: int):
    # Sets to keep track of occupied columns and diagonals
    col = set()
    posDiag = set()  # Positive diagonals (r + c)
    negDiag = set()  # Negative diagonals (r - c)

    # Store solutions and initialize empty board
    res = []
    board = [["0"] * n for _ in range(n)]

    def backtrack(r):
        # Base case: if we've placed queens in all rows, add solution
        if r == n:
            res.append(["".join(row) for row in board])
            return

        # Try placing queen in each column of current row
        for c in range(n):
            # Skip if column or diagonals are already occupied
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            # Place queen and update tracking sets
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "1"

            # Recursively try next row
            backtrack(r + 1)

            # Backtrack: remove queen and clear tracking sets
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "0"

    # Place first queen in specified column of first row
    col.add(first_queen_col)
    posDiag.add(0 + first_queen_col)
    negDiag.add(0 - first_queen_col)
    board[0][first_queen_col] = "1"

    backtrack(1)  # Start with the second row since first queen is fixed
    return res

if __name__ == "__main__":
    # Example usage with 4x4 board and first queen in column 1
    n = 6
    first_queen_col = 1
    board = solveNQueens(n, first_queen_col)[0]  # Get first solution
    # Print the solution
    for row in board:
        print(" ".join(row))



# This code solves the N-Queens problem with a fixed first queen position:
# 1. The solveNQueens function takes board size n and first queen's column position
# 2. Uses three sets to track occupied columns and diagonals
# 3. Uses backtracking to try placing queens row by row
# 4. The backtrack function:
#    - Base case: when all rows are filled (r == n)
#    - Tries each column in current row
#    - Checks if placement is valid (no conflicts)
#    - Places queen, updates tracking sets, and moves to next row
#    - Backtracks by removing queen if solution not found
# 5. First queen is placed in specified column of first row
# 6. Main section demonstrates usage with 4x4 board, first queen in column 1
# 7. Returns and prints one valid solution as a matrix of 0s and 1s