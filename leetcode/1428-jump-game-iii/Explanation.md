# Jump Game III

## Problem Explanation
Given an array of non-negative integers `arr` and a starting index, you can jump from index `i` to `i + arr[i]` or `i - arr[i]`. Return whether you can reach any index with value `0`.

## How the Code Works
The code uses **BFS** (Breadth-First Search).

1. Start from the given index, mark it as visited, and add it to a queue.
2. For each index `i` dequeued: if `arr[i] == 0`, return `true`.
3. Otherwise, calculate the two possible jump destinations (`i + arr[i]` and `i - arr[i]`). If a destination is within bounds and unvisited, mark it visited and enqueue it.
4. If the queue empties without finding a `0`, return `false`.

Time complexity is $O(N)$ and space complexity is $O(N)$.
