# LeetCode 1220: Count Vowels Permutation

**LeetCode Problem #1220 — Count Vowels Permutation**
Solve LeetCode Count Vowels Permutation using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Vowels Permutation |
| LeetCode | #1220 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, your task is to count how many strings of length `n` can be formed under the following rules:

Each character is a lower case vowel (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) 
 Each vowel `'a'` may only be followed by an `'e'`. 
 Each vowel `'e'` may only be followed by an `'a'` or an `'i'`. 
 Each vowel `'i'` **may not** be followed by another `'i'`. 
 Each vowel `'o'` may only be followed by an `'i'` or a `'u'`. 
 Each vowel `'u'` may only be followed by an `'a'`.

Since the answer may be too large, return it modulo `10^9 + 7`.

## Constraints
- `1 <= n <= 2 * 10^4`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `5`
- **Explanation:** All possible strings are: "a", "e", "i" , "o" and "u".

### Example 2
- **Input:** `n = 2`
- **Output:** `10`
- **Explanation:** All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Vowels Permutation**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** All possible strings are: "a", "e", "i" , "o" and "u".

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
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        
        a = e = i = o = u = 1
        
        for _ in range(n - 1):
            a, e, i, o, u = (
                (e + i + u) % MOD,
                (a + i) % MOD,
                (e + o) % MOD,
                i % MOD,
                (i + o) % MOD
            )
            
        return (a + e + i + o + u) % MOD
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
- [38. Count and Say](../../0001-0500/0038-count-and-say/)
- [204. Count Primes](../../0001-0500/0204-count-primes/)
- [222. Count Complete Tree Nodes](../../0001-0500/0222-count-complete-tree-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-vowels-permutation/)
