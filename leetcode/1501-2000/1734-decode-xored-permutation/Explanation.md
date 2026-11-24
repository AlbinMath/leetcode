# LeetCode 1734: Decode XORed Permutation

**LeetCode Problem #1734 — Decode XORed Permutation**
Solve LeetCode Decode XORed Permutation using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Decode XORed Permutation |
| LeetCode | #1734 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an integer array `perm` that is a permutation of the first `n` positive integers, where `n` is always **odd**.

It was encoded into another integer array `encoded` of length `n - 1`, such that `encoded[i] = perm[i] XOR perm[i + 1]`. For example, if `perm = [1,3,2]`, then `encoded = [2,1]`.

Given the `encoded` array, return *the original array* `perm`. It is guaranteed that the answer exists and is unique.

## Constraints
- `3 <= n < 10^5`
- `n` is odd.
- `encoded.length == n - 1`

## Examples
### Example 1
- **Input:** `encoded = [3,1]`
- **Output:** `[1,2,3]`
- **Explanation:** If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]

### Example 2
- **Input:** `encoded = [6,5,4,6]`
- **Output:** `[2,4,1,5,3]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Decode XORed Permutation**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `encoded = [3,1]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3]`.
4. **Verification:** If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]

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
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        total = 0
        for i in range(1, n + 1):
            total ^= i

        odd = 0
        for i in range(1, n - 1, 2):
            odd ^= encoded[i]

        perm = [total ^ odd]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm
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
- [1720. Decode XORed Array](../../1501-2000/1720-decode-xored-array/)
- [91. Decode Ways](../../0001-0500/0091-decode-ways/)
- [394. Decode String](../../0001-0500/0394-decode-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/decode-xored-permutation/)
