# LeetCode 539: Minimum Time Difference

**LeetCode Problem #539 — Minimum Time Difference**
Solve LeetCode Minimum Time Difference using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Time Difference |
| LeetCode | #539 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a list of 24-hour clock time points in **"HH:MM"** format, return *the minimum minutes difference between any two time-points in the list*.

## Constraints
- `2 <= timePoints.length <= 2 * 10^4`
- `timePoints[i]` is in the format **"HH:MM"**.

## Examples
### Example 1
- **Input:** `timePoints = ["23:59","00:00"]`
- **Output:** `1`

### Example 2
- **Input:** `timePoints = ["00:00","23:59","00:00"]`
- **Output:** `0`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Time Difference**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `timePoints = ["23:59","00:00"]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0

        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)

        best = minutes[0] + 1440 - minutes[-1]  # wraparound gap
        for i in range(1, len(minutes)):
            best = min(best, minutes[i] - minutes[i - 1])
        return best
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [530. Minimum Absolute Difference in BST](../../0501-1000/0530-minimum-absolute-difference-in-bst/)
- [1200. Minimum Absolute Difference](../../1001-1500/1200-minimum-absolute-difference/)
- [1509. Minimum Difference Between Largest and Smallest Value in Three Moves](../../1501-2000/1509-minimum-difference-between-largest-and-smallest-value-in-three-moves/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-time-difference/)
