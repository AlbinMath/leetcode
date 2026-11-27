# LeetCode 845: Longest Mountain in Array

**LeetCode Problem #845 — Longest Mountain in Array**
Solve LeetCode Longest Mountain in Array using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Mountain in Array |
| LeetCode | #845 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You may recall that an array `arr` is a **mountain array** if and only if:

`arr.length >= 3` 
 There exists some index `i` (**0-indexed**) with `0 < i < arr.length - 1` such that:
 
 `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]` 
 `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given an integer array `arr`, return *the length of the longest subarray, which is a mountain*. Return `0` if there is no mountain subarray.

## Constraints
- `1 <= arr.length <= 10^4`
- `0 <= arr[i] <= 10^4`
- Can you solve it using only one pass?
- Can you solve it in `O(1)` space?

## Examples
### Example 1
- **Input:** `arr = [2,1,4,7,3,2,5]`
- **Output:** `5`
- **Explanation:** The largest mountain is [1,4,7,3,2] which has length 5.

### Example 2
- **Input:** `arr = [2,2,2]`
- **Output:** `0`
- **Explanation:** There is no mountain.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Mountain in Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [2,1,4,7,3,2,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The largest mountain is [1,4,7,3,2] which has length 5.

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
class Solution(object):
    def longestMountain(self, arr):
        n = len(arr)
        longest = 0
        i = 1
        
        while i < n - 1:
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1
                
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                    
                longest = max(longest, right - left + 1)
                i = right
            else:
                i += 1
                
        return longest
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
- [2501. Longest Square Streak in an Array](../../2501-3000/2501-longest-square-streak-in-an-array/)
- [852. Peak Index in a Mountain Array](../../0501-1000/0852-peak-index-in-a-mountain-array/)
- [941. Valid Mountain Array](../../0501-1000/0941-valid-mountain-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-mountain-in-array/)
