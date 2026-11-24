# LeetCode 2543: Check if Point Is Reachable

**LeetCode Problem #2543 — Check if Point Is Reachable**
Solve LeetCode Check if Point Is Reachable using Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Point Is Reachable |
| LeetCode | #2543 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There exists an infinitely large grid. You are currently at point `(1, 1)`, and you need to reach the point `(targetX, targetY)` using a finite number of steps.

In one **step**, you can move from point `(x, y)` to any one of the following points:

`(x, y - x)` 
 `(x - y, y)` 
 `(2 * x, y)` 
 `(x, 2 * y)`

Given two integers `targetX` and `targetY` representing the X-coordinate and Y-coordinate of your final position, return `true` *if you can reach the point from* `(1, 1)` *using some number of steps, and *`false`* otherwise*.

## Constraints
- `1 <= targetX, targetY <= 10^9`

## Examples
### Example 1
- **Input:** `targetX = 6, targetY = 9`
- **Output:** `false`
- **Explanation:** It is impossible to reach (6,9) from (1,1) using any sequence of moves, so false is returned.

### Example 2
- **Input:** `targetX = 4, targetY = 7`
- **Output:** `true`
- **Explanation:** You can follow the path (1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7).

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if Point Is Reachable**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `targetX = 6, targetY = 9`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** It is impossible to reach (6,9) from (1,1) using any sequence of moves, so false is returned.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from math import gcd
class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        return gcd(targetX, targetY) & (gcd(targetX, targetY) - 1) == 0
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3235. Check if the Rectangle Corner Is Reachable](../../3001-3500/3235-check-if-the-rectangle-corner-is-reachable/)
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1003-check-if-word-is-valid-after-substitutions/)
- [1232. Check If It Is a Straight Line](../../1001-1500/1232-check-if-it-is-a-straight-line/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-point-is-reachable/)
