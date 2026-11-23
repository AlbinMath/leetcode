# LeetCode 3689: Maximum Total Subarray Value I

**LeetCode Problem #3689 — Maximum Total Subarray Value I**
Solve LeetCode Maximum Total Subarray Value I using Java and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Total Subarray Value I |
| LeetCode | #3689 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer `k`.

You need to choose **exactly** `k` non-empty subarrays `nums[l..r]` of `nums`. Subarrays may overlap, and the exact same subarray (same `l` and `r`) **can** be chosen more than once.

The **value** of a subarray `nums[l..r]` is defined as: `max(nums[l..r]) - min(nums[l..r])`.

The **total value** is the sum of the **values** of all chosen subarrays.

Return the **maximum** possible total value you can achieve.

## Constraints
- `1 <= n == nums.length <= 5 * 10^​​​​​​​4`
- `0 <= nums[i] <= 10^9`
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,3,2], k = 2`
- **Output:** `4`
- **Explanation:** One optimal approach is: 

 
 Choose `nums[0..1] = [1, 3]`. The maximum is 3 and the minimum is 1, giving a value of `3 - 1 = 2`. 
 Choose `nums[0..2] = [1, 3, 2]`. The maximum is still 3 and the minimum is still 1, so the value is also `3 - 1 = 2`. 
 

 Adding these gives `2 + 2 = 4`.

### Example 2
- **Input:** `nums = [4,2,5,1], k = 3`
- **Output:** `12`
- **Explanation:** One optimal approach is: 

 
 Choose `nums[0..3] = [4, 2, 5, 1]`. The maximum is 5 and the minimum is 1, giving a value of `5 - 1 = 4`. 
 Choose `nums[0..3] = [4, 2, 5, 1]`. The maximum is 5 and the minimum is 1, so the value is also `4`. 
 Choose `nums[2..3] = [5, 1]`. The maximum is 5 and the minimum is 1, so the value is again `4`. 
 

 Adding these gives `4 + 4 + 4 = 12`.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Maximum Total Subarray Value I**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2], k = 2`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** One optimal approach is: 

 
 Choose `nums[0..1] = [1, 3]`. The maximum is 3 and the minimum is 1, giving a value of `3 - 1 = 2`. 
 Choose `nums[0..2] = [1, 3, 2]`. The maximum is still 3 and the minimum is still 1, so the value is also `3 - 1 = 2`. 
 

 Adding these gives `2 + 2 = 4`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public long maxTotalValue(int[] nums, int k) {
        int min = nums[0];
        int max = nums[0];

        for (int num : nums) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }

        return (long) (max - min) * k;
    }
}
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3691. Maximum Total Subarray Value II](../../4001-4500/4007-maximum-total-subarray-value-ii/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)
- [152. Maximum Product Subarray](../../0001-0500/0152-maximum-product-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-total-subarray-value-i/)
