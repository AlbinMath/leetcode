# LeetCode 754: Reach a Number

**LeetCode Problem #754 — Reach a Number**
Solve LeetCode Reach a Number using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reach a Number |
| LeetCode | #754 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are standing at position `0` on an infinite number line. There is a destination at position `target`.

You can make some number of moves `numMoves` so that:

On each move, you can either go left or right. 
 During the `i^th` move (starting from `i == 1` to `i == numMoves`), you take `i` steps in the chosen direction.

Given the integer `target`, return *the **minimum** number of moves required (i.e., the minimum *`numMoves`*) to reach the destination*.

## Constraints
- `-10^9 <= target <= 10^9`
- `target != 0`

## Examples
### Example 1
- **Input:** `target = 2`
- **Output:** `3`
- **Explanation:** On the 1^st move, we step from 0 to 1 (1 step).
On the 2^nd move, we step from 1 to -1 (2 steps).
On the 3^rd move, we step from -1 to 2 (3 steps).

### Example 2
- **Input:** `target = 3`
- **Output:** `2`
- **Explanation:** On the 1^st move, we step from 0 to 1 (1 step).
On the 2^nd move, we step from 1 to 3 (2 steps).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reach a Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** On the 1^st move, we step from 0 to 1 (1 step).
On the 2^nd move, we step from 1 to -1 (2 steps).
On the 3^rd move, we step from -1 to 2 (3 steps).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k, s = 0, 0

        while s < target or (s - target) % 2:
            k += 1
            s += k

        return k
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1557. Minimum Number of Vertices to Reach All Nodes](../../1501-2000/1557-minimum-number-of-vertices-to-reach-all-nodes/)
- [1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number](../../1501-2000/1850-minimum-adjacent-swaps-to-reach-the-kth-smallest-number/)
- [2400. Number of Ways to Reach a Position After Exactly k Steps](../../2001-2500/2400-number-of-ways-to-reach-a-position-after-exactly-k-steps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reach-a-number/)
