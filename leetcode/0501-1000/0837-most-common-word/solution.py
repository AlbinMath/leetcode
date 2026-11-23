
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = re.findall(r"[a-z]+", paragraph.lower())
        banned_set = set(banned)

        word_counts = Counter(
            word for word in words if word not in banned_set
        )

        return word_counts.most_common(1)[0][0]

