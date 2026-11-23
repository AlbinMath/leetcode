class Solution(object):
    def movesToChessboard(self, board):
        n = len(board)

        # Every row must equal the first row or its complement (same for columns)
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1

        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))

        # Counts of 1s must be balanced
        if not (n // 2 <= row_sum <= (n + 1) // 2):
            return -1
        if not (n // 2 <= col_sum <= (n + 1) // 2):
            return -1

        # Mismatches against the pattern 0101...
        row_diff = sum(board[0][i] != i % 2 for i in range(n))
        col_diff = sum(board[i][0] != i % 2 for i in range(n))

        def calc(diff):
            if n % 2:
                # odd n: only the even mismatch count is achievable
                if diff % 2:
                    diff = n - diff
                return diff // 2
            return min(diff, n - diff) // 2

        return calc(row_diff) + calc(col_diff)
