# LeetCode 3427: Sum of Variable Length Subarrays

**LeetCode Problem #3427 — Sum of Variable Length Subarrays**
Solve LeetCode Sum of Variable Length Subarrays using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Variable Length Subarrays |
| LeetCode | #3427 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of size `n`. For **each** index `i` where `0 <= i < n`, define a subarray `nums[start ... i]` where `start = max(0, i - nums[i])`.

Return the total sum of all elements from the subarray defined for each index in the array.

## Constraints
- `1 <= n == nums.length <= 100`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [2,3,1]`
- **Output:** `11`
- **Explanation:** i 
 Subarray 
 Sum 
 
 
 0 
 `nums[0] = [2]` 
 2 
 
 
 1 
 `nums[0 ... 1] = [2, 3]` 
 5 
 
 
 2 
 `nums[1 ... 2] = [3, 1]` 
 4

### Example 2
- **Input:** `nums = [3,1,1,2]`
- **Output:** `13`
- **Explanation:** i 
 Subarray 
 Sum 
 
 
 0 
 `nums[0] = [3]` 
 3 
 
 
 1 
 `nums[0 ... 1] = [3, 1]` 
 4 
 
 
 2 
 `nums[1 ... 2] = [1, 1]` 
 2 
 
 
 3 
 `nums[1 ... 3] = [1, 1, 2]` 
 4

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Variable Length Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `11`.
4. **Verification:** i 
 Subarray 
 Sum 
 
 
 0 
 `nums[0] = [2]` 
 2 
 
 
 1 
 `nums[0 ... 1] = [2, 3]` 
 5 
 
 
 2 
 `nums[1 ... 2] = [3, 1]` 
 4

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
var subarraySum = function(nums) {
    const n = nums.length;
    const prefix = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + nums[i];
    }

    let ans = 0;

    for (let i = 0; i < n; i++) {
        const start = Math.max(0, i - nums[i]);
        const sum = prefix[i + 1] - prefix[start];

        ans += sum;
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
- [1588. Sum of All Odd Length Subarrays](../../1501-2000/1588-sum-of-all-odd-length-subarrays/)
- [2461. Maximum Sum of Distinct Subarrays With Length K](../../2001-2500/2461-maximum-sum-of-distinct-subarrays-with-length-k/)
- [3473. Sum of K Subarrays With Length at Least M](../../3001-3500/3473-sum-of-k-subarrays-with-length-at-least-m/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-variable-length-subarrays/)
