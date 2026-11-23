import sys
from typing import List

# Extend recursion limit for deep chain trees
sys.setrecursionlimit(200000)

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [1] * n

        # If 1 is not present, all subtrees are missing 1
        if 1 not in nums:
            return ans

        # Build adjacency list
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)

        # Track observed genetic values and visited nodes
        seen_vals = [False] * 100005
        visited_nodes = [False] * n

        def dfs(u: int):
            visited_nodes[u] = True
            if nums[u] <= 100002:
                seen_vals[nums[u]] = True
            for child in children[u]:
                if not visited_nodes[child]:
                    dfs(child)

        curr = nums.index(1)
        missing = 1

        # Walk up from node with 1 to the root
        while curr != -1:
            dfs(curr)
            while seen_vals[missing]:
                missing += 1
            ans[curr] = missing
            curr = parents[curr]

        return ans
