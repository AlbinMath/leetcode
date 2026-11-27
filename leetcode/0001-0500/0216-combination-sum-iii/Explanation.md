# LeetCode 216: Combination Sum III

**LeetCode Problem #216 — Combination Sum III**
Solve LeetCode Combination Sum III using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Combination Sum III |
| LeetCode | #216 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:

Only numbers `1` through `9` are used. 
 Each number is used **at most once**.

Return *a list of all possible valid combinations*. The list must not contain the same combination twice, and the combinations may be returned in any order.

## Constraints
- `2 <= k <= 9`
- `1 <= n <= 60`

## Examples
### Example 1
- **Input:** `k = 3, n = 7`
- **Output:** `[[1,2,4]]`
- **Explanation:** 1 + 2 + 4 = 7
There are no other valid combinations.

### Example 2
- **Input:** `k = 3, n = 9`
- **Output:** `[[1,2,6],[1,3,5],[2,3,4]]`
- **Explanation:** 1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

### Example 3
- **Input:** `k = 4, n = 1`
- **Output:** `[]`
- **Explanation:** There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Combination Sum III**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `k = 3, n = 7`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2,4]]`.
4. **Verification:** 1 + 2 + 4 = 7
There are no other valid combinations.

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
var combinationSum3 = function(k, n) {
    const result = [];
    const path = [];

    function backtrack(start, remaining) {
        if (path.length === k) {
            if (remaining === 0) {
                result.push([...path]);
            }
            return;
        }

        for (let num = start; num <= 9; num++) {
            if (num > remaining) {
                break;
            }

            path.push(num);
            backtrack(num + 1, remaining - num);
            path.pop();
        }
    }

    backtrack(1, n);
    return result;
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
- [39. Combination Sum](../../0001-0500/0039-combination-sum/)
- [40. Combination Sum II](../../0001-0500/0040-combination-sum-ii/)
- [377. Combination Sum IV](../../0001-0500/0377-combination-sum-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/combination-sum-iii/)
