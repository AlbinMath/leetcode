from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        words = set(wordList)
        if endWord not in words:
            return []

        parents = defaultdict(list)
        q = deque([beginWord])
        visited = {beginWord}
        found = False

        while q and not found:
            level = set()
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nxt = word[:i] + c + word[i + 1:]
                        if nxt in words and nxt not in visited:
                            parents[nxt].append(word)
                            if nxt not in level:
                                level.add(nxt)
                                q.append(nxt)
                            if nxt == endWord:
                                found = True
            visited.update(level)

        res = []
        def backtrack(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [p])

        if found:
            backtrack(endWord, [endWord])
        return res
