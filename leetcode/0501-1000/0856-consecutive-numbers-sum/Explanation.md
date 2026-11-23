# LeetCode 829: Consecutive Numbers Sum

**LeetCode Problem #829 — Consecutive Numbers Sum**
Solve LeetCode Consecutive Numbers Sum using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Consecutive Numbers Sum |
| LeetCode | #829 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, return *the number of ways you can write *`n`* as the sum of consecutive positive integers.*

## Constraints
- `1 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 5`
- **Output:** `2`
- **Explanation:** 5 = 2 + 3

### Example 2
- **Input:** `n = 9`
- **Output:** `3`
- **Explanation:** 9 = 4 + 5 = 2 + 3 + 4

### Example 3
- **Input:** `n = 15`
- **Output:** `4`
- **Explanation:** 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Consecutive Numbers Sum**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** 5 = 2 + 3

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
    def consecutiveNumbersSum(self, n):
        count = 0
        k = 1
        while k * (k - 1) // 2 < n:
            if (n - k * (k - 1) // 2) % k == 0:
                count += 1
            k += 1
        return count
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
- [129. Sum Root to Leaf Numbers](../../0001-0500/0129-sum-root-to-leaf-numbers/)
- [633. Sum of Square Numbers](../../0501-1000/0633-sum-of-square-numbers/)
- [985. Sum of Even Numbers After Queries](../../1001-1500/1027-sum-of-even-numbers-after-queries/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/consecutive-numbers-sum/)
