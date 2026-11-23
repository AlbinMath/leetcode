# LeetCode 2429: Minimize XOR

**LeetCode Problem #2429 — Minimize XOR**
Solve LeetCode Minimize XOR using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize XOR |
| LeetCode | #2429 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two positive integers `num1` and `num2`, find the positive integer `x` such that:

`x` has the same number of set bits as `num2`, and 
 The value `x XOR num1` is **minimal**.

Note that `XOR` is the bitwise XOR operation.

Return *the integer *`x`. The test cases are generated such that `x` is **uniquely determined**.

The number of **set bits** of an integer is the number of `1`'s in its binary representation.

## Constraints
- `1 <= num1, num2 <= 10^9`

## Examples
### Example 1
- **Input:** `num1 = 3, num2 = 5`
- **Output:** `3`
- **Explanation:** The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer

### Example 2
- **Input:** `num1 = 1, num2 = 12`
- **Output:** `3`
- **Explanation:** The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimize XOR**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num1 = 3, num2 = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer

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
    def minimizeXor(self, num1, num2):
        c = bin(num2).count('1')
        x = 0

        # match the highest set bits of num1 first
        for b in range(31, -1, -1):
            if c == 0:
                break
            if (num1 >> b) & 1:
                x |= 1 << b
                c -= 1

        # leftover ones go to the lowest unset bits of num1
        b = 0
        while c > 0:
            if not (x >> b) & 1:
                x |= 1 << b
                c -= 1
            b += 1
        return x
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
- [3599. Partition Array to Minimize XOR](../../3501-4000/3913-partition-array-to-minimize-xor/)
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [810. Chalkboard XOR Game](../../0501-1000/0828-chalkboard-xor-game/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-xor/)
