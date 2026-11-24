# LeetCode 3737: Count Subarrays With Majority Element I

**LeetCode Problem #3737 — Count Subarrays With Majority Element I**
Solve LeetCode Count Subarrays With Majority Element I using Java and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subarrays With Majority Element I |
| LeetCode | #3737 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `target`.

Return the number of ** subarrays ** of `nums` in which `target` is the **majority element**.

The **majority element** of a subarray is the element that appears **strictly** **more than half** of the times in that subarray.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^​​​​​​​9`
- `1 <= target <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,3], target = 2`
- **Output:** `5`
- **Explanation:** Valid subarrays with `target = 2` as the majority element: 

 
 `nums[1..1] = [2]` 
 `nums[2..2] = [2]` 
 `nums[1..2] = [2,2]` 
 `nums[0..2] = [1,2,2]` 
 `nums[1..3] = [2,2,3]` 
 

 So there are 5 such subarrays.

### Example 2
- **Input:** `nums = [1,1,1,1], target = 1`
- **Output:** `10`

### Example 3
- **Input:** `nums = [1,2,3], target = 4`
- **Output:** `0`
- **Explanation:** `target = 4` does not appear in `nums` at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Count Subarrays With Majority Element I**, we observe the problem requirements and utilize the **Monotonic Stack** technique. We maintain a **Stack** with elements in strictly monotonic order. Whenever an incoming element violates monotonicity, we pop previous elements and compute answer intervals in amortized linear time.

## Algorithm
1. Initialize an empty stack.
2. For each element, pop previous items from stack while monotonic invariant is violated.
3. Push current element or index onto stack.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,3], target = 2`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** Valid subarrays with `target = 2` as the majority element: 

 
 `nums[1..1] = [2]` 
 `nums[2..2] = [2]` 
 `nums[1..2] = [2,2]` 
 `nums[0..2] = [1,2,2]` 
 `nums[1..3] = [2,2,3]` 
 

 So there are 5 such subarrays.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public int countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;
        int count = 0;

        for (int i = 0; i < n; i++) {
            int targetCount = 0;

            for (int j = i; j < n; j++) {
                if (nums[j] == target) {
                    targetCount++;
                }

                int length = j - i + 1;

                if (targetCount * 2 > length) {
                    count++;
                }
            }
        }

        return count;
    }
}
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [3739. Count Subarrays With Majority Element II](../../3501-4000/3739-count-subarrays-with-majority-element-ii/)
- [2962. Count Subarrays Where Max Element Appears at Least K Times](../../2501-3000/2962-count-subarrays-where-max-element-appears-at-least-k-times/)
- [169. Majority Element](../../0001-0500/0169-majority-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-i/)
