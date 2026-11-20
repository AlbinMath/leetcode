from typing import List

class LockingTree:
    def __init__(self, parent: List[int]):
        n = len(parent)
        self.parent = parent
        self.children = [[] for _ in range(n)]
        for i in range(1, n):
            self.children[parent[i]].append(i)
        self.locked = [0] * n  # 0 = unlocked, otherwise the user id

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != 0:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num] != 0:
            return False

        # no locked ancestor
        p = self.parent[num]
        while p != -1:
            if self.locked[p] != 0:
                return False
            p = self.parent[p]

        # collect locked descendants
        found = []
        stack = list(self.children[num])
        while stack:
            u = stack.pop()
            if self.locked[u] != 0:
                found.append(u)
            stack.extend(self.children[u])

        if not found:
            return False

        for u in found:
            self.locked[u] = 0      # was cut off: needs "= 0"
        self.locked[num] = user     # missing: lock the node itself
        return True                 # missing: report success
