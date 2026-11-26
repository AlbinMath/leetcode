# LeetCode 2100: Find Good Days to Rob the Bank

**LeetCode Problem #2100 — Find Good Days to Rob the Bank**
Solve LeetCode Find Good Days to Rob the Bank using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Good Days to Rob the Bank |
| LeetCode | #2100 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You and a gang of thieves are planning on robbing a bank. You are given a **0-indexed** integer array `security`, where `security[i]` is the number of guards on duty on the `i^th` day. The days are numbered starting from `0`. You are also given an integer `time`.

The `i^th` day is a good day to rob the bank if:

There are at least `time` days before and after the `i^th` day, 
 The number of guards at the bank for the `time` days **before** `i` are **non-increasing**, and 
 The number of guards at the bank for the `time` days **after** `i` are **non-decreasing**.

More formally, this means day `i` is a good day to rob the bank if and only if `security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time]`.

Return *a list of **all** days **(0-indexed) **that are good days to rob the bank*.* The order that the days are returned in does** ****not** matter.*

## Constraints
- `1 <= security.length <= 10^5`
- `0 <= security[i], time <= 10^5`

## Examples
### Example 1
- **Input:** `security = [5,3,3,3,5,6,2], time = 2`
- **Output:** `[2,3]`
- **Explanation:** On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= security[4].
On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= security[5].
No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.

### Example 2
- **Input:** `security = [1,1,1,1,1], time = 0`
- **Output:** `[0,1,2,3,4]`
- **Explanation:** Since time equals 0, every day is a good day to rob the bank, so return every day.

### Example 3
- **Input:** `security = [1,2,3,4,5,6], time = 2`
- **Output:** `[]`
- **Explanation:** No day has 2 days before it that have a non-increasing number of guards.
Thus, no day is a good day to rob the bank, so return an empty list.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Good Days to Rob the Bank**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `security = [5,3,3,3,5,6,2], time = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3]`.
4. **Verification:** On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= security[4].
On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= security[5].
No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var goodDaysToRobBank = function(security, time) {
    const n = security.length;

    const left = new Array(n).fill(0);
    const right = new Array(n).fill(0);
    for (let i = 1; i < n; i++) {
        if (security[i] <= security[i - 1]) {
            left[i] = left[i - 1] + 1;
        }
    }
    for (let i = n - 2; i >= 0; i--) {
        if (security[i] <= security[i + 1]) {
            right[i] = right[i + 1] + 1;
        }
    }

    const result = [];
    for (let i = time; i < n - time; i++) {
        if (left[i] >= time && right[i] >= time) {
            result.push(i);
        }
    }

    return result;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1397. Find All Good Strings](../../1001-1500/1397-find-all-good-strings/)
- [2420. Find All Good Indices](../../2001-2500/2420-find-all-good-indices/)
- [2732. Find a Good Subset of the Matrix](../../2501-3000/2732-find-a-good-subset-of-the-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-good-days-to-rob-the-bank/)
