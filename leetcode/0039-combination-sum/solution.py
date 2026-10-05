class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(start, current, remaining):

            # Found a valid combination
            if remaining == 0:
                result.append(current[:])
                return

            # Sum is too large
            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                value = candidates[i]

                # Since candidates are sorted,
                # no later value can work either.
                if value > remaining:
                    break

                # Choose
                current.append(value)

                # We pass i, not i + 1,
                # because the same number can be reused.
                backtrack(i, current, remaining - value)

                # Undo
                current.pop()

        candidates.sort()
        backtrack(0, [], target)

        return result
