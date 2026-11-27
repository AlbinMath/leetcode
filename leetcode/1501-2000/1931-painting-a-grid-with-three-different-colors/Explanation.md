# LeetCode 1931: Painting a Grid With Three Different Colors

**LeetCode Problem #1931 — Painting a Grid With Three Different Colors**
Solve LeetCode Painting a Grid With Three Different Colors using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Painting a Grid With Three Different Colors |
| LeetCode | #1931 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers `m` and `n`. Consider an `m x n` grid where each cell is initially white. You can paint each cell **red**, **green**, or **blue**. All cells **must** be painted.

Return* the number of ways to color the grid with **no two adjacent cells having the same color***. Since the answer can be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= m <= 5`
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `m = 1, n = 1`
- **Output:** `3`
- **Explanation:** The three possible colorings are shown in the image above.

### Example 2
- **Input:** `m = 1, n = 2`
- **Output:** `6`
- **Explanation:** The six possible colorings are shown in the image above.

### Example 3
- **Input:** `m = 5, n = 5`
- **Output:** `580986`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Painting a Grid With Three Different Colors**, we observe the problem requirements and utilize the **Tree & Graph** technique. We decompose the problem into overlapping subproblems using a **Tree / Graph / Grid**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `m = 1, n = 1`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The three possible colorings are shown in the image above.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        valid_cols = []
        
        def backtrack(row: int, current: list[int]) -> None:
            if row == m:
                valid_cols.append(tuple(current))
                return
            for color in range(3):
                if row == 0 or current[-1] != color:
                    current.append(color)
                    backtrack(row + 1, current)
                    current.pop()
                    
        backtrack(0, [])
        num_states = len(valid_cols)
        
        adj = [[] for _ in range(num_states)]
        for i in range(num_states):
            for j in range(i + 1, num_states):
                if all(a != b for a, b in zip(valid_cols[i], valid_cols[j])):
                    adj[i].append(j)
                    adj[j].append(i)
                    
        dp = [1] * num_states
        for _ in range(n - 1):
            next_dp = [0] * num_states
            for i in range(num_states):
                total = 0
                for prev in adj[i]:
                    total += dp[prev]
                next_dp[i] = total % MOD
            dp = next_dp
            
        return sum(dp) % MOD
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
- [2078. Two Furthest Houses With Different Colors](../../2001-2500/2078-two-furthest-houses-with-different-colors/)
- [1878. Get Biggest Three Rhombus Sums in a Grid](../../1501-2000/1878-get-biggest-three-rhombus-sums-in-a-grid/)
- [241. Different Ways to Add Parentheses](../../0001-0500/0241-different-ways-to-add-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/painting-a-grid-with-three-different-colors/)
