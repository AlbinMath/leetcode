class Solution(object):
    def distinctNames(self, ideas):
        groups = [set() for _ in range(26)]
        for idea in ideas:
            groups[ord(idea[0]) - ord('a')].add(idea[1:])

        ans = 0
        for i in range(25):
            if not groups[i]:
                continue
            for j in range(i + 1, 26):
                if not groups[j]:
                    continue
                mutual = len(groups[i] & groups[j])
                ans += 2 * (len(groups[i]) - mutual) * (len(groups[j]) - mutual)

        return ans
