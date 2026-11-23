class Solution(object):
    def minimizeXor(self, num1, num2):
        c = bin(num2).count('1')
        x = 0

        # match the highest set bits of num1 first
        for b in range(31, -1, -1):
            if c == 0:
                break
            if (num1 >> b) & 1:
                x |= 1 << b
                c -= 1

        # leftover ones go to the lowest unset bits of num1
        b = 0
        while c > 0:
            if not (x >> b) & 1:
                x |= 1 << b
                c -= 1
            b += 1
        return x
