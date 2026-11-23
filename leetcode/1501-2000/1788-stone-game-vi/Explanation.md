# LeetCode 1686: Stone Game VI

**LeetCode Problem #1686 — Stone Game VI**
Solve LeetCode Stone Game VI using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game VI |
| LeetCode | #1686 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice and Bob take turns playing a game, with Alice starting first.

There are `n` stones in a pile. On each player's turn, they can **remove** a stone from the pile and receive points based on the stone's value. Alice and Bob may **value the stones differently**.

You are given two integer arrays of length `n`, `aliceValues` and `bobValues`. Each `aliceValues[i]` and `bobValues[i]` represents how Alice and Bob, respectively, value the `i^th` stone.

The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play **optimally**. Both players know the other's values.

Determine the result of the game, and:

If Alice wins, return `1`. 
 If Bob wins, return `-1`. 
 If the game results in a draw, return `0`.

## Constraints
- `n == aliceValues.length == bobValues.length`
- `1 <= n <= 10^5`
- `1 <= aliceValues[i], bobValues[i] <= 100`

## Examples
### Example 1
- **Input:** `aliceValues = [1,3], bobValues = [2,1]`
- **Output:** `1`
- **Explanation:** If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
Bob can only choose stone 0, and will only receive 2 points.
Alice wins.

### Example 2
- **Input:** `aliceValues = [1,2], bobValues = [3,1]`
- **Output:** `0`
- **Explanation:** If Alice takes stone 0, and Bob takes stone 1, they will both have 1 point.
Draw.

### Example 3
- **Input:** `aliceValues = [2,4,3], bobValues = [1,6,7]`
- **Output:** `-1`
- **Explanation:** Regardless of how Alice plays, Bob will be able to have more points than Alice.
For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes stone 0, Alice will have 6 points to Bob's 7.
Bob wins.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Stone Game VI**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `aliceValues = [1,3], bobValues = [2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** If Alice takes stone 1 (0-indexed) first, Alice will receive 3 points.
Bob can only choose stone 0, and will only receive 2 points.
Alice wins.

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
    def stoneGameVI(self, aliceValues, bobValues):
        stones = sorted(range(len(aliceValues)),
                        key=lambda i: aliceValues[i] + bobValues[i],
                        reverse=True)
        score = sum((1 if t % 2 == 0 else -1) *
                    (aliceValues[i] if t % 2 == 0 else bobValues[i])
                    for t, i in enumerate(stones))
        return (score > 0) - (score < 0)
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
- [877. Stone Game](../../0501-1000/0909-stone-game/)
- [1140. Stone Game II](../../1001-1500/1240-stone-game-ii/)
- [1406. Stone Game III](../../1501-2000/1522-stone-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-vi/)
