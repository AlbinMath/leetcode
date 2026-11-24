class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        frequency = {}
        count = 0

        for num in nums:
            count += frequency.get(num, 0)
            frequency[num] = frequency.get(num, 0) + 1

        return count
