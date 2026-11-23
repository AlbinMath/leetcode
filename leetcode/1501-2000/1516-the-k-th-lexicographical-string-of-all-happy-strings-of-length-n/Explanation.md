# LeetCode 1415: The k-th Lexicographical String of All Happy Strings of Length n

**LeetCode Problem #1415 — The k-th Lexicographical String of All Happy Strings of Length n**
Solve LeetCode The k-th Lexicographical String of All Happy Strings of Length n using Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The k-th Lexicographical String of All Happy Strings of Length n |
| LeetCode | #1415 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **happy string** is a string that:

consists only of letters of the set `['a', 'b', 'c']`. 
 `s[i] != s[i + 1]` for all values of `i` from `1` to `s.length - 1` (string is 1-indexed).

For example, strings **"abc", "ac", "b"** and **"abcbabcbcb"** are all happy strings and strings **"aa", "baa"** and **"ababbc"** are not happy strings.

Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted in lexicographical order.

Return *the kth string* of this list or return an **empty string** if there are less than `k` happy strings of length `n`.

## Constraints
- `1 <= n <= 10`
- `1 <= k <= 100`

## Examples
### Example 1
- **Input:** `n = 1, k = 3`
- **Output:** `"c"`
- **Explanation:** The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

### Example 2
- **Input:** `n = 1, k = 4`
- **Output:** `""`
- **Explanation:** There are only 3 happy strings of length 1.

### Example 3
- **Input:** `n = 3, k = 9`
- **Output:** `"cab"`
- **Explanation:** There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9^th string = "cab"

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **The k-th Lexicographical String of All Happy Strings of Length n**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1, k = 3`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"c"`.
4. **Verification:** The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

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
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def backtrack(s):
            if len(s) == n:
                res.append(s)
                return

            for c in "abc":
                if not s or s[-1] != c:
                    backtrack(s + c)

        backtrack("")

        return res[k - 1] if k <= len(res) else ""
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
- [1461. Check If a String Contains All Binary Codes of Size K](../../1501-2000/1557-check-if-a-string-contains-all-binary-codes-of-size-k/)
- [3304. Find the K-th Character in String Game I](../../3501-4000/3600-find-the-k-th-character-in-string-game-i/)
- [3307. Find the K-th Character in String Game II](../../3501-4000/3601-find-the-k-th-character-in-string-game-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)
