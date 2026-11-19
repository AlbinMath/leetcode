from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = down = max_len = 1
        
        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                up, down = down + 1, 1
            elif arr[i - 1] > arr[i]:
                down, up = up + 1, 1
            else:
                up = down = 1
                
            if up > max_len:
                max_len = up
            if down > max_len:
                max_len = down
                
        return max_len
