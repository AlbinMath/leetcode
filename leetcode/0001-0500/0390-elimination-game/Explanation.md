# LeetCode 390: Elimination Game

**LeetCode Problem #390 — Elimination Game**
Solve LeetCode Elimination Game using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Elimination Game |
| LeetCode | #390 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:

Starting from left to right, remove the first number and every other number afterward until you reach the end of the list. 
 Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers. 
 Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Given the integer `n`, return *the last number that remains in* `arr`.

## Constraints
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 9`
- **Output:** `6`
- **Explanation:** arr = [ 1 , 2, 3 , 4, 5 , 6, 7 , 8, 9 ]
arr = [2, 4 , 6, 8 ]
arr = [ 2 , 6]
arr = [6]

### Example 2
- **Input:** `n = 1`
- **Output:** `1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Elimination Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 9`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** arr = [ 1 , 2, 3 , 4, 5 , 6, 7 , 8, 9 ]
arr = [2, 4 , 6, 8 ]
arr = [ 2 , 6]
arr = [6]

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
    def lastRemaining(self, n: int) -> int:
        head, step, remaining = 1, 1, n
        left_to_right = True

        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right

        return head
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
- [1293. Shortest Path in a Grid with Obstacles Elimination](../../1001-1500/1293-shortest-path-in-a-grid-with-obstacles-elimination/)
- [45. Jump Game II](../../0001-0500/0045-jump-game-ii/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/elimination-game/)
