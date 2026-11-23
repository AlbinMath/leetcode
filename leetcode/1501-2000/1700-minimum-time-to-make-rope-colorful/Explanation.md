# LeetCode 1578: Minimum Time to Make Rope Colorful

**LeetCode Problem #1578 — Minimum Time to Make Rope Colorful**
Solve LeetCode Minimum Time to Make Rope Colorful using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time to Make Rope Colorful |
| LeetCode | #1578 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Alice has `n` balloons arranged on a rope. You are given a **0-indexed** string `colors` where `colors[i]` is the color of the `i^th` balloon.

Alice wants the rope to be **colorful**. She does not want **two consecutive balloons** to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it **colorful**. You are given a **0-indexed** integer array `neededTime` where `neededTime[i]` is the time (in seconds) that Bob needs to remove the `i^th` balloon from the rope.

Return *the **minimum time** Bob needs to make the rope **colorful***.

## Constraints
- `n == colors.length == neededTime.length`
- `1 <= n <= 10^5`
- `1 <= neededTime[i] <= 10^4`
- `colors` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `colors = "abaac", neededTime = [1,2,3,4,5]`
- **Output:** `3`
- **Explanation:** In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

### Example 2
- **Input:** `colors = "abc", neededTime = [1,2,3]`
- **Output:** `0`
- **Explanation:** The rope is already colorful. Bob does not need to remove any balloons from the rope.

### Example 3
- **Input:** `colors = "aabaa", neededTime = [1,2,3,4,1]`
- **Output:** `2`
- **Explanation:** Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time to Make Rope Colorful**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `colors = "abaac", neededTime = [1,2,3,4,5]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

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
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        prev_max = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                total += min(prev_max, neededTime[i])
                prev_max = max(prev_max, neededTime[i])
            else:
                prev_max = neededTime[i]

        return total
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
- [539. Minimum Time Difference](../../0501-1000/0539-minimum-time-difference/)
- [1266. Minimum Time Visiting All Points](../../1001-1500/1395-minimum-time-visiting-all-points/)
- [1443. Minimum Time to Collect All Apples in a Tree](../../1501-2000/1554-minimum-time-to-collect-all-apples-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/)
