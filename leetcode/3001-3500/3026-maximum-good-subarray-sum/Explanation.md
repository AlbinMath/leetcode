# LeetCode 3026: Maximum Good Subarray Sum

**LeetCode Problem #3026 — Maximum Good Subarray Sum**
Solve LeetCode Maximum Good Subarray Sum using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Good Subarray Sum |
| LeetCode | #3026 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` of length `n` and a **positive** integer `k`.

A subarray of `nums` is called **good** if the **absolute difference** between its first and last element is **exactly** `k`, in other words, the subarray `nums[i..j]` is good if `|nums[i] - nums[j]| == k`.

Return *the **maximum** sum of a **good** subarray of *`nums`. *If there are no good subarrays**, return *`0`.

## Constraints
- `2 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5,6], k = 1`
- **Output:** `11`
- **Explanation:** The absolute difference between the first and last element must be 1 for a good subarray. All the good subarrays are: [1,2], [2,3], [3,4], [4,5], and [5,6]. The maximum subarray sum is 11 for the subarray [5,6].

### Example 2
- **Input:** `nums = [-1,3,2,4,5], k = 3`
- **Output:** `11`
- **Explanation:** The absolute difference between the first and last element must be 3 for a good subarray. All the good subarrays are: [-1,3,2], and [2,4,5]. The maximum subarray sum is 11 for the subarray [2,4,5].

### Example 3
- **Input:** `nums = [-1,-2,-3,-4], k = 2`
- **Output:** `-6`
- **Explanation:** The absolute difference between the first and last element must be 2 for a good subarray. All the good subarrays are: [-1,-2,-3], and [-2,-3,-4]. The maximum subarray sum is -6 for the subarray [-1,-2,-3].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Good Subarray Sum**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5,6], k = 1`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `11`.
4. **Verification:** The absolute difference between the first and last element must be 1 for a good subarray. All the good subarrays are: [1,2], [2,3], [3,4], [4,5], and [5,6]. The maximum subarray sum is 11 for the subarray [5,6].

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
var maximumSubarraySum = function(nums, k) {
    const map = new Map();
    let prefixSum = 0;
    let ans = -Infinity;

    for (let num of nums) {
        if (map.has(num - k)) {
            ans = Math.max(
                ans,
                prefixSum + num - map.get(num - k)
            );
        }
        if (map.has(num + k)) {
            ans = Math.max(
                ans,
                prefixSum + num - map.get(num + k)
            );
        }
        if (!map.has(num)) {
            map.set(num, prefixSum);
        } else {
            map.set(num, Math.min(map.get(num), prefixSum));
        }
        prefixSum += num;
    }
    return ans === -Infinity ? 0 : ans;
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
- [918. Maximum Sum Circular Subarray](../../0501-1000/0918-maximum-sum-circular-subarray/)
- [1793. Maximum Score of a Good Subarray](../../1501-2000/1793-maximum-score-of-a-good-subarray/)
- [1800. Maximum Ascending Subarray Sum](../../1501-2000/1800-maximum-ascending-subarray-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-good-subarray-sum/)
