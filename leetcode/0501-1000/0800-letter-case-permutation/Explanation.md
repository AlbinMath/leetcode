# LeetCode 784: Letter Case Permutation

**LeetCode Problem #784 — Letter Case Permutation**
Solve LeetCode Letter Case Permutation using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Letter Case Permutation |
| LeetCode | #784 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, you can transform every letter individually to be lowercase or uppercase to create another string.

Return *a list of all possible strings we could create*. Return the output in **any order**.

## Constraints
- `1 <= s.length <= 12`
- `s` consists of lowercase English letters, uppercase English letters, and digits.

## Examples
### Example 1
- **Input:** `s = "a1b2"`
- **Output:** `["a1b2","a1B2","A1b2","A1B2"]`

### Example 2
- **Input:** `s = "3z4"`
- **Output:** `["3z4","3Z4"]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Letter Case Permutation**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "a1b2"`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["a1b2","a1B2","A1b2","A1B2"]`.

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
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [""]
        for ch in s:
            if ch.isalpha():
                res = [p + c for p in res for c in (ch.lower(), ch.upper())]
            else:
                res = [p + ch for p in res]
        return res
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
- [2309. Greatest English Letter in Upper and Lower Case](../../1001-1500/1363-greatest-english-letter-in-upper-and-lower-case/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [744. Find Smallest Letter Greater Than Target](../../0501-1000/0745-find-smallest-letter-greater-than-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/letter-case-permutation/)
