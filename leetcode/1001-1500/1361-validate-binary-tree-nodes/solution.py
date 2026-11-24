from collections import deque
from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        in_degree = [0] * n

        # 1. Compute in-degree for each node
        for child in leftChild + rightChild:
            if child != -1:
                in_degree[child] += 1
                if in_degree[child] > 1:
                    return False  # A node cannot have more than one parent

        # 2. Identify the single root candidate (in-degree == 0)
        root = -1
        for i in range(n):
            if in_degree[i] == 0:
                if root != -1:
                    return False  # Multiple roots -> multiple disconnected trees
                root = i

        if root == -1:
            return False  # Cycle among all nodes (no root)

        # 3. BFS traversal to verify connectivity and absence of cycles
        visited = [False] * n
        queue = deque([root])
        visited[root] = True
        count = 0

        while queue:
            node = queue.popleft()
            count += 1

            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    if visited[child]:
                        return False  # Cycle detected
                    visited[child] = True
                    queue.append(child)

        # All n nodes must be reachable from the root
        return count == n
