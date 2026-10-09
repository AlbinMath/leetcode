
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0

        # Climb while values are strictly increasing
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak cannot be the first or last element
        if i == 0 or i == n - 1:
            return False

        # Descend while values are strictly decreasing
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1

