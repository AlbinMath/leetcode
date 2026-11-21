class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []

        while a > 0 or b > 0:
            # Would adding 'a' create "aaa"?
            if len(res) >= 2 and res[-1] == res[-2]:
                write_a = res[-1] == 'b'   # last two are equal: pick the other letter
            else:
                write_a = a >= b           # otherwise take the larger pile

            if write_a:
                res.append('a')
                a -= 1
            else:
                res.append('b')
                b -= 1

        return ''.join(res)
