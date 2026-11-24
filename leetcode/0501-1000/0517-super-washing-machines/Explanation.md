# LeetCode 517: Super Washing Machines

**LeetCode Problem #517 — Super Washing Machines**
Solve LeetCode Super Washing Machines using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Super Washing Machines |
| LeetCode | #517 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have `n` super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any `m` (`1 <= m <= n`) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time.

Given an integer array `machines` representing the number of dresses in each washing machine from left to right on the line, return *the minimum number of moves to make all the washing machines have the same number of dresses*. If it is not possible to do it, return `-1`.

## Constraints
- `n == machines.length`
- `1 <= n <= 10^4`
- `0 <= machines[i] <= 10^5`

## Examples
### Example 1
- **Input:** `machines = [1,0,5]`
- **Output:** `3`
- **Explanation:** 1st move: 1 0 <-- 5 => 1 1 4
2nd move: 1 <-- 1 <-- 4 => 2 1 3
3rd move: 2 1 <-- 3 => 2 2 2

### Example 2
- **Input:** `machines = [0,3,0]`
- **Output:** `2`
- **Explanation:** 1st move: 0 <-- 3 0 => 1 2 0
2nd move: 1 2 --> 0 => 1 1 1

### Example 3
- **Input:** `machines = [0,2,0]`
- **Output:** `-1`
- **Explanation:** It's impossible to make all three washing machines have the same number of dresses.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Super Washing Machines**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `machines = [1,0,5]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** 1st move: 1 0 <-- 5 => 1 1 4
2nd move: 1 <-- 1 <-- 4 => 2 1 3
3rd move: 2 1 <-- 3 => 2 2 2

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
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n:
            return -1
        avg = total // n
        ans = 0
        prefix = 0
        for i, m in enumerate(machines):
            left = prefix - i * avg
            right = (total - prefix - m) - (n - 1 - i) * avg
            if left < 0 and right < 0:
                cost = -left - right
            else:
                cost = max(abs(left), abs(right))
            ans = max(ans, cost)
            prefix += m
        return ans
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
- [372. Super Pow](../../0001-0500/0372-super-pow/)
- [906. Super Palindromes](../../0501-1000/0906-super-palindromes/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/super-washing-machines/)
