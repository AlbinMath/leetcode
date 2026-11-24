class Solution(object):
    def countSubarrays(self, nums, k):
        ans = 0
        cur = {}
        for x in nums:
            nxt = {x: 1}
            for v, c in cur.items():
                w = v & x
                nxt[w] = nxt.get(w, 0) + c
            cur = nxt
            ans += cur.get(k, 0)
        return ans
