from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:
            return 0

        ans = right  # remove arr[0..right-1]
        left = 0
        while left < right:
            while right < n and arr[right] < arr[left]:
                right += 1
            ans = min(ans, right - left - 1)
            if left + 1 < n and arr[left] > arr[left + 1]:
                break
            left += 1

        return ans
