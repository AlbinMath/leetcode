# LeetCode 2595: Number of Even and Odd Bits

**LeetCode Problem #2595 — Number of Even and Odd Bits**
Solve LeetCode Number of Even and Odd Bits using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Even and Odd Bits |
| LeetCode | #2595 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **positive** integer `n`.

Let `even` denote the number of even indices in the binary representation of `n` with value 1.

Let `odd` denote the number of odd indices in the binary representation of `n` with value 1.

Note that bits are indexed from **right to left** in the binary representation of a number.

Return the array `[even, odd]`.

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 50`
- **Output:** `[1,2]`
- **Explanation:** The binary representation of 50 is `110010`. 

 It contains 1 on indices 1, 4, and 5.

### Example 2
- **Input:** `n = 2`
- **Output:** `[0,1]`
- **Explanation:** The binary representation of 2 is `10`. 

 It contains 1 only on index 1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Even and Odd Bits**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 50`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.
4. **Verification:** The binary representation of 50 is `110010`. 

 It contains 1 on indices 1, 4, and 5.

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
    def evenOddBit(self, n):
        res = [0, 0]
        i = 0
        while n:
            if n & 1:
                res[i & 1] += 1
            n >>= 1
            i += 1
        return res
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
- [191. Number of 1 Bits](../../0001-0500/0191-number-of-1-bits/)
- [693. Binary Number with Alternating Bits](../../0501-1000/0693-binary-number-with-alternating-bits/)
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0762-prime-number-of-set-bits-in-binary-representation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-even-and-odd-bits/)
