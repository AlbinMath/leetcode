class Solution:
    def partition(self, s):
        res = []
        def dfs(i, path):
            if i == len(s):
                res.append(path[:])
                return
            for j in range(i, len(s)):
                t = s[i:j+1]
                if t == t[::-1]:
                    dfs(j+1, path+[t])
        dfs(0, [])
        return res
