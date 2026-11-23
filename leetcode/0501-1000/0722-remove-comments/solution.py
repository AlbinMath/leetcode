class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        buf = []
        in_block = False

        for line in source:
            i, n = 0, len(line)
            while i < n:
                two = line[i:i + 2]
                if in_block:
                    if two == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1
                else:
                    if two == "/*":
                        in_block = True
                        i += 2
                    elif two == "//":
                        break
                    else:
                        buf.append(line[i])
                        i += 1

            if not in_block and buf:
                res.append(''.join(buf))
                buf = []

        return res
