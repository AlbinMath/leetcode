class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def height(first: int, second: int) -> int:
            have = [first, second]
            h = 0
            while True:
                need = h + 1
                idx = h % 2
                if have[idx] < need:
                    return h
                have[idx] -= need
                h += 1

        return max(height(red, blue), height(blue, red))
