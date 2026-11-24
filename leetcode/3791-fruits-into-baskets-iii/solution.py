from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size < n:
            size *= 2

        tree = [0] * (2 * size)
        for i, b in enumerate(baskets):
            tree[size + i] = b
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        unplaced = 0
        for f in fruits:
            if tree[1] < f:
                unplaced += 1
                continue
            node = 1
            while node < size:
                if tree[2 * node] >= f:
                    node = 2 * node
                else:
                    node = 2 * node + 1
            tree[node] = 0
            node //= 2
            while node >= 1:
                tree[node] = max(tree[2 * node], tree[2 * node + 1])
                node //= 2

        return unplaced
