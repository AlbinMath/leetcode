# LeetCode 915: Partition Array into Disjoint Intervals

**LeetCode Problem #915 — Partition Array into Disjoint Intervals**
Solve LeetCode Partition Array into Disjoint Intervals using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array into Disjoint Intervals |
| LeetCode | #915 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `nums`, partition it into two (contiguous) subarrays `left` and `right` so that:

Every element in `left` is less than or equal to every element in `right`. 
 `left` and `right` are non-empty. 
 `left` has the smallest possible size.

Return *the length of *`left`* after such a partitioning*.

Test cases are generated such that partitioning exists.

## Constraints
- `2 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^6`
- There is at least one valid answer for the given input.

## Examples
### Example 1
- **Input:** `nums = [5,0,3,8,6]`
- **Output:** `3`
- **Explanation:** left = [5,0,3], right = [8,6]

### Example 2
- **Input:** `nums = [1,1,1,0,6,12]`
- **Output:** `4`
- **Explanation:** left = [1,1,1,0], right = [6,12]

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Partition Array into Disjoint Intervals**, we observe the problem requirements and utilize the **Greedy** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,0,3,8,6]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** left = [5,0,3], right = [8,6]

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        partition_idx = 0
        left_max = nums[0]
        curr_max = nums[0]
        
        for i in range(1, len(nums)):
            curr_max = max(curr_max, nums[i])
            if nums[i] < left_max:
                partition_idx = i
                left_max = curr_max
                
        return partition_idx + 1
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1013. Partition Array Into Three Parts With Equal Sum](../../1001-1500/1013-partition-array-into-three-parts-with-equal-sum/)
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2035-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [3566. Partition Array into Two Equal Product Subsets](../../3501-4000/3566-partition-array-into-two-equal-product-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-into-disjoint-intervals/)
