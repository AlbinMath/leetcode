class Solution:

    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        # length[i] = length of result after processing s[0:i]
        length = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = length[i]

            if 'a' <= ch <= 'z':
                cur += 1

            elif ch == '*':
                if cur > 0:
                    cur -= 1

            elif ch == '#':
                cur *= 2

            elif ch == '%':
                # Reversing does not change length.
                pass

            length[i + 1] = cur

        # k is outside the final string.
        if k >= length[n]:
            return "."

        # Work backwards.
        for i in range(n - 1, -1, -1):
            ch = s[i]

            prev_len = length[i]
            cur_len = length[i + 1]

            # A normal character was appended.
            if 'a' <= ch <= 'z':
                # The appended character occupies the last position.
                if k == cur_len - 1:
                    return ch

                # Otherwise k belongs to the previous string.
                continue

            # '*' removed the last character.
            elif ch == '*':
                # The remaining characters keep the same indices.
                continue

            # '#' duplicated the string:
            #
            #   result = old + old
            #
            # Map an index from the second copy back to the first.
            elif ch == '#':
                if prev_len > 0:
                    k %= prev_len

            # '%' reversed the string.
            elif ch == '%':
                k = prev_len - 1 - k

        return "."
