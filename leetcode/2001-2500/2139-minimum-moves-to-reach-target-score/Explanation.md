# LeetCode 2139: Minimum Moves to Reach Target Score

**LeetCode Problem #2139 — Minimum Moves to Reach Target Score**
Solve LeetCode Minimum Moves to Reach Target Score using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Reach Target Score |
| LeetCode | #2139 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are playing a game with integers. You start with the integer `1` and you want to reach the integer `target`.

In one move, you can either:

**Increment** the current integer by one (i.e., `x = x + 1`). 
 **Double** the current integer (i.e., `x = 2 * x`).

You can use the **increment** operation **any** number of times, however, you can only use the **double** operation **at most** `maxDoubles` times.

Given the two integers `target` and `maxDoubles`, return *the minimum number of moves needed to reach *`target`* starting with *`1`.

## Constraints
- `1 <= target <= 10^9`
- `0 <= maxDoubles <= 100`

## Examples
### Example 1
- **Input:** `target = 5, maxDoubles = 0`
- **Output:** `4`
- **Explanation:** Keep incrementing by 1 until you reach target.

### Example 2
- **Input:** `target = 19, maxDoubles = 2`
- **Output:** `7`
- **Explanation:** Initially, x = 1
Increment 3 times so x = 4
Double once so x = 8
Increment once so x = 9
Double again so x = 18
Increment once so x = 19

### Example 3
- **Input:** `target = 10, maxDoubles = 4`
- **Output:** `4`
- **Explanation:** Initially, x = 1
Increment once so x = 2
Double once so x = 4
Increment once so x = 5
Double again so x = 10

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Moves to Reach Target Score**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = 5, maxDoubles = 0`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Keep incrementing by 1 until you reach target.

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
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            moves += 1
        return moves + (target - 1)
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
- [1210. Minimum Moves to Reach Target with Rotations](../../1001-1500/1210-minimum-moves-to-reach-target-with-rotations/)
- [1263. Minimum Moves to Move a Box to Their Target Location](../../1001-1500/1263-minimum-moves-to-move-a-box-to-their-target-location/)
- [3810. Minimum Operations to Reach Target Array](../../3501-4000/3810-minimum-operations-to-reach-target-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-reach-target-score/)
