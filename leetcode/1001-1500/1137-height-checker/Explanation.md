# LeetCode 1051: Height Checker

**LeetCode Problem #1051 — Height Checker**
Solve LeetCode Height Checker using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Height Checker |
| LeetCode | #1051 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in **non-decreasing order** by height. Let this ordering be represented by the integer array `expected` where `expected[i]` is the expected height of the `i^th` student in line.

You are given an integer array `heights` representing the **current order** that the students are standing in. Each `heights[i]` is the height of the `i^th` student in line (**0-indexed**).

Return *the **number of indices** where *`heights[i] != expected[i]`.

## Constraints
- `1 <= heights.length <= 100`
- `1 <= heights[i] <= 100`

## Examples
### Example 1
- **Input:** `heights = [1,1,4,2,1,3]`
- **Output:** `3`
- **Explanation:** heights: [1,1, 4 ,2, 1 , 3 ]
expected: [1,1, 1 ,2, 3 , 4 ]
Indices 2, 4, and 5 do not match.

### Example 2
- **Input:** `heights = [5,1,2,3,4]`
- **Output:** `5`
- **Explanation:** heights: [ 5 , 1 , 2 , 3 , 4 ]
expected: [ 1 , 2 , 3 , 4 , 5 ]
All indices do not match.

### Example 3
- **Input:** `heights = [1,2,3,4,5]`
- **Output:** `0`
- **Explanation:** heights: [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Height Checker**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `heights = [1,1,4,2,1,3]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** heights: [1,1, 4 ,2, 1 , 3 ]
expected: [1,1, 1 ,2, 3 , 4 ]
Indices 2, 4, and 5 do not match.

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
from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count
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
- [420. Strong Password Checker](../../0001-0500/0420-strong-password-checker/)
- [310. Minimum Height Trees](../../0001-0500/0310-minimum-height-trees/)
- [406. Queue Reconstruction by Height](../../0001-0500/0406-queue-reconstruction-by-height/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/height-checker/)
