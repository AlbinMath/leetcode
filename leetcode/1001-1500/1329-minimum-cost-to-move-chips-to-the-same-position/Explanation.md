# LeetCode 1217: Minimum Cost to Move Chips to The Same Position

**LeetCode Problem #1217 — Minimum Cost to Move Chips to The Same Position**
Solve LeetCode Minimum Cost to Move Chips to The Same Position using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Move Chips to The Same Position |
| LeetCode | #1217 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
We have `n` chips, where the position of the `i^th` chip is `position[i]`.

We need to move all the chips to **the same position**. In one step, we can change the position of the `i^th` chip from `position[i]` to:

`position[i] + 2` or `position[i] - 2` with `cost = 0`. 
 `position[i] + 1` or `position[i] - 1` with `cost = 1`.

Return *the minimum cost* needed to move all the chips to the same position.

## Constraints
- `1 <= position.length <= 100`
- `1 <= position[i] <= 10^9`

## Examples
### Example 1
- **Input:** `position = [1,2,3]`
- **Output:** `1`
- **Explanation:** First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.

### Example 2
- **Input:** `position = [2,2,2,3,3]`
- **Output:** `2`
- **Explanation:** We can move the two chips at position 3 to position 2. Each move has cost = 1. The total cost = 2.

### Example 3
- **Input:** `position = [1,1000000000]`
- **Output:** `1`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost to Move Chips to The Same Position**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `position = [1,2,3]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** First step: Move the chip at position 3 to position 1 with cost = 0.
Second step: Move the chip at position 2 to position 1 with cost = 1.
Total cost is 1.

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
from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = sum(1 for p in position if p % 2 == 0)
        odd = len(position) - even

        return min(even, odd)
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
- [1263. Minimum Moves to Move a Box to Their Target Location](../../1001-1500/1389-minimum-moves-to-move-a-box-to-their-target-location/)
- [1769. Minimum Number of Operations to Move All Balls to Each Box](../../1501-2000/1895-minimum-number-of-operations-to-move-all-balls-to-each-box/)
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1228-minimum-cost-tree-from-leaf-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/)
