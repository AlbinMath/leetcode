# LeetCode 2833: Furthest Point From Origin

**LeetCode Problem #2833 — Furthest Point From Origin**
Solve LeetCode Furthest Point From Origin using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Furthest Point From Origin |
| LeetCode | #2833 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `moves` of length `n` consisting only of characters `'L'`, `'R'`, and `'_'`. The string represents your movement on a number line starting from the origin `0`.

In the `i^th` move, you can choose one of the following directions:

move to the left if `moves[i] = 'L'` or `moves[i] = '_'` 
 move to the right if `moves[i] = 'R'` or `moves[i] = '_'`

Return *the **distance from the origin** of the **furthest** point you can get to after *`n`* moves*.

## Constraints
- `1 <= moves.length == n <= 50`
- `moves` consists only of characters `'L'`, `'R'` and `'_'`.

## Examples
### Example 1
- **Input:** `moves = "L_RL__R"`
- **Output:** `3`
- **Explanation:** The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".

### Example 2
- **Input:** `moves = "_R__LL_"`
- **Output:** `5`
- **Explanation:** The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves "LRLLLLL".

### Example 3
- **Input:** `moves = "_______"`
- **Output:** `7`
- **Explanation:** The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves "RRRRRRR".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Furthest Point From Origin**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `moves = "L_RL__R"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".

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
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('L') - moves.count('R')) + moves.count('_')
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
- [478. Generate Random Point in a Circle](../../0001-0500/0478-generate-random-point-in-a-circle/)
- [497. Random Point in Non-overlapping Rectangles](../../0001-0500/0497-random-point-in-non-overlapping-rectangles/)
- [1779. Find Nearest Point That Has the Same X or Y Coordinate](../../1501-2000/1779-find-nearest-point-that-has-the-same-x-or-y-coordinate/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/furthest-point-from-origin/)
