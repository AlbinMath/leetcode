class Solution:
    def isNumber(self, s):
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):

            if ch.isdigit():
                seen_digit = True

            elif ch in '+-':
                # Sign is allowed only at the beginning
                # or immediately after e/E
                if i > 0 and s[i - 1] not in 'eE':
                    return False

            elif ch == '.':
                # Dot is not allowed after an exponent
                # and only one dot is allowed
                if seen_dot or seen_exp:
                    return False

                seen_dot = True

            elif ch in 'eE':
                # Only one exponent is allowed
                # and exponent must have a digit before it
                if seen_exp or not seen_digit:
                    return False

                seen_exp = True
                seen_digit = False

            else:
                return False

        return seen_digit
