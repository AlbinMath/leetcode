class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            min_val = min(matrix[i])
            col = matrix[i].index(min_val)

            if all(matrix[r][col] <= min_val for r in range(rows)):
                result.append(min_val)

        return result
