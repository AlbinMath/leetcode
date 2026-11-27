# LeetCode 1537: Get the Maximum Score

**LeetCode Problem #1537 — Get the Maximum Score**
Solve LeetCode Get the Maximum Score using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Get the Maximum Score |
| LeetCode | #1537 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **sorted** arrays of distinct integers `nums1` and `nums2`.

A **valid * ***path is defined as follows:

Choose array `nums1` or `nums2` to traverse (from index-0). 
 Traverse the current array from left to right. 
 If you are reading any value that is present in `nums1` and `nums2` you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).

The **score** is defined as the sum of unique values in a valid path.

Return *the maximum score you can obtain of all possible **valid paths***. Since the answer may be too large, return it modulo `10^9 + 7`.

## Constraints
- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^7`
- `nums1` and `nums2` are strictly increasing.

## Examples
### Example 1
- **Input:** `nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]`
- **Output:** `30`
- **Explanation:** Valid paths:
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10], (starting from nums1)
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10] (starting from nums2)
The maximum is obtained with the path in green

### Example 2
- **Input:** `nums1 = [1,3,5,7,9], nums2 = [3,5,100]`
- **Output:** `109`
- **Explanation:** Maximum sum is obtained with the path

### Example 3
- **Input:** `nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]`
- **Output:** `40`
- **Explanation:** There are no common elements between nums1 and nums2.
Maximum sum is obtained with the path [6,7,8,9,10].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Get the Maximum Score**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `30`.
4. **Verification:** Valid paths:
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10], (starting from nums1)
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10] (starting from nums2)
The maximum is obtained with the path in green

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
from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        i = j = 0
        n, m = len(nums1), len(nums2)
        s1 = s2 = 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                s1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                s2 += nums2[j]
                j += 1
            else:
                best = max(s1, s2) + nums1[i]
                s1 = s2 = best
                i += 1
                j += 1
        while i < n:
            s1 += nums1[i]
            i += 1
        while j < m:
            s2 += nums2[j]
            j += 1
        return max(s1, s2) % MOD
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
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)
- [1561. Maximum Number of Coins You Can Get](../../1501-2000/1561-maximum-number-of-coins-you-can-get/)
- [1646. Get Maximum in Generated Array](../../1501-2000/1646-get-maximum-in-generated-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/get-the-maximum-score/)
