from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        pairs = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]
        if not pairs:
            return 0

        start = "".join(c1 for c1, _ in pairs)
        target = "".join(c2 for _, c2 in pairs)
        n = len(start)

        queue = deque([start])
        visited = {start}
        steps = 0

        while queue:
            steps += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                i = 0
                while curr[i] == target[i]:
                    i += 1

                # Check for an optimal 2-cycle swap first
                candidates = []
                for j in range(i + 1, n):
                    if curr[j] == target[i] and curr[j] != target[j]:
                        if curr[i] == target[j]:
                            candidates = [j]
                            break
                        candidates.append(j)

                lst = list(curr)
                for j in candidates:
                    lst[i], lst[j] = lst[j], lst[i]
                    nxt = "".join(lst)
                    if nxt == target:
                        return steps
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
                    lst[i], lst[j] = lst[j], lst[i]

        return steps
