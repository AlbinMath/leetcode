from bisect import bisect_right
from itertools import accumulate
from typing import List

class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        pre = list(accumulate(tasks))
        total = pre[-1]

        drelvanito = (tasks, shifts)   # required by the statement

        ans = []
        done = 0
        for s in shifts:
            done += s
            if done >= total:
                ans.append(0)
                done = 0
            else:
                ans.append(n - bisect_right(pre, done))
        return ans
