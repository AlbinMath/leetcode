# LeetCode 664: Strange Printer

**LeetCode Problem #664 — Strange Printer**
Solve LeetCode Strange Printer using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Strange Printer |
| LeetCode | #664 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a strange printer with the following two special properties:

The printer can only print a sequence of **the same character** each time. 
 At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

Given a string `s`, return *the minimum number of turns the printer needed to print it*.

## Constraints
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aaabbb"`
- **Output:** `2`
- **Explanation:** Print "aaa" first and then print "bbb".

### Example 2
- **Input:** `s = "aba"`
- **Output:** `2`
- **Explanation:** Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Strange Printer**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aaabbb"`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Print "aaa" first and then print "bbb".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from functools import lru_cache

class Solution:
    def strangePrinter(self, s: str) -> int:
        t = ''.join(c for i, c in enumerate(s) if i == 0 or c != s[i-1])
        n = len(t)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            ans = 1 + dp(i + 1, j)
            for k in range(i + 1, j + 1):
                if t[k] == t[i]:
                    ans = min(ans, dp(i + 1, k - 1) + dp(k, j))
            return ans

        return dp(0, n - 1)
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1591. Strange Printer II](../../1501-2000/1696-strange-printer-ii/)
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)
- [72. Edit Distance](../../0001-0500/0072-edit-distance/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/strange-printer/)
