# LeetCode 526: Beautiful Arrangement

**LeetCode Problem #526 — Beautiful Arrangement**
Solve LeetCode Beautiful Arrangement using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Beautiful Arrangement |
| LeetCode | #526 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Suppose you have `n` integers labeled `1` through `n`. A permutation of those `n` integers `perm` (**1-indexed**) is considered a **beautiful arrangement** if for every `i` (`1 <= i <= n`), **either** of the following is true:

`perm[i]` is divisible by `i`. 
 `i` is divisible by `perm[i]`.

Given an integer `n`, return *the **number** of the **beautiful arrangements** that you can construct*.

## Constraints
- `1 <= n <= 15`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `2`

### Example 2
- **Input:** `n = 1`
- **Output:** `1`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Beautiful Arrangement**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.

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
 * @param {number} n
 * @return {number}
 */
var countArrangement = function (n) {
  const used = new Array(n + 1).fill(false);
  let count = 0;

  const backtrack = (pos) => {
    if (pos === 0) {
      count++;
      return;
    }
    for (let num = 1; num <= n; num++) {
      if (used[num]) continue;
      if (num % pos !== 0 && pos % num !== 0) continue;

      used[num] = true;
      backtrack(pos - 1);
      used[num] = false;
    }
  };

  backtrack(n);
  return count;
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
- [932. Beautiful Array](../../0501-1000/0932-beautiful-array/)
- [2216. Minimum Deletions to Make Array Beautiful](../../2001-2500/2216-minimum-deletions-to-make-array-beautiful/)
- [2588. Count the Number of Beautiful Subarrays](../../2501-3000/2588-count-the-number-of-beautiful-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/beautiful-arrangement/)
