from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        cnt = Counter(tasks)
        maxf = max(cnt.values())
        cnt_max = sum(1 for v in cnt.values() if v == maxf)
        return max(len(tasks), (maxf - 1) * (n + 1) + cnt_max)
