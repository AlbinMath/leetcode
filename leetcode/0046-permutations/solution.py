class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path, used):
            # We have selected all numbers
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                # Skip numbers already used
                if used[i]:
                    continue

                # Choose
                path.append(nums[i])
                used[i] = True

                # Explore
                backtrack(path, used)

                # Undo choice
                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))

        return result
