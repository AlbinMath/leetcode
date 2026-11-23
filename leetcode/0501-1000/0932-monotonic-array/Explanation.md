# LeetCode 896: Monotonic Array

**LeetCode Problem #896 — Monotonic Array**
Solve LeetCode Monotonic Array using Python and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Monotonic Array |
| LeetCode | #896 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
An array is **monotonic** if it is either monotone increasing or monotone decreasing.

An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array `nums`, return `true`* if the given array is monotonic, or *`false`* otherwise*.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,3]`
- **Output:** `true`

### Example 2
- **Input:** `nums = [6,5,4,4]`
- **Output:** `true`

### Example 3
- **Input:** `nums = [1,3,2]`
- **Output:** `false`

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
To solve **Monotonic Array**, we observe the problem requirements and utilize the **Monotonic Stack** technique. We maintain a **Stack** with elements in strictly monotonic order. Whenever an incoming element violates monotonicity, we pop previous elements and compute answer intervals in amortized linear time.

## Algorithm
1. Initialize an empty stack.
2. For each element, pop previous items from stack while monotonic invariant is violated.
3. Push current element or index onto stack.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,3]`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increasing = False

            if nums[i] > nums[i - 1]:
                decreasing = False

        return increasing or decreasing
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
- [3250. Find the Count of Monotonic Pairs I](../../3501-4000/3535-find-the-count-of-monotonic-pairs-i/)
- [3251. Find the Count of Monotonic Pairs II](../../3501-4000/3536-find-the-count-of-monotonic-pairs-ii/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/monotonic-array/)
