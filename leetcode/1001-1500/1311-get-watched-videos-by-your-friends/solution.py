from collections import Counter, deque

class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        q = deque([id])
        seen = {id}

        for _ in range(level):
            for _ in range(len(q)):
                u = q.popleft()
                for v in friends[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)

        cnt = Counter()
        for u in q:
            cnt.update(watchedVideos[u])

        return sorted(cnt, key=lambda x: (cnt[x], x))
