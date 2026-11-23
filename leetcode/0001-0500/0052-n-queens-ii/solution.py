class Solution:
    def totalNQueens(self, n):
        columns = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        def backtrack(row):
            # All queens placed successfully
            if row == n:
                return 1

            count = 0

            for col in range(n):

                # Check column
                if col in columns:
                    continue

                # Check \ diagonal
                if row - col in diag1:
                    continue

                # Check / diagonal
                if row + col in diag2:
                    continue

                # Place queen
                columns.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Explore
                count += backtrack(row + 1)

                # Backtrack
                columns.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

            return count

        return backtrack(0)
