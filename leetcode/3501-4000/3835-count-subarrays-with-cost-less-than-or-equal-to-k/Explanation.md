# LeetCode 3835: Count Subarrays With Cost Less Than or Equal to K

**LeetCode Problem #3835 — Count Subarrays With Cost Less Than or Equal to K**
Solve LeetCode Count Subarrays With Cost Less Than or Equal to K using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subarrays With Cost Less Than or Equal to K |
| LeetCode | #3835 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`, and an integer `k`.

For any subarray `nums[l..r]`, define its **cost** as:

`cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1)`.

Return an integer denoting the number of subarrays of `nums` whose cost is **less than or equal** to `k`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^15`

## Examples
### Example 1
- **Input:** `nums = [1,3,2], k = 4`
- **Output:** `5`
- **Explanation:** We consider all subarrays of `nums`: 

 
 `nums[0..0]`: `cost = (1 - 1) * 1 = 0` 
 `nums[0..1]`: `cost = (3 - 1) * 2 = 4` 
 `nums[0..2]`: `cost = (3 - 1) * 3 = 6` 
 `nums[1..1]`: `cost = (3 - 3) * 1 = 0` 
 `nums[1..2]`: `cost = (3 - 2) * 2 = 2` 
 `nums[2..2]`: `cost = (2 - 2) * 1 = 0` 
 

 There are 5 subarrays whose cost is less than or equal to 4.

### Example 2
- **Input:** `nums = [5,5,5,5], k = 0`
- **Output:** `10`
- **Explanation:** For any subarray of `nums`, the maximum and minimum values are the same, so the cost is always 0. 

 As a result, every subarray of `nums` has cost less than or equal to 0. 

 For an array of length 4, the total number of subarrays is `(4 * 5) / 2 = 10`.

### Example 3
- **Input:** `nums = [1,2,3], k = 0`
- **Output:** `3`
- **Explanation:** The only subarrays of `nums` with cost 0 are the single-element subarrays, and there are 3 of them.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Subarrays With Cost Less Than or Equal to K**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2], k = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** We consider all subarrays of `nums`: 

 
 `nums[0..0]`: `cost = (1 - 1) * 1 = 0` 
 `nums[0..1]`: `cost = (3 - 1) * 2 = 4` 
 `nums[0..2]`: `cost = (3 - 1) * 3 = 6` 
 `nums[1..1]`: `cost = (3 - 3) * 1 = 0` 
 `nums[1..2]`: `cost = (3 - 2) * 2 = 2` 
 `nums[2..2]`: `cost = (2 - 2) * 1 = 0` 
 

 There are 5 subarrays whose cost is less than or equal to 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

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
var countSubarrays = function (nums, k) {
    const n = nums.length;
    const maxQ = new Array(n), minQ = new Array(n);
    let maxH = 0, maxT = 0, minH = 0, minT = 0;
    let l = 0, ans = 0;

    for (let r = 0; r < n; r++) {
        while (maxH < maxT && nums[maxQ[maxT - 1]] <= nums[r]) maxT--;
        maxQ[maxT++] = r;
        while (minH < minT && nums[minQ[minT - 1]] >= nums[r]) minT--;
        minQ[minT++] = r;

        while ((nums[maxQ[maxH]] - nums[minQ[minH]]) * (r - l + 1) > k) {
            l++;
            if (maxQ[maxH] < l) maxH++;
            if (minQ[minH] < l) minH++;
        }
        ans += r - l + 1;
    }
    return ans;
};
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
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2302-count-subarrays-with-score-less-than-k/)
- [3352. Count K-Reducible Numbers Less Than N](../../3001-3500/3352-count-k-reducible-numbers-less-than-n/)
- [2311. Longest Binary Subsequence Less Than or Equal to K](../../2001-2500/2311-longest-binary-subsequence-less-than-or-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subarrays-with-cost-less-than-or-equal-to-k/)
