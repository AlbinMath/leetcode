
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        last_position = -1
        max_gap = 0

        for i, bit in enumerate(binary):
            if bit == '1':
                if last_position != -1:
                    max_gap = max(max_gap, i - last_position)
                last_position = i

        return max_gap

