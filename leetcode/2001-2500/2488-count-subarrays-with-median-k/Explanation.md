# LeetCode 2488: Count Subarrays With Median K

**LeetCode Problem #2488 — Count Subarrays With Median K**
Solve LeetCode Count Subarrays With Median K using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subarrays With Median K |
| LeetCode | #2488 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` of size `n` consisting of **distinct **integers from `1` to `n` and a positive integer `k`.

Return *the number of non-empty subarrays in *`nums`* that have a **median** equal to *`k`.

**Note**:

The median of an array is the **middle **element after sorting the array in **ascending **order. If the array is of even length, the median is the **left **middle element.

For example, the median of `[2,3,1,4]` is `2`, and the median of `[8,4,3,5,1]` is `4`. 
 
 
 A subarray is a contiguous part of an array.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i], k <= n`
- The integers in `nums` are distinct.

## Examples
### Example 1
- **Input:** `nums = [3,2,1,4,5], k = 4`
- **Output:** `3`
- **Explanation:** The subarrays that have a median equal to 4 are: [4], [4,5] and [1,4,5].

### Example 2
- **Input:** `nums = [2,3,1], k = 3`
- **Output:** `1`
- **Explanation:** [3] is the only subarray that has a median equal to 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Subarrays With Median K**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,2,1,4,5], k = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The subarrays that have a median equal to 4 are: [4], [4,5] and [1,4,5].

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
var countSubarrays = function(nums, k) {
    const n = nums.length;
    const pos = nums.indexOf(k);
    let count = new Map();
    count.set(0, 1);
    let balance = 0;
    for (let i = pos + 1; i < n; i++) {
        if (nums[i] > k) {
            balance++;
        } else {
            balance--;
        }
        count.set(balance, (count.get(balance) || 0) + 1);
    }
    let ans = 0;
    balance = 0;
    for (let i = pos; i >= 0; i--) {
        if (i < pos) {
            if (nums[i] > k) {
                balance++;
            } else {
                balance--;
            }
        }
        ans += count.get(-balance) || 0;
        ans += count.get(1 - balance) || 0;
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
- [2962. Count Subarrays Where Max Element Appears at Least K Times](../../2501-3000/2962-count-subarrays-where-max-element-appears-at-least-k-times/)
- [3420. Count Non-Decreasing Subarrays After K Operations](../../3001-3500/3420-count-non-decreasing-subarrays-after-k-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subarrays-with-median-k/)
