# LeetCode 1800: Maximum Ascending Subarray Sum

**LeetCode Problem #1800 — Maximum Ascending Subarray Sum**
Solve LeetCode Maximum Ascending Subarray Sum using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Ascending Subarray Sum |
| LeetCode | #1800 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of positive integers `nums`, return the **maximum** possible sum of an strictly increasing subarray in* *`nums`.

A subarray is defined as a contiguous sequence of numbers in an array.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [10,20,30,5,10,50]`
- **Output:** `65`
- **Explanation:** [5,10,50] is the ascending subarray with the maximum sum of 65.

### Example 2
- **Input:** `nums = [10,20,30,40,50]`
- **Output:** `150`
- **Explanation:** [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

### Example 3
- **Input:** `nums = [12,17,15,13,10,11,12]`
- **Output:** `33`
- **Explanation:** [10,11,12] is the ascending subarray with the maximum sum of 33.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Maximum Ascending Subarray Sum**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,20,30,5,10,50]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `65`.
4. **Verification:** [5,10,50] is the ascending subarray with the maximum sum of 65.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int currentSum = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i - 1]) {
                currentSum += nums[i];
            } else {
                currentSum = nums[i];
            }

            maxSum = max(maxSum, currentSum);
        }

        return maxSum;
    }
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
- [918. Maximum Sum Circular Subarray](../../0501-1000/0918-maximum-sum-circular-subarray/)
- [2841. Maximum Sum of Almost Unique Subarray](../../2501-3000/2841-maximum-sum-of-almost-unique-subarray/)
- [3026. Maximum Good Subarray Sum](../../3001-3500/3026-maximum-good-subarray-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-ascending-subarray-sum/)
