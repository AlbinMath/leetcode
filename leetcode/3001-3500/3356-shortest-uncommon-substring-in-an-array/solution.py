class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        ans = []
        for i, s in enumerate(arr):
            subs = sorted({s[a:b] for a in range(len(s)) for b in range(a+1, len(s)+1)}, key=lambda x: (len(x), x))
            ans.append(next((x for x in subs if all(x not in t for j, t in enumerate(arr) if j != i)), ""))
        return ans
