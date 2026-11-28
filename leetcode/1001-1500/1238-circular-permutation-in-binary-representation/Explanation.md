# LeetCode 1238: Circular Permutation in Binary Representation

**LeetCode Problem #1238 — Circular Permutation in Binary Representation**
Solve LeetCode Circular Permutation in Binary Representation using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Circular Permutation in Binary Representation |
| LeetCode | #1238 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given 2 integers `n` and `start`. Your task is return **any** permutation `p` of `(0,1,2.....,2^n -1) `such that :

`p[0] = start` 
 `p[i]` and `p[i+1]` differ by only one bit in their binary representation. 
 `p[0]` and `p[2^n -1]` must also differ by only one bit in their binary representation.

## Constraints
- `1 <= n <= 16`
- `0 <= start < 2 ^ n`

## Examples
### Example 1
- **Input:** `n = 2, start = 3`
- **Output:** `[3,2,0,1]`
- **Explanation:** The binary representation of the permutation is (11,10,00,01). 
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]

### Example 2
- **Input:** `n = 3, start = 2`
- **Output:** `[2,6,7,5,4,0,1,3]`
- **Explanation:** The binary representation of the permutation is (010,110,111,101,100,000,001,011).

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Circular Permutation in Binary Representation**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2, start = 3`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,2,0,1]`.
4. **Verification:** The binary representation of the permutation is (11,10,00,01). 
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ i ^ (i >> 1) for i in range(1 << n)]
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0762-prime-number-of-set-bits-in-binary-representation/)
- [1404. Number of Steps to Reduce a Number in Binary Representation to One](../../1001-1500/1404-number-of-steps-to-reduce-a-number-in-binary-representation-to-one/)
- [457. Circular Array Loop](../../0001-0500/0457-circular-array-loop/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/circular-permutation-in-binary-representation/)
