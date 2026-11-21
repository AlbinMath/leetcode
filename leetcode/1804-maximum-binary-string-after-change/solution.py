class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        first = binary.find('0')
        if first == -1:
            return binary

        zeros = binary.count('0')
        n = len(binary)
        pos = first + zeros - 1  # index of the single remaining zero

        res = ['1'] * n
        res[pos] = '0'
        return ''.join(res)
