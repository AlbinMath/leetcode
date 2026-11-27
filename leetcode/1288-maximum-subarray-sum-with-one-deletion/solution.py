class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        no_del = arr[0]
        one_del = float('-inf')
        ans = arr[0]
        
        for x in arr[1:]:
            one_del = max(one_del + x, no_del)
            no_del = max(x, no_del + x)
            ans = max(ans, no_del, one_del)
            
        return ans
