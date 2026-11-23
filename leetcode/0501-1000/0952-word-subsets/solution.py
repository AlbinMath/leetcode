from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        need = [0] * 26
        for b in words2:
            for ch, c in Counter(b).items():
                i = ord(ch) - 97
                if c > need[i]:
                    need[i] = c

        res = []
        for a in words1:
            have = [0] * 26
            for ch in a:
                have[ord(ch) - 97] += 1
            if all(have[i] >= need[i] for i in range(26)):
                res.append(a)
        return res
