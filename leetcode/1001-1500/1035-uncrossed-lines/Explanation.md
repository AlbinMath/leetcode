# LeetCode 1035: Uncrossed Lines

**LeetCode Problem #1035 — Uncrossed Lines**
Solve LeetCode Uncrossed Lines using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Uncrossed Lines |
| LeetCode | #1035 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2`. We write the integers of `nums1` and `nums2` (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers `nums1[i]` and `nums2[j]` such that:

`nums1[i] == nums2[j]`, and 
 the line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return *the maximum number of connecting lines we can draw in this way*.

## Constraints
- `1 <= nums1.length, nums2.length <= 500`
- `1 <= nums1[i], nums2[j] <= 2000`

## Examples
### Example 1
- **Input:** `nums1 = [1,4,2], nums2 = [1,2,4]`
- **Output:** `2`
- **Explanation:** We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

### Example 2
- **Input:** `nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]`
- **Output:** `3`

### Example 3
- **Input:** `nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]`
- **Output:** `2`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Uncrossed Lines**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,4,2], nums2 = [1,2,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            
        n = len(nums2)
        dp = [0] * (n + 1)
        
        for num1 in nums1:
            prev_diag = 0
            for j, num2 in enumerate(nums2, start=1):
                temp = dp[j]
                if num1 == num2:
                    dp[j] = prev_diag + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diag = temp
                
        return dp[n]
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
- [806. Number of Lines To Write String](../../0501-1000/0806-number-of-lines-to-write-string/)
- [2280. Minimum Lines to Represent a Line Chart](../../2001-2500/2280-minimum-lines-to-represent-a-line-chart/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/uncrossed-lines/)
