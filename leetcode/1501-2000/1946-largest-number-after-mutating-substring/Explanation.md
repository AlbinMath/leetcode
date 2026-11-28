# LeetCode 1946: Largest Number After Mutating Substring

**LeetCode Problem #1946 — Largest Number After Mutating Substring**
Solve LeetCode Largest Number After Mutating Substring using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Largest Number After Mutating Substring |
| LeetCode | #1946 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `num`, which represents a large integer. You are also given a **0-indexed** integer array `change` of length `10` that maps each digit `0-9` to another digit. More formally, digit `d` maps to digit `change[d]`.

You may **choose** to mutate a single substring of `num`. To mutate a substring, replace each digit `num[i]` with the digit it maps to in `change` (i.e. replace `num[i]` with `change[num[i]]`).

Return *a string representing the **largest** possible integer after **mutating** (or choosing not to) a **single substring** of *`num`.

A **substring** is a contiguous sequence of characters within the string.

## Constraints
- `1 <= num.length <= 10^5`
- `num` consists of only digits `0-9`.
- `change.length == 10`
- `0 <= change[d] <= 9`

## Examples
### Example 1
- **Input:** `num = " 1 32", change = [9,8,5,0,3,6,4,2,6,8]`
- **Output:** `" 8 32"`
- **Explanation:** Replace the substring "1":
- 1 maps to change[1] = 8.
Thus, " 1 32" becomes " 8 32".
"832" is the largest number that can be created, so return it.

### Example 2
- **Input:** `num = " 021 ", change = [9,4,3,5,7,2,1,9,0,6]`
- **Output:** `" 934 "`
- **Explanation:** Replace the substring "021":
- 0 maps to change[0] = 9.
- 2 maps to change[2] = 3.
- 1 maps to change[1] = 4.
Thus, " 021 " becomes " 934 ".
"934" is the largest number that can be created, so return it.

### Example 3
- **Input:** `num = "5", change = [1,4,7,5,3,2,5,6,9,4]`
- **Output:** `"5"`
- **Explanation:** "5" is already the largest number that can be created, so return it.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Largest Number After Mutating Substring**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = " 1 32", change = [9,8,5,0,3,6,4,2,6,8]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `" 8 32"`.
4. **Verification:** Replace the substring "1":
- 1 maps to change[1] = 8.
Thus, " 1 32" becomes " 8 32".
"832" is the largest number that can be created, so return it.

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
    def maximumNumber(self, num: str, change: list[int]) -> str:
        digits = list(num)
        mutated = False
        
        for i, ch in enumerate(digits):
            d = int(ch)
            
            if change[d] > d:
                # Start or continue mutating on a strictly better digit
                digits[i] = str(change[d])
                mutated = True
            elif change[d] == d:
                # Neutral digit: keep going if we've already started, otherwise ignore
                continue
            else:
                # change[d] < d: if we already started mutating, we must stop here
                if mutated:
                    break
                    
        return "".join(digits)
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
- [2231. Largest Number After Digit Swaps by Parity](../../2001-2500/2231-largest-number-after-digit-swaps-by-parity/)
- [179. Largest Number](../../0001-0500/0179-largest-number/)
- [586. Customer Placing the Largest Number of Orders](../../0501-1000/0586-customer-placing-the-largest-number-of-orders/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/largest-number-after-mutating-substring/)
