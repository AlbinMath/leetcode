class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for r in range(rows):
            # Build histogram heights for the current row
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Find the largest rectangle in this histogram
            stack = []
            for c in range(cols + 1):
                current_height = heights[c] if c < cols else 0

                while stack and heights[stack[-1]] > current_height:
                    h = heights[stack.pop()]

                    left_boundary = stack[-1] if stack else -1
                    width = c - left_boundary - 1

                    max_area = max(max_area, h * width)

                stack.append(c)

        return max_area
