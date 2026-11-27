from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        n = len(clips)
        cur_end = 0
        farthest = 0
        count = 0
        i = 0
        while cur_end < time:
            while i < n and clips[i][0] <= cur_end:
                farthest = max(farthest, clips[i][1])
                i += 1
            if farthest <= cur_end:
                return -1
            cur_end = farthest
            count += 1
        return count
