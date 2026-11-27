# LeetCode 693: Binary Number with Alternating Bits

**LeetCode Problem #693 — Binary Number with Alternating Bits**
Solve LeetCode Binary Number with Alternating Bits using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Number with Alternating Bits |
| LeetCode | #693 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

## Constraints
- `1 <= n <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `n = 5`
- **Output:** `true`
- **Explanation:** The binary representation of 5 is: 101

### Example 2
- **Input:** `n = 7`
- **Output:** `false`
- **Explanation:** The binary representation of 7 is: 111.

### Example 3
- **Input:** `n = 11`
- **Output:** `false`
- **Explanation:** The binary representation of 11 is: 1011.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Binary Number with Alternating Bits**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

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
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The binary representation of 5 is: 101

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
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)[2:]

        for i in range(1, len(binary)):
            if binary[i] == binary[i - 1]:
                return False

        return True
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
- [1864. Minimum Number of Swaps to Make the Binary String Alternating](../../1501-2000/1864-minimum-number-of-swaps-to-make-the-binary-string-alternating/)
- [1888. Minimum Number of Flips to Make the Binary String Alternating](../../1501-2000/1888-minimum-number-of-flips-to-make-the-binary-string-alternating/)
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0762-prime-number-of-set-bits-in-binary-representation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-number-with-alternating-bits/)
