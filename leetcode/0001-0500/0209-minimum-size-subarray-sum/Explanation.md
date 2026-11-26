# LeetCode 209: Minimum Size Subarray Sum

**LeetCode Problem #209 — Minimum Size Subarray Sum**
Solve LeetCode Minimum Size Subarray Sum using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Size Subarray Sum |
| LeetCode | #209 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a * *subarray* * whose sum is greater than or equal to* `target`. If there is no such subarray, return `0` instead.

## Constraints
- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `target = 7, nums = [2,3,1,2,4,3]`
- **Output:** `2`
- **Explanation:** The subarray [4,3] has the minimal length under the problem constraint.

### Example 2
- **Input:** `target = 4, nums = [1,4,4]`
- **Output:** `1`

### Example 3
- **Input:** `target = 11, nums = [1,1,1,1,1,1,1,1]`
- **Output:** `0`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Minimum Size Subarray Sum**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = 7, nums = [2,3,1,2,4,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The subarray [4,3] has the minimal length under the problem constraint.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minSubArrayLen = function(target, nums) {
    let left = 0;
    let sum = 0;
    let minLength = Infinity;

    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];

        while (sum >= target) {
            minLength = Math.min(minLength, right - left + 1);
            sum -= nums[left];
            left++;
        }
    }

    return minLength === Infinity ? 0 : minLength;
};
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
- [2875. Minimum Size Subarray in Infinite Array](../../2501-3000/2875-minimum-size-subarray-in-infinite-array/)
- [3364. Minimum Positive Sum Subarray ](../../3001-3500/3364-minimum-positive-sum-subarray/)
- [3795. Minimum Subarray Length With Distinct Sum At Least K](../../3501-4000/3795-minimum-subarray-length-with-distinct-sum-at-least-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)
