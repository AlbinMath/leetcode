class Solution:
    def findReplaceString(self, s: str, indices: List[int],
                          sources: List[str], targets: List[str]) -> str:
        match = {}  # start index -> (source length, target)
        for idx, src, tgt in zip(indices, sources, targets):
            if s.startswith(src, idx):
                match[idx] = (len(src), tgt)

        res = []
        i = 0
        while i < len(s):
            if i in match:
                length, tgt = match[i]
                res.append(tgt)
                i += length
            else:
                res.append(s[i])
                i += 1

        return ''.join(res)
