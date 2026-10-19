class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        return [q for q in queries if any(sum(a != b for a, b in zip(q, w)) <= 2 for w in dictionary)]
