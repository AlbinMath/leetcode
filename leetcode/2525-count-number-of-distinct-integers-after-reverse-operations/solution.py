class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        distinct = set(nums)
        
        for num in list(distinct):
            rev = 0
            temp = num
            while temp > 0:
                rev = rev * 10 + temp % 10
                temp //= 10
            distinct.add(rev)
            
        return len(distinct)
