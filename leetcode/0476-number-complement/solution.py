class Solution:
    def findComplement(self, num):
        mask = 0
        temp = num

        # Create a mask containing all 1s
        # with the same number of bits as num
        while temp:
            mask = (mask << 1) | 1
            temp >>= 1

        # Flip only the relevant bits
        return num ^ mask
