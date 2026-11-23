class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            return s.count(min(s))

        # suffix[v] = number of words with f(word) >= v; size 12 so suffix[11] = 0
        suffix = [0] * 12
        for w in words:
            suffix[f(w)] += 1
        for v in range(10, 0, -1):
            suffix[v] += suffix[v + 1]

        return [suffix[f(q) + 1] for q in queries]
