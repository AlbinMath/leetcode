class Solution(object):
    def searchMatrix(self, matrix, target):
        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            val = matrix[r][c]
            if val == target:
                return True
            elif val > target:
                c -= 1
            else:
                r += 1

        return False
