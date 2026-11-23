class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        for w in words:
            node = trie
            for c in w:
                node = node.setdefault(c, {})
                node['#'] = node.get('#', 0) + 1
        ans = []
        for w in words:
            node = trie
            score = 0
            for c in w:
                node = node[c]
                score += node['#']
            ans.append(score)
        return ans
