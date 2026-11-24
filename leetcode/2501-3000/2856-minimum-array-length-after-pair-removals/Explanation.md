# LeetCode 2856: Minimum Array Length After Pair Removals

**LeetCode Problem #2856 — Minimum Array Length After Pair Removals**
Solve LeetCode Minimum Array Length After Pair Removals using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Array Length After Pair Removals |
| LeetCode | #2856 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `num` sorted in non-decreasing order.

You can perform the following operation any number of times:

Choose **two** indices, `i` and `j`, where `nums[i] < nums[j]`. 
 Then, remove the elements at indices `i` and `j` from `nums`. The remaining elements retain their original order, and the array is re-indexed.

Return the **minimum** length of `nums` after applying the operation zero or more times.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `nums` is sorted in **non-decreasing** order.

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4]`
- **Output:** `0`

### Example 2
- **Input:** `nums = [1,1,2,2,3,3]`
- **Output:** `0`

### Example 3
- **Input:** `nums = [1000000000,1000000000]`
- **Output:** `2`
- **Explanation:** Since both numbers are equal, they cannot be removed.

### Example 4
- **Input:** `nums = [2,3,4,4,4]`
- **Output:** `1`

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Array Length After Pair Removals**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from bisect import bisect_left, bisect_right

class Solution:
    def minLengthAfterRemovals(self, nums: list[int]) -> int:
        n = len(nums)
        mid_val = nums[n // 2]
        max_freq = bisect_right(nums, mid_val) - bisect_left(nums, mid_val)
        
        if max_freq > n // 2:
            return 2 * max_freq - n
            
        return n % 2
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3746. Minimum String Length After Balanced Removals](../../3501-4000/3746-minimum-string-length-after-balanced-removals/)
- [3507. Minimum Pair Removal to Sort Array I](../../3501-4000/3507-minimum-pair-removal-to-sort-array-i/)
- [3510. Minimum Pair Removal to Sort Array II](../../3501-4000/3510-minimum-pair-removal-to-sort-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-array-length-after-pair-removals/)
