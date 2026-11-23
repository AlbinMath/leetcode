# LeetCode 2400: Number of Ways to Reach a Position After Exactly k Steps

**LeetCode Problem #2400 — Number of Ways to Reach a Position After Exactly k Steps**
Solve LeetCode Number of Ways to Reach a Position After Exactly k Steps using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways to Reach a Position After Exactly k Steps |
| LeetCode | #2400 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **positive** integers `startPos` and `endPos`. Initially, you are standing at position `startPos` on an **infinite** number line. With one step, you can move either one position to the left, or one position to the right.

Given a positive integer `k`, return *the number of **different** ways to reach the position *`endPos`* starting from *`startPos`*, such that you perform **exactly** *`k`* steps*. Since the answer may be very large, return it **modulo** `10^9 + 7`.

Two ways are considered different if the order of the steps made is not exactly the same.

**Note** that the number line includes negative integers.

## Constraints
- `1 <= startPos, endPos, k <= 1000`

## Examples
### Example 1
- **Input:** `startPos = 1, endPos = 2, k = 3`
- **Output:** `3`
- **Explanation:** We can reach position 2 from 1 in exactly 3 steps in three ways:
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
It can be proven that no other way is possible, so we return 3.

### Example 2
- **Input:** `startPos = 2, endPos = 5, k = 10`
- **Output:** `0`
- **Explanation:** It is impossible to reach position 5 from position 2 in exactly 10 steps.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Ways to Reach a Position After Exactly k Steps**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `startPos = 1, endPos = 2, k = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can reach position 2 from 1 in exactly 3 steps in three ways:
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
It can be proven that no other way is possible, so we return 3.

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
var numberOfWays = function(startPos, endPos, k) {
    const MOD = 1000000007n;
    const distance = endPos - startPos;

    if (Math.abs(distance) > k || (k + distance) % 2 !== 0) {
        return 0;
    }

    const right = (k + distance) / 2;
    const left = k - right;

    let result = 1n;

    for (let i = 1; i <= Math.min(right, left); i++) {
        result = result * BigInt(k - i + 1) / BigInt(i);
    }

    return Number(result % MOD);
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
- [3154. Find Number of Ways to Reach the K-th Stair](../../3001-3500/3414-find-number-of-ways-to-reach-the-k-th-stair/)
- [1866. Number of Ways to Rearrange Sticks With K Sticks Visible](../../1501-2000/1996-number-of-ways-to-rearrange-sticks-with-k-sticks-visible/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2229-maximum-fruits-harvested-after-at-most-k-steps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/)
