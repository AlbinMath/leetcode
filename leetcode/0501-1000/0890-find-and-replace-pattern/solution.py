class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def shape(w: str):
            first = {}
            return [first.setdefault(ch, len(first)) for ch in w]

        target = shape(pattern)
        return [w for w in words if shape(w) == target]
