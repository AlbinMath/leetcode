# LeetCode 822: Card Flipping Game

**LeetCode Problem #822 — Card Flipping Game**
Solve LeetCode Card Flipping Game using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Card Flipping Game |
| LeetCode | #822 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** integer arrays `fronts` and `backs` of length `n`, where the `i^th` card has the positive integer `fronts[i]` printed on the front and `backs[i]` printed on the back. Initially, each card is placed on a table such that the front number is facing up and the other is facing down. You may flip over any number of cards (possibly zero).

After flipping the cards, an integer is considered **good** if it is facing down on some card and **not** facing up on any card.

Return *the minimum possible good integer after flipping the cards*. If there are no good integers, return `0`.

## Constraints
- `n == fronts.length == backs.length`
- `1 <= n <= 1000`
- `1 <= fronts[i], backs[i] <= 2000`

## Examples
### Example 1
- **Input:** `fronts = [1,2,4,4,7], backs = [1,3,4,1,3]`
- **Output:** `2`
- **Explanation:** If we flip the second card, the face up numbers are [1,3,4,4,7] and the face down are [1,2,4,1,3].
2 is the minimum good integer as it appears facing down but not facing up.
It can be shown that 2 is the minimum possible good integer obtainable after flipping some cards.

### Example 2
- **Input:** `fronts = [1], backs = [1]`
- **Output:** `0`
- **Explanation:** There are no good integers no matter how we flip the cards, so we return 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Card Flipping Game**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `fronts = [1,2,4,4,7], backs = [1,3,4,1,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** If we flip the second card, the face up numbers are [1,3,4,4,7] and the face down are [1,2,4,1,3].
2 is the minimum good integer as it appears facing down but not facing up.
It can be shown that 2 is the minimum possible good integer obtainable after flipping some cards.

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
from itertools import chain
from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        banned = {f for f, b in zip(fronts, backs) if f == b}
        return min((x for x in chain(fronts, backs) if x not in banned), default=0)
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
- [3664. Two-Letter Card Game](../../3501-4000/3664-two-letter-card-game/)
- [45. Jump Game II](../../0001-0500/0045-jump-game-ii/)
- [55. Jump Game](../../0001-0500/0055-jump-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/card-flipping-game/)
