class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subseq(a: str, b: str) -> bool:
            it = iter(b)
            return all(ch in it for ch in a)

        best = -1
        for i, s in enumerate(strs):
            if len(s) <= best:
                continue
            if all(i == j or not is_subseq(s, t) for j, t in enumerate(strs)):
                best = len(s)
        return best
