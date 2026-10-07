class Solution:
    def removeInvalidParentheses(self, s):
        left_remove = 0
        right_remove = 0

        # Find the minimum number of removals
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(index, path, balance, left_rem, right_rem):

            # Invalid parentheses
            if balance < 0:
                return

            # End of string
            if index == len(s):
                if balance == 0 and left_rem == 0 and right_rem == 0:
                    result.add(path)
                return

            ch = s[index]

            if ch == '(':

                # Remove '('
                if left_rem > 0:
                    backtrack(
                        index + 1,
                        path,
                        balance,
                        left_rem - 1,
                        right_rem
                    )

                # Keep '('
                backtrack(
                    index + 1,
                    path + ch,
                    balance + 1,
                    left_rem,
                    right_rem
                )

            elif ch == ')':

                # Remove ')'
                if right_rem > 0:
                    backtrack(
                        index + 1,
                        path,
                        balance,
                        left_rem,
                        right_rem - 1
                    )

                # Keep ')' only if possible
                if balance > 0:
                    backtrack(
                        index + 1,
                        path + ch,
                        balance - 1,
                        left_rem,
                        right_rem
                    )

            else:
                # Keep letters
                backtrack(
                    index + 1,
                    path + ch,
                    balance,
                    left_rem,
                    right_rem
                )

        backtrack(
            0,
            "",
            0,
            left_remove,
            right_remove
        )

        return list(result)
