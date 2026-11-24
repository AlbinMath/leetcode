
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        smallest = min(nums)
        largest = max(nums)

        return max(0, largest - smallest - 2 * k)

