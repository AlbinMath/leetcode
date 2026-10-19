from collections import Counter

class Encrypter:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.mp = dict(zip(keys, values))
        self.cnt = Counter(self.encrypt(w) for w in dictionary)

    def encrypt(self, word1: str) -> str:
        return ''.join(self.mp.get(c, '') for c in word1) if all(c in self.mp for c in word1) else ''

    def decrypt(self, word2: str) -> int:
        return self.cnt[word2]
