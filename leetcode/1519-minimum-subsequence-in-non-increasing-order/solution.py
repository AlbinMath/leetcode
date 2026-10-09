class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        selected = []
        selected_sum = 0

        for num in nums:
            selected.append(num)
            selected_sum += num

            if selected_sum > total - selected_sum:
                break

        return selected
