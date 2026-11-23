from collections import Counter

class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        sums.sort()
        ans = []
        
        for _ in range(n):
            d = sums[1] - sums[0]
            freq = Counter(sums)
            without_d = []
            with_d = []
            
            for x in sums:
                if freq[x] > 0:
                    freq[x] -= 1
                    freq[x + d] -= 1
                    without_d.append(x)
                    with_d.append(x + d)
            
            if 0 in without_d:
                ans.append(d)
                sums = without_d
            else:
                ans.append(-d)
                sums = with_d
                
        return ans
