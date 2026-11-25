class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        return all(len(set(line)) == n for line in matrix) and \
               all(len(set(col)) == n for col in zip(*matrix))
