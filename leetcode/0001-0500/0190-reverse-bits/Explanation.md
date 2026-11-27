# LeetCode 190: Reverse Bits

**LeetCode Problem #190 — Reverse Bits**
Solve LeetCode Reverse Bits using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Bits |
| LeetCode | #190 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Reverse bits of a given 32 bits signed integer.

## Constraints
- `0 <= n <= 2^31 - 2`
- `n` is even.

## Examples
### Example 1
- **Input:** `n = 43261596`
- **Output:** `964176192`
- **Explanation:** Integer 
 Binary 
 
 
 43261596 
 00000010100101000001111010011100 
 
 
 964176192 
 00111001011110000010100101000000

### Example 2
- **Input:** `n = 2147483644`
- **Output:** `1073741822`
- **Explanation:** Integer 
 Binary 
 
 
 2147483644 
 01111111111111111111111111111100 
 
 
 1073741822 
 00111111111111111111111111111110

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Reverse Bits**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 43261596`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `964176192`.
4. **Verification:** Integer 
 Binary 
 
 
 43261596 
 00000010100101000001111010011100 
 
 
 964176192 
 00111001011110000010100101000000

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
    def reverseBits(self, n):
        result = 0

        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1

        return result
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
- [338. Counting Bits](../../0001-0500/0338-counting-bits/)
- [693. Binary Number with Alternating Bits](../../0501-1000/0693-binary-number-with-alternating-bits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-bits/)
