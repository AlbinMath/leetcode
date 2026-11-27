class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        total_ones = sum(arr)
        
        if total_ones == 0:
            return [0, 2]
        if total_ones % 3 != 0:
            return [-1, -1]
            
        k = total_ones // 3
        p1 = p2 = p3 = -1
        ones_seen = 0
        for idx, bit in enumerate(arr):
            if bit == 1:
                ones_seen += 1
                if ones_seen == 1:
                    p1 = idx
                elif ones_seen == k + 1:
                    p2 = idx
                elif ones_seen == 2 * k + 1:
                    p3 = idx
                    break
        n = len(arr)
        while p3 < n:
            if arr[p1] != arr[p2] or arr[p2] != arr[p3]:
                return [-1, -1]
            p1 += 1
            p2 += 1
            p3 += 1
            
        return [p1 - 1, p2]
