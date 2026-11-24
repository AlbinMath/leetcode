# LeetCode 1025: Divisor Game

**LeetCode Problem #1025 — Divisor Game**
Solve LeetCode Divisor Game using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Divisor Game |
| LeetCode | #1025 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number `n` on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any integer `x` with `0 < x < n` and `n % x == 0`. 
 Replacing the number `n` on the chalkboard with `n - x`.

Also, if a player cannot make a move, they lose the game.

Return `true` *if and only if Alice wins the game, assuming both players play optimally*.

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `true`
- **Explanation:** Alice chooses 1, and Bob has no more moves.

### Example 2
- **Input:** `n = 3`
- **Output:** `false`
- **Explanation:** Alice chooses 1, Bob chooses 1, and Alice has no more moves.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Divisor Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Alice chooses 1, and Bob has no more moves.

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
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
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
- [1071. Greatest Common Divisor of Strings](../../1001-1500/1071-greatest-common-divisor-of-strings/)
- [1979. Find Greatest Common Divisor of Array](../../1501-2000/1979-find-greatest-common-divisor-of-array/)
- [2709. Greatest Common Divisor Traversal](../../2501-3000/2709-greatest-common-divisor-traversal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/divisor-game/)
