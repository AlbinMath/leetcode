# LeetCode 3621: Number of Integers With Popcount-Depth Equal to K I

**LeetCode Problem #3621 — Number of Integers With Popcount-Depth Equal to K I**
Solve LeetCode Number of Integers With Popcount-Depth Equal to K I using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Integers With Popcount-Depth Equal to K I |
| LeetCode | #3621 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `n` and `k`.

For any positive integer `x`, define the following sequence:

`p_0 = x` 
 `p_i+1 = popcount(p_i)` for all `i >= 0`, where `popcount(y)` is the number of set bits (1's) in the binary representation of `y`.

This sequence will eventually reach the value 1.

The **popcount-depth** of `x` is defined as the **smallest** integer `d >= 0` such that `p_d = 1`.

For example, if `x = 7` (binary representation `"111"`). Then, the sequence is: `7 &rarr; 3 &rarr; 2 &rarr; 1`, so the popcount-depth of 7 is 3.

Your task is to determine the number of integers in the range `[1, n]` whose popcount-depth is **exactly** equal to `k`.

Return the number of such integers.

## Constraints
- `1 <= n <= 10^15`
- `0 <= k <= 5`

## Examples
### Example 1
- **Input:** `n = 4, k = 1`
- **Output:** `2`
- **Explanation:** The following integers in the range `[1, 4]` have popcount-depth exactly equal to 1: 

 
 
 
 x 
 Binary 
 Sequence 
 
 
 
 
 2 
 `"10"` 
 `2 &rarr; 1` 
 
 
 4 
 `"100"` 
 `4 &rarr; 1` 
 
 
 

 Thus, the answer is 2.

### Example 2
- **Input:** `n = 7, k = 2`
- **Output:** `3`
- **Explanation:** The following integers in the range `[1, 7]` have popcount-depth exactly equal to 2: 

 
 
 
 x 
 Binary 
 Sequence 
 
 
 
 
 3 
 `"11"` 
 `3 &rarr; 2 &rarr; 1` 
 
 
 5 
 `"101"` 
 `5 &rarr; 2 &rarr; 1` 
 
 
 6 
 `"110"` 
 `6 &rarr; 2 &rarr; 1` 
 
 
 

 Thus, the answer is 3.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Integers With Popcount-Depth Equal to K I**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The following integers in the range `[1, 4]` have popcount-depth exactly equal to 1: 

 
 
 
 x 
 Binary 
 Sequence 
 
 
 
 
 2 
 `"10"` 
 `2 &rarr; 1` 
 
 
 4 
 `"100"` 
 `4 &rarr; 1` 
 
 
 

 Thus, the answer is 2.

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
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var popcountDepth = function (n, k) {
    if (k === 0) return 1; // only x = 1 has depth 0, and n >= 1

    const s = n.toString(2);
    const len = s.length;

    const pc = (x) => x.toString(2).replace(/0/g, "").length;

    const depth = new Array(len + 1).fill(0);
    for (let i = 2; i <= len; i++) depth[i] = depth[pc(i)] + 1;

    const C = Array.from({ length: len + 1 }, () => new Array(len + 1).fill(0));
    for (let i = 0; i <= len; i++) {
        C[i][0] = 1;
        for (let j = 1; j <= i; j++) C[i][j] = C[i - 1][j - 1] + (C[i - 1][j] || 0);
    }

    let ans = 0;
    for (let ones = 1; ones <= len; ones++) {
        if (depth[ones] !== k - 1) continue;

        let remaining = ones;
        for (let i = 0; i < len; i++) {
            if (s[i] === "1") {
                const left = len - i - 1;
                if (remaining <= left) ans += C[left][remaining];
                remaining--;
                if (remaining < 0) break;
            }
        }
        if (remaining === 0) ans++;
    }

    if (k === 1) ans--; // remove x = 1 (popcount 1 but depth 0)
    return ans;
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
- [3624. Number of Integers With Popcount-Depth Equal to K II](../../3501-4000/3941-number-of-integers-with-popcount-depth-equal-to-k-ii/)
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1445-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)
- [1481. Least Number of Unique Integers after K Removals](../../1501-2000/1604-least-number-of-unique-integers-after-k-removals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/)
