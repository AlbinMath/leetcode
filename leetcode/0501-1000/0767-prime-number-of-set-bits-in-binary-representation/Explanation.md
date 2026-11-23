# LeetCode 762: Prime Number of Set Bits in Binary Representation

**LeetCode Problem #762 — Prime Number of Set Bits in Binary Representation**
Solve LeetCode Prime Number of Set Bits in Binary Representation using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Prime Number of Set Bits in Binary Representation |
| LeetCode | #762 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers `left` and `right`, return *the **count** of numbers in the **inclusive** range *`[left, right]`* having a **prime number of set bits** in their binary representation*.

Recall that the **number of set bits** an integer has is the number of `1`'s present when written in binary.

For example, `21` written in binary is `10101`, which has `3` set bits.

## Constraints
- `1 <= left <= right <= 10^6`
- `0 <= right - left <= 10^4`

## Examples
### Example 1
- **Input:** `left = 6, right = 10`
- **Output:** `4`
- **Explanation:** 6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
8 -> 1000 (1 set bit, 1 is not prime)
9 -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.

### Example 2
- **Input:** `left = 10, right = 15`
- **Output:** `5`
- **Explanation:** 10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
5 numbers have a prime number of set bits.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Prime Number of Set Bits in Binary Representation**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `left = 6, right = 10`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** 6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
8 -> 1000 (1 set bit, 1 is not prime)
9 -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.

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
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        count = 0

        for num in range(left, right + 1):
            set_bits = bin(num).count('1')

            if set_bits in primes:
                count += 1

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
- [693. Binary Number with Alternating Bits](../../0501-1000/0693-binary-number-with-alternating-bits/)
- [3370. Smallest Number With All Set Bits](../../3501-4000/3676-smallest-number-with-all-set-bits/)
- [1404. Number of Steps to Reduce a Number in Binary Representation to One](../../1501-2000/1520-number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)
