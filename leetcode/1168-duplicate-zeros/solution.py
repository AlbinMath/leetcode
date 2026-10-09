from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        original = arr.copy()
        i = 0
        j = 0

        while i < len(arr):
            arr[i] = original[j]
            i += 1

            if original[j] == 0 and i < len(arr):
                arr[i] = 0
                i += 1

            j += 1
