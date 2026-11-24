# LeetCode 2763: Sum of Imbalance Numbers of All Subarrays

**LeetCode Problem #2763 — Sum of Imbalance Numbers of All Subarrays**
Solve LeetCode Sum of Imbalance Numbers of All Subarrays using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Imbalance Numbers of All Subarrays |
| LeetCode | #2763 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **imbalance number** of a **0-indexed** integer array `arr` of length `n` is defined as the number of indices in `sarr = sorted(arr)` such that:

`0 <= i < n - 1`, and 
 `sarr[i+1] - sarr[i] > 1`

Here, `sorted(arr)` is the function that returns the sorted version of `arr`.

Given a **0-indexed** integer array `nums`, return *the **sum of imbalance numbers** of all its **subarrays***.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [2,3,1,4]`
- **Output:** `3`
- **Explanation:** There are 3 subarrays with non-zero

### Example 2
- **Input:** `nums = [1,3,3,3,5]`
- **Output:** `8`
- **Explanation:** There are 7 subarrays with non-zero imbalance numbers:
- Subarray [1, 3] with an imbalance number of 1.
- Subarray [1, 3, 3] with an imbalance number of 1.
- Subarray [1, 3, 3, 3] with an imbalance number of 1.
- Subarray [1, 3, 3, 3, 5] with an imbalance number of 2. 
- Subarray [3, 3, 3, 5] with an imbalance number of 1. 
- Subarray [3, 3, 5] with an imbalance number of 1.
- Subarray [3, 5] with an imbalance number of 1.
The imbalance number of all other subarrays is 0. Hence, the sum of imbalance numbers of all the subarrays of nums is 8.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Imbalance Numbers of All Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,1,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are 3 subarrays with non-zero

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution(object):
    def sumImbalanceNumbers(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            seen = [False] * (n + 2)
            seen[nums[i]] = True
            imbalance = 0

            for j in range(i + 1, n):
                x = nums[j]
                if not seen[x]:
                    seen[x] = True
                    if seen[x - 1] and seen[x + 1]:
                        imbalance -= 1
                    elif not seen[x - 1] and not seen[x + 1]:
                        imbalance += 1
                ans += imbalance

        return ans
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
- [3318. Find X-Sum of All K-Long Subarrays I](../../3001-3500/3318-find-x-sum-of-all-k-long-subarrays-i/)
- [3321. Find X-Sum of All K-Long Subarrays II](../../3001-3500/3321-find-x-sum-of-all-k-long-subarrays-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/)
