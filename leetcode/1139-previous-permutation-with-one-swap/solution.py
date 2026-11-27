from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i < 0:
            return arr
        j = i + 1
        for k in range(i + 1, n):
            if arr[k] < arr[i] and arr[k] > arr[j]:
                j = k
        arr[i], arr[j] = arr[j], arr[i]
        return arr
