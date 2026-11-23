from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        END = '#'
        for root in dictionary:
            node = trie
            for ch in root:
                node = node.setdefault(ch, {})
            node[END] = True

        def shortest(word):
            node = trie
            for i, ch in enumerate(word):
                if ch not in node:
                    return word
                node = node[ch]
                if END in node:
                    return word[:i + 1]
            return word

        return ' '.join(shortest(w) for w in sentence.split())
