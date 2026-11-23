# LeetCode 941: Valid Mountain Array

**LeetCode Problem #941 — Valid Mountain Array**
Solve LeetCode Valid Mountain Array using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Mountain Array |
| LeetCode | #941 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `arr`, return *`true` if and only if it is a valid mountain array*.

Recall that arr is a mountain array if and only if:

`arr.length >= 3` 
 There exists some `i` with `0 < i < arr.length - 1` such that:
 
 `arr[0] < arr[1] < ... < arr[i - 1] < arr[i] ` 
 `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

## Constraints
- `1 <= arr.length <= 10^4`
- `0 <= arr[i] <= 10^4`

## Examples
### Example 1
- **Input:** `arr = [2,1]`
- **Output:** `false`

### Example 2
- **Input:** `arr = [3,5,5]`
- **Output:** `false`

### Example 3
- **Input:** `arr = [0,3,2,1]`
- **Output:** `true`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Valid Mountain Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [2,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.

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
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0

        # Climb while values are strictly increasing
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak cannot be the first or last element
        if i == 0 or i == n - 1:
            return False

        # Descend while values are strictly decreasing
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [845. Longest Mountain in Array](../../0501-1000/0875-longest-mountain-in-array/)
- [852. Peak Index in a Mountain Array](../../0501-1000/0882-peak-index-in-a-mountain-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-mountain-array/)
