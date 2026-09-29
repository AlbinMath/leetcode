# Jump Game IV

## Problem Explanation
Given an array of integers, find the minimum number of jumps to reach the last index. From index `i`, you can jump to `i-1`, `i+1`, or to any index `j` where `arr[j] == arr[i]`.

## How the Code Works
The code uses **BFS** for shortest path.

1. **Group by Value:** Build a map from each value to all indices containing it.
2. **BFS:** Start from index `0`. Each level of BFS represents one jump. For each index, explore three types of neighbors: `i-1`, `i+1`, and all indices with the same value.
3. **Optimization:** After processing all indices of a value, erase that value from the map. This prevents revisiting the same group and ensures $O(N)$ total work.
4. Return the number of BFS levels when reaching index `n-1`.

Time complexity is $O(N)$ and space complexity is $O(N)$.
