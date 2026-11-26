from collections import Counter
from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        user_langs = [set(langs) for langs in languages]
        need_help = set()
        for u, v in friendships:
            u_idx, v_idx = u - 1, v - 1
            if user_langs[u_idx].isdisjoint(user_langs[v_idx]):
                need_help.add(u_idx)
                need_help.add(v_idx)
                
        if not need_help:
            return 0
        lang_counts = Counter()
        for user in need_help:
            for lang in user_langs[user]:
                lang_counts[lang] += 1
        max_known = max(lang_counts.values(), default=0)
        return len(need_help) - max_known
