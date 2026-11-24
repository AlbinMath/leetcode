# LeetCode 43: Multiply Strings

**LeetCode Problem #43 — Multiply Strings**
Solve LeetCode Multiply Strings using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Multiply Strings |
| LeetCode | #43 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

## Constraints
- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.

## Examples
### Example 1
- **Input:** `num1 = "2", num2 = "3"`
- **Output:** `"6"`

### Example 2
- **Input:** `num1 = "123", num2 = "456"`
- **Output:** `"56088"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Multiply Strings**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num1 = "2", num2 = "3"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"6"`.

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
    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result = [0] * (m + n)

        # Multiply every digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                product = a * b

                pos2 = i + j + 1
                pos1 = i + j

                result[pos2] += product

                # Handle carry
                result[pos1] += result[pos2] // 10
                result[pos2] %= 10

        # Remove leading zeros
        start = 0

        while start < len(result) - 1 and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))
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
- [3754. Concatenate Non-Zero Digits and Multiply by Sum I](../../3501-4000/3754-concatenate-non-zero-digits-and-multiply-by-sum-i/)
- [3756. Concatenate Non-Zero Digits and Multiply by Sum II](../../3501-4000/3756-concatenate-non-zero-digits-and-multiply-by-sum-ii/)
- [205. Isomorphic Strings](../../0001-0500/0205-isomorphic-strings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/multiply-strings/)
