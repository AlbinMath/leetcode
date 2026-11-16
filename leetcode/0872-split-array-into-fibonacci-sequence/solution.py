from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        LIMIT = 2**31

        for i in range(1, min(11, n)):          # length of first number
            if i > 1 and num[0] == "0":
                break                            # leading zero, longer prefixes fail too
            a = int(num[:i])
            if a >= LIMIT:
                break
            for j in range(1, min(11, n - i)):   # length of second number
                if j > 1 and num[i] == "0":
                    break
                b = int(num[i:i + j])
                if b >= LIMIT:
                    break

                seq = [a, b]
                pos = i + j
                x, y = a, b
                while pos < n:
                    z = x + y
                    if z >= LIMIT:
                        break
                    s = str(z)
                    if not num.startswith(s, pos):
                        break
                    seq.append(z)
                    pos += len(s)
                    x, y = y, z
                if pos == n and len(seq) >= 3:
                    return seq
        return []
