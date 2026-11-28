# LeetCode 805: Split Array With Same Average

**LeetCode Problem #805 — Split Array With Same Average**
Solve LeetCode Split Array With Same Average using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split Array With Same Average |
| LeetCode | #805 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

You should move each element of `nums` into one of the two arrays `A` and `B` such that `A` and `B` are non-empty, and `average(A) == average(B)`.

Return `true` if it is possible to achieve that and `false` otherwise.

**Note** that for an array `arr`, `average(arr)` is the sum of all the elements of `arr` over the length of `arr`.

## Constraints
- `1 <= nums.length <= 30`
- `0 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5,6,7,8]`
- **Output:** `true`
- **Explanation:** We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.

### Example 2
- **Input:** `nums = [3,1]`
- **Output:** `false`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Split Array With Same Average**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5,6,7,8]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var splitArraySameAverage = function (nums) {
  const n = nums.length;
  if (n === 1) return false;

  const S = nums.reduce((a, b) => a + b, 0);
  const half = Math.floor(n / 2);

  let possible = false;
  for (let k = 1; k <= half; k++) {
    if ((S * k) % n === 0) {
      possible = true;
      break;
    }
  }
  if (!possible) return false;

  const dp = Array.from({ length: half + 1 }, () => new Set());
  dp[0].add(0);

  for (const num of nums) {
    for (let k = half; k >= 1; k--) {
      for (const s of dp[k - 1]) {
        dp[k].add(s + num);
      }
    }
  }

  for (let k = 1; k <= half; k++) {
    if ((S * k) % n === 0 && dp[k].has((S * k) / n)) return true;
  }
  return false;
};
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1968. Array With Elements Not Equal to Average of Neighbors](../../1501-2000/1968-array-with-elements-not-equal-to-average-of-neighbors/)
- [1569. Number of Ways to Reorder Array to Get Same BST](../../1501-2000/1569-number-of-ways-to-reorder-array-to-get-same-bst/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-array-with-same-average/)
