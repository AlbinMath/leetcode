# LeetCode 873: Length of Longest Fibonacci Subsequence

**LeetCode Problem #873 — Length of Longest Fibonacci Subsequence**
Solve LeetCode Length of Longest Fibonacci Subsequence using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Length of Longest Fibonacci Subsequence |
| LeetCode | #873 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A sequence `x_1, x_2, ..., x_n` is *Fibonacci-like* if:

`n >= 3` 
 `x_i + x_i+1 == x_i+2` for all `i + 2 <= n`

Given a strictly increasing array `arr` of positive integers forming a sequence, return *the **length** of the longest Fibonacci-like subsequence of* `arr`. If one does not exist, return `0`.

A **subsequence** is derived from another sequence `arr` by deleting any number of elements (including none) from `arr`, without changing the order of the remaining elements. For example, `[3, 5, 8]` is a subsequence of `[3, 4, 5, 6, 7, 8]`.

## Constraints
- `3 <= arr.length <= 1000`
- `1 <= arr[i] < arr[i + 1] <= 10^9`

## Examples
### Example 1
- **Input:** `arr = [1,2,3,4,5,6,7,8]`
- **Output:** `5`
- **Explanation:** The longest subsequence that is fibonacci-like: [1,2,3,5,8].

### Example 2
- **Input:** `arr = [1,3,7,11,12,14,18]`
- **Output:** `3`
- **Explanation:** :

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Length of Longest Fibonacci Subsequence**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,3,4,5,6,7,8]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The longest subsequence that is fibonacci-like: [1,2,3,5,8].

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
from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        max_len = 0
        
        for k in range(2, n):
            left, right = 0, k - 1
            target = arr[k]
            while left < right:
                pair_sum = arr[left] + arr[right]
                if pair_sum < target:
                    left += 1
                elif pair_sum > target:
                    right -= 1
                else:
                    dp[right][k] = dp[left][right] + 1
                    if dp[right][k] > max_len:
                        max_len = dp[right][k]
                    left += 1
                    right -= 1
                    
        return max_len
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
- [300. Longest Increasing Subsequence](../../0001-0500/0300-longest-increasing-subsequence/)
- [516. Longest Palindromic Subsequence](../../0501-1000/0516-longest-palindromic-subsequence/)
- [521. Longest Uncommon Subsequence I](../../0501-1000/0521-longest-uncommon-subsequence-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/)
