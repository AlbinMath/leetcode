class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        res = []
        for ch in s:
            if ch in res[-k:]:
                continue
            res.append(ch)
        return ''.join(res)
