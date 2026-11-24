
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        required = Counter(
            ch.lower() for ch in licensePlate if ch.isalpha()
        )

        result = ""

        for word in words:
            counts = Counter(word)

            if all(counts[ch] >= freq for ch, freq in required.items()):
                if not result or len(word) < len(result):
                    result = word

        return result

