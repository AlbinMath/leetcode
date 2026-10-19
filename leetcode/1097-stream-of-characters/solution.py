from typing import List

class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = {}
        self.max_len = 0
        for w in words:
            node = self.root
            for ch in reversed(w):
                node = node.setdefault(ch, {})
            node['$'] = True          # marks end of a (reversed) word
            self.max_len = max(self.max_len, len(w))
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        if len(self.stream) > self.max_len:
            self.stream.pop(0)        # drop oldest char (at most 200 elements)

        node = self.root
        for ch in reversed(self.stream):
            if ch not in node:
                return False
            node = node[ch]
            if '$' in node:
                return True
        return False
