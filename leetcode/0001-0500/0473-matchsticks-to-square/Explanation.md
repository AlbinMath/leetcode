# LeetCode 473: Matchsticks to Square

**LeetCode Problem #473 — Matchsticks to Square**
Solve LeetCode Matchsticks to Square using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Matchsticks to Square |
| LeetCode | #473 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `matchsticks` where `matchsticks[i]` is the length of the `i^th` matchstick. You want to use **all the matchsticks** to make one square. You **should not break** any stick, but you can link them up, and each matchstick must be used **exactly one time**.

Return `true` if you can make this square and `false` otherwise.

## Constraints
- `1 <= matchsticks.length <= 15`
- `1 <= matchsticks[i] <= 10^8`

## Examples
### Example 1
- **Input:** `matchsticks = [1,1,2,2,2]`
- **Output:** `true`
- **Explanation:** You can form a square with length 2, one side of the square came two sticks with length 1.

### Example 2
- **Input:** `matchsticks = [3,3,3,3,4]`
- **Output:** `false`
- **Explanation:** You cannot find a way to form a square with all the matchsticks.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Matchsticks to Square**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `matchsticks = [1,1,2,2,2]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** You can form a square with length 2, one side of the square came two sticks with length 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} matchsticks
 * @return {boolean}
 */
var makesquare = function (matchsticks) {
  const total = matchsticks.reduce((a, b) => a + b, 0);
  if (total % 4 !== 0) return false;

  const side = total / 4;
  matchsticks.sort((a, b) => b - a);
  if (matchsticks[0] > side) return false;

  const sides = [0, 0, 0, 0];
  const n = matchsticks.length;

  const backtrack = (i) => {
    if (i === n) return true;

    const seen = new Set();
    for (let j = 0; j < 4; j++) {
      if (sides[j] + matchsticks[i] > side || seen.has(sides[j])) continue;

      seen.add(sides[j]);
      sides[j] += matchsticks[i];
      if (backtrack(i + 1)) return true;
      sides[j] -= matchsticks[i];
    }
    return false;
  };

  return backtrack(0);
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [221. Maximal Square](../../0001-0500/0221-maximal-square/)
- [367. Valid Perfect Square](../../0001-0500/0367-valid-perfect-square/)
- [593. Valid Square](../../0501-1000/0593-valid-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/matchsticks-to-square/)
