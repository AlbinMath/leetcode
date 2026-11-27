class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
            
        bits = []
        while n != 0:
            bits.append(str(n & 1))
            n = -(n >> 1)
            
        return "".join(reversed(bits))
