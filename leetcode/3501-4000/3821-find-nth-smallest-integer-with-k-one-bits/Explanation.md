# LeetCode 3821: Find Nth Smallest Integer With K One Bits

**LeetCode Problem #3821 — Find Nth Smallest Integer With K One Bits**
Solve LeetCode Find Nth Smallest Integer With K One Bits using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Nth Smallest Integer With K One Bits |
| LeetCode | #3821 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two positive integers `n` and `k`.

Return an integer denoting the `n^th` smallest positive integer that has **exactly** `k` ones in its binary representation. It is guaranteed that the answer is **strictly less** than `2^50`.

## Constraints
- `1 <= n <= 2^50`
- `1 <= k <= 50`
- The answer is strictly less than `2^50`.

## Examples
### Example 1
- **Input:** `n = 4, k = 2`
- **Output:** `9`
- **Explanation:** The 4 smallest positive integers that have exactly `k = 2` ones in their binary representations are: 

 
 `3 = 11_2` 
 `5 = 101_2` 
 `6 = 110_2` 
 `9 = 1001_2`

### Example 2
- **Input:** `n = 3, k = 1`
- **Output:** `4`
- **Explanation:** The 3 smallest positive integers that have exactly `k = 1` one in their binary representations are: 

 
 `1 = 1_2` 
 `2 = 10_2` 
 `4 = 100_2`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Nth Smallest Integer With K One Bits**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, k = 2`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** The 4 smallest positive integers that have exactly `k = 2` ones in their binary representations are: 

 
 `3 = 11_2` 
 `5 = 101_2` 
 `6 = 110_2` 
 `9 = 1001_2`

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
mx = 50
c = [[0] * (mx + 1) for _ in range(mx)]
for i in range(mx):
    c[i][0] = 1
    for j in range(1, i + 1):
        c[i][j] = c[i - 1][j - 1] + c[i - 1][j]


class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        ans = 0
        for i in range(49, -1, -1):
            if n > c[i][k]:
                n -= c[i][k]
                ans |= 1 << i
                k -= 1
                if k == 0:
                    break
        return ans
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [373. Find K Pairs with Smallest Sums](../../0001-0500/0373-find-k-pairs-with-smallest-sums/)
- [1015. Smallest Integer Divisible by K](../../1001-1500/1015-smallest-integer-divisible-by-k/)
- [440. K-th Smallest in Lexicographical Order](../../0001-0500/0440-k-th-smallest-in-lexicographical-order/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/)
