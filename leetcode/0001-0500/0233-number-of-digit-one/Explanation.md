# LeetCode 233: Number of Digit One

**LeetCode Problem #233 — Number of Digit One**
Solve LeetCode Number of Digit One using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Digit One |
| LeetCode | #233 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, count *the total number of digit *`1`* appearing in all non-negative integers less than or equal to* `n`.

## Constraints
- `0 <= n <= 10^9`

## Examples
### Example 1
- **Input:** `n = 13`
- **Output:** `6`

### Example 2
- **Input:** `n = 0`
- **Output:** `0`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Digit One**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 13`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.

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
    def countDigitOne(self, n: int) -> int:
        ans, i = 0, 1
        while i <= n:
            high = n // (i * 10)
            cur = (n // i) % 10
            low = n % i
            if cur == 0:
                ans += high * i
            elif cur == 1:
                ans += high * i + low + 1
            else:
                ans += (high + 1) * i
            i *= 10
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
- [1404. Number of Steps to Reduce a Number in Binary Representation to One](../../1001-1500/1404-number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)
- [2259. Remove Digit From Number to Maximize Result](../../2001-2500/2259-remove-digit-from-number-to-maximize-result/)
- [2283. Check if Number Has Equal Digit Count and Digit Value](../../2001-2500/2283-check-if-number-has-equal-digit-count-and-digit-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-digit-one/)
