# LeetCode 3420: Count Non-Decreasing Subarrays After K Operations

**LeetCode Problem #3420 — Count Non-Decreasing Subarrays After K Operations**
Solve LeetCode Count Non-Decreasing Subarrays After K Operations using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Non-Decreasing Subarrays After K Operations |
| LeetCode | #3420 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` of `n` integers and an integer `k`.

For each subarray of `nums`, you can apply **up to** `k` operations on it. In each operation, you increment any element of the subarray by 1.

**Note** that each subarray is considered independently, meaning changes made to one subarray do not persist to another.

Return the number of subarrays that you can make **non-decreasing** ​​​​​after performing at most `k` operations.

An array is said to be **non-decreasing** if each element is greater than or equal to its previous element, if it exists.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [6,3,1,2,4,4], k = 7`
- **Output:** `17`
- **Explanation:** Out of all 21 possible subarrays of `nums`, only the subarrays `[6, 3, 1]`, `[6, 3, 1, 2]`, `[6, 3, 1, 2, 4]` and `[6, 3, 1, 2, 4, 4]` cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is `21 - 4 = 17`.

### Example 2
- **Input:** `nums = [6,3,1,3,6], k = 4`
- **Output:** `12`
- **Explanation:** The subarray `[3, 1, 3, 6]` along with all subarrays of `nums` with three or fewer elements, except `[6, 3, 1]`, can be made non-decreasing after `k` operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except `[6, 3, 1]`, so there are `1 + 5 + 4 + 2 = 12` subarrays that can be made non-decreasing.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Non-Decreasing Subarrays After K Operations**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [6,3,1,2,4,4], k = 7`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `17`.
4. **Verification:** Out of all 21 possible subarrays of `nums`, only the subarrays `[6, 3, 1]`, `[6, 3, 1, 2]`, `[6, 3, 1, 2, 4]` and `[6, 3, 1, 2, 4, 4]` cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is `21 - 4 = 17`.

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
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countNonDecreasingSubarrays = function (nums, k) {
    const n = nums.length;
    const pre = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pre[i + 1] = pre[i] + nums[i];

    const st = new Array(n); // chain stack: top (smallest index) is st[sz-1], bottom is st[bot]
    let bot = 0, sz = 0;
    let total = 0;          // sum of nums[c] * segment length
    let r = n - 1;
    let ans = 0;

    for (let l = n - 1; l >= 0; l--) {
        // pop chain elements that l now dominates
        while (sz > bot && nums[st[sz - 1]] <= nums[l]) {
            const c = st[sz - 1];
            const end = (sz - 1 > bot) ? st[sz - 2] : r + 1; // exclusive end of c's segment
            total -= nums[c] * (end - c);
            sz--;
        }
        // push l; its segment ends before the next chain element (or at r)
        const end = (sz > bot) ? st[sz - 1] : r + 1;
        total += nums[l] * (end - l);
        st[sz++] = l;

        // shrink r while cost exceeds k
        while (total - (pre[r + 1] - pre[l]) > k) {
            const c = st[bot];
            total -= nums[c];
            if (c === r) bot++;
            r--;
        }
        ans += r - l + 1;
    }
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
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2302-count-subarrays-with-score-less-than-k/)
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2001-2500/2442-count-number-of-distinct-integers-after-reverse-operations/)
- [2960. Count Tested Devices After Test Operations](../../2501-3000/2960-count-tested-devices-after-test-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/)
