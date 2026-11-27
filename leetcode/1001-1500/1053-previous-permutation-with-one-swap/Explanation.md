# LeetCode 1053: Previous Permutation With One Swap

**LeetCode Problem #1053 — Previous Permutation With One Swap**
Solve LeetCode Previous Permutation With One Swap using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Previous Permutation With One Swap |
| LeetCode | #1053 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of positive integers `arr` (not necessarily distinct), return *the * *lexicographically* * largest permutation that is smaller than* `arr`, that can be **made with exactly one swap**. If it cannot be done, then return the same array.

**Note** that a *swap* exchanges the positions of two numbers `arr[i]` and `arr[j]`

## Constraints
- `1 <= arr.length <= 10^4`
- `1 <= arr[i] <= 10^4`

## Examples
### Example 1
- **Input:** `arr = [3,2,1]`
- **Output:** `[3,1,2]`
- **Explanation:** Swapping 2 and 1.

### Example 2
- **Input:** `arr = [1,1,5]`
- **Output:** `[1,1,5]`
- **Explanation:** This is already the smallest permutation.

### Example 3
- **Input:** `arr = [1,9,4,6,7]`
- **Output:** `[1,7,4,6,9]`
- **Explanation:** Swapping 9 and 7.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Previous Permutation With One Swap**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [3,2,1]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,1,2]`.
4. **Verification:** Swapping 2 and 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i < 0:
            return arr
        j = i + 1
        for k in range(i + 1, n):
            if arr[k] < arr[i] and arr[k] > arr[j]:
                j = k
        arr[i], arr[j] = arr[j], arr[i]
        return arr
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1790. Check if One String Swap Can Make Strings Equal](../../1501-2000/1790-check-if-one-string-swap-can-make-strings-equal/)
- [3900. Longest Balanced Substring After One Swap](../../3501-4000/3900-longest-balanced-substring-after-one-swap/)
- [24. Swap Nodes in Pairs](../../0001-0500/0024-swap-nodes-in-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/previous-permutation-with-one-swap/)
