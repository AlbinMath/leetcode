# LeetCode 2294: Partition Array Such That Maximum Difference Is K

**LeetCode Problem #2294 — Partition Array Such That Maximum Difference Is K**
Solve LeetCode Partition Array Such That Maximum Difference Is K using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array Such That Maximum Difference Is K |
| LeetCode | #2294 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `k`. You may partition `nums` into one or more **subsequences** such that each element in `nums` appears in **exactly** one of the subsequences.

Return *the **minimum **number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is **at most** *`k`*.*

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`
- `0 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [3,6,1,2,5], k = 2`
- **Output:** `2`
- **Explanation:** We can partition nums into the two subsequences [3,1,2] and [6,5].
The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
Since two subsequences were created, we return 2. It can be shown that 2 is the minimum number of subsequences needed.

### Example 2
- **Input:** `nums = [1,2,3], k = 1`
- **Output:** `2`
- **Explanation:** We can partition nums into the two subsequences [1,2] and [3].
The difference between the maximum and minimum value in the first subsequence is 2 - 1 = 1.
The difference between the maximum and minimum value in the second subsequence is 3 - 3 = 0.
Since two subsequences were created, we return 2. Note that another optimal solution is to partition nums into the two subsequences [1] and [2,3].

### Example 3
- **Input:** `nums = [2,2,4,5], k = 0`
- **Output:** `3`
- **Explanation:** We can partition nums into the three subsequences [2,2], [4], and [5].
The difference between the maximum and minimum value in the first subsequences is 2 - 2 = 0.
The difference between the maximum and minimum value in the second subsequences is 4 - 4 = 0.
The difference between the maximum and minimum value in the third subsequences is 5 - 5 = 0.
Since three subsequences were created, we return 3. It can be shown that 3 is the minimum number of subsequences needed.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Partition Array Such That Maximum Difference Is K**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,6,1,2,5], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can partition nums into the two subsequences [3,1,2] and [6,5].
The difference between the maximum and minimum value in the first subsequence is 3 - 1 = 2.
The difference between the maximum and minimum value in the second subsequence is 6 - 5 = 1.
Since two subsequences were created, we return 2. It can be shown that 2 is the minimum number of subsequences needed.

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
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        groups = 1
        start = nums[0]
        for x in nums:
            if x - start > k:
                groups += 1
                start = x
        return groups
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
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
- [3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K](../../3001-3500/3007-maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/)
- [3659. Partition Array Into K-Distinct Groups](../../3501-4000/3659-partition-array-into-k-distinct-groups/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/)
