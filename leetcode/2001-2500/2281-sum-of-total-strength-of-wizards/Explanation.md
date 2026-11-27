# LeetCode 2281: Sum of Total Strength of Wizards

**LeetCode Problem #2281 — Sum of Total Strength of Wizards**
Solve LeetCode Sum of Total Strength of Wizards using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Total Strength of Wizards |
| LeetCode | #2281 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
As the ruler of a kingdom, you have an army of wizards at your command.

You are given a **0-indexed** integer array `strength`, where `strength[i]` denotes the strength of the `i^th` wizard. For a **contiguous** group of wizards (i.e. the wizards' strengths form a **subarray** of `strength`), the **total strength** is defined as the **product** of the following two values:

The strength of the **weakest** wizard in the group. 
 The **total** of all the individual strengths of the wizards in the group.

Return *the **sum** of the total strengths of **all** contiguous groups of wizards*. Since the answer may be very large, return it **modulo** `10^9 + 7`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `1 <= strength.length <= 10^5`
- `1 <= strength[i] <= 10^9`

## Examples
### Example 1
- **Input:** `strength = [1,3,1,2]`
- **Output:** `44`
- **Explanation:** The following are all the contiguous groups of wizards:
- [1] from [

### Example 2
- **Input:** `strength = [5,4,6]`
- **Output:** `213`
- **Explanation:** The following are all the contiguous groups of wizards: 
- [5] from [

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Sum of Total Strength of Wizards**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `strength = [1,3,1,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `44`.
4. **Verification:** The following are all the contiguous groups of wizards:
- [1] from [

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
    def totalStrength(self, strength: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(strength)

        P = [0] * (n + 1)
        for i, x in enumerate(strength):
            P[i + 1] = P[i] + x
        PP = [0] * (n + 2)
        for k in range(n + 1):
            PP[k + 1] = PP[k] + P[k]

        total = 0
        stack = []
        for j in range(n + 1):
            cur = strength[j] if j < n else 0   # sentinel flushes the stack
            while stack and strength[stack[-1]] >= cur:
                i = stack.pop()
                L = stack[-1] if stack else -1
                R = j
                right = PP[R + 1] - PP[i + 1]
                left = PP[i + 1] - PP[L + 1]
                total += strength[i] * ((i - L) * right - (R - i) * left)
            stack.append(j)

        return total % MOD
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
- [3974. Maximum Total Sum of K Selected Elements](../../3501-4000/3974-maximum-total-sum-of-k-selected-elements/)
- [477. Total Hamming Distance](../../0001-0500/0477-total-hamming-distance/)
- [1010. Pairs of Songs With Total Durations Divisible by 60](../../1001-1500/1010-pairs-of-songs-with-total-durations-divisible-by-60/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-total-strength-of-wizards/)
