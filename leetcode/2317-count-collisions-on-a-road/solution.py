class Solution:
    def countCollisions(self, directions: str) -> int:
        # Strip leading 'L's and trailing 'R's, then count remaining non-'S' cars
        trimmed = directions.lstrip('L').rstrip('R')
        return len(trimmed) - trimmed.count('S')
