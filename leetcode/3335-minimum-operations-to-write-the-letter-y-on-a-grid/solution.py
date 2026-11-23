class Solution:
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        n = len(grid)
        mid = n // 2
        
        y_counts = [0, 0, 0]
        bg_counts = [0, 0, 0]
        
        for r in range(n):
            for c in range(n):
                is_y = (r <= mid and (r == c or r + c == n - 1)) or (r > mid and c == mid)
                if is_y:
                    y_counts[grid[r][c]] += 1
                else:
                    bg_counts[grid[r][c]] += 1
                    
        total_y = sum(y_counts)
        total_bg = sum(bg_counts)
        min_ops = n * n
        
        for y_val in range(3):
            for bg_val in range(3):
                if y_val != bg_val:
                    ops = (total_y - y_counts[y_val]) + (total_bg - bg_counts[bg_val])
                    min_ops = min(min_ops, ops)
                    
        return min_ops
