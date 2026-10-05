class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()
        result = []

        def backtrack(start, current, remaining):

            # Found a valid combination
            if remaining == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate values at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if candidates[i] > remaining:
                    break

                # Choose
                current.append(candidates[i])

                # Move to next index because each element
                # can only be used once
                backtrack(i + 1, current, remaining - candidates[i])

                # Undo
                current.pop()

        backtrack(0, [], target)

        return result
