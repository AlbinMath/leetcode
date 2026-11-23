# LeetCode 2119: A Number After a Double Reversal

**LeetCode Problem #2119 — A Number After a Double Reversal**
Solve LeetCode A Number After a Double Reversal using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | A Number After a Double Reversal |
| LeetCode | #2119 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
**Reversing** an integer means to reverse all its digits.

For example, reversing `2021` gives `1202`. Reversing `12300` gives `321` as the **leading zeros are not retained**.

Given an integer `num`, **reverse** `num` to get `reversed1`, **then reverse** `reversed1` to get `reversed2`. Return `true` *if* `reversed2` *equals* `num`. Otherwise return `false`.

## Constraints
- `0 <= num <= 10^6`

## Examples
### Example 1
- **Input:** `num = 526`
- **Output:** `true`
- **Explanation:** Reverse num to get 625, then reverse 625 to get 526, which equals num.

### Example 2
- **Input:** `num = 1800`
- **Output:** `false`
- **Explanation:** Reverse num to get 81, then reverse 81 to get 18, which does not equal num.

### Example 3
- **Input:** `num = 0`
- **Output:** `true`
- **Explanation:** Reverse num to get 0, then reverse 0 to get 0, which equals num.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **A Number After a Double Reversal**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 526`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Reverse num to get 625, then reverse 625 to get 526, which equals num.

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
    def isSameAfterReversals(self, num):
        return num == 0 or num % 10 != 0
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
- [1946. Largest Number After Mutating Substring](../../2001-2500/2077-largest-number-after-mutating-substring/)
- [2400. Number of Ways to Reach a Position After Exactly k Steps](../../2001-2500/2477-number-of-ways-to-reach-a-position-after-exactly-k-steps/)
- [2816. Double a Number Represented as a Linked List](../../2501-3000/2871-double-a-number-represented-as-a-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/a-number-after-a-double-reversal/)
