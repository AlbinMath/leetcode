# LeetCode 1954: Minimum Garden Perimeter to Collect Enough Apples

**LeetCode Problem #1954 — Minimum Garden Perimeter to Collect Enough Apples**
Solve LeetCode Minimum Garden Perimeter to Collect Enough Apples using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Garden Perimeter to Collect Enough Apples |
| LeetCode | #1954 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
In a garden represented as an infinite 2D grid, there is an apple tree planted at **every** integer coordinate. The apple tree planted at an integer coordinate `(i, j)` has `|i| + |j|` apples growing on it.

You will buy an axis-aligned **square plot** of land that is centered at `(0, 0)`.

Given an integer `neededApples`, return *the **minimum perimeter** of a plot such that **at least***** **`neededApples` *apples are **inside or on** the perimeter of that plot*.

The value of `|x|` is defined as:

`x` if `x >= 0` 
 `-x` if `x < 0`

## Constraints
- `1 <= neededApples <= 10^15`

## Examples
### Example 1
- **Input:** `neededApples = 1`
- **Output:** `8`
- **Explanation:** A square plot of side length 1 does not contain any apples.
However, a square plot of side length 2 has 12 apples inside (as depicted in the image above).
The perimeter is 2 * 4 = 8.

### Example 2
- **Input:** `neededApples = 13`
- **Output:** `16`

### Example 3
- **Input:** `neededApples = 1000000000`
- **Output:** `5040`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Garden Perimeter to Collect Enough Apples**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `neededApples = 1`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** A square plot of side length 1 does not contain any apples.
However, a square plot of side length 2 has 12 apples inside (as depicted in the image above).
The perimeter is 2 * 4 = 8.

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
    def minimumPerimeter(self, neededApples: int) -> int:
        def apples(r: int) -> int:
            return 2 * r * (r + 1) * (2 * r + 1)

        lo, hi = 1, 100_000
        while lo < hi:
            mid = (lo + hi) // 2
            if apples(mid) >= neededApples:
                hi = mid
            else:
                lo = mid + 1

        return 8 * lo
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
- [1443. Minimum Time to Collect All Apples in a Tree](../../1001-1500/1443-minimum-time-to-collect-all-apples-in-a-tree/)
- [3928. Minimum Cost to Buy Apples II](../../3501-4000/3928-minimum-cost-to-buy-apples-ii/)
- [1326. Minimum Number of Taps to Open to Water a Garden](../../1001-1500/1326-minimum-number-of-taps-to-open-to-water-a-garden/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/)
