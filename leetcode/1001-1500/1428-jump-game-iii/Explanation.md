# LeetCode 1306: Jump Game III

**LeetCode Problem #1306 — Jump Game III**
Solve LeetCode Jump Game III using C++ and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game III |
| LeetCode | #1306 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, check if you can reach **any** index with value 0.

Notice that you can not jump outside of the array at any time.

## Constraints
- `1 <= arr.length <= 5 * 10^4`
- `0 <= arr[i] < arr.length`
- `0 <= start < arr.length`

## Examples
### Example 1
- **Input:** `arr = [4,2,3,0,3,1,2], start = 5`
- **Output:** `true`
- **Explanation:** All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3

### Example 2
- **Input:** `arr = [4,2,3,0,3,1,2], start = 0`
- **Output:** `true`
- **Explanation:** One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

### Example 3
- **Input:** `arr = [3,0,2,1,2], start = 2`
- **Output:** `false`
- **Explanation:** There is no way to reach at index 1 with value 0.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **BFS** (Breadth-First Search).

1. Start from the given index, mark it as visited, and add it to a queue.
2. For each index `i` dequeued: if `arr[i] == 0`, return `true`.
3. Otherwise, calculate the two possible jump destinations (`i + arr[i]` and `i - arr[i]`). If a destination is within bounds and unvisited, mark it visited and enqueue it.
4. If the queue empties without finding a `0`, return `false`.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [4,2,3,0,3,1,2], start = 5`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        vector<bool> visited(n, false);
        queue<int> q;

        q.push(start);
        visited[start] = true;

        while (!q.empty()) {
            int i = q.front();
            q.pop();

            // Reached an index with value 0
            if (arr[i] == 0)
                return true;

            // Jump right
            int right = i + arr[i];
            if (right < n && !visited[right]) {
                visited[right] = true;
                q.push(right);
            }

            // Jump left
            int left = i - arr[i];
            if (left >= 0 && !visited[left]) {
                visited[left] = true;
                q.push(left);
            }
        }

        return false;
    }
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [45. Jump Game II](../../0001-0500/0045-jump-game-ii/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)
- [1340. Jump Game V](../../1001-1500/1466-jump-game-v/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-iii/)
