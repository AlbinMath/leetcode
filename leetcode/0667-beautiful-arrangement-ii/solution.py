class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        ans = list(range(1, n - k))
        left, right = n - k, n
        while left <= right:
            ans.append(left)
            left += 1
            if left <= right:
                ans.append(right)
                right -= 1
                
        return ans
