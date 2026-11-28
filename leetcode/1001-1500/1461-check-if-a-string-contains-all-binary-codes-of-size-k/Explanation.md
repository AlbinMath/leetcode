# LeetCode 1461: Check If a String Contains All Binary Codes of Size K

**LeetCode Problem #1461 — Check If a String Contains All Binary Codes of Size K**
Solve LeetCode Check If a String Contains All Binary Codes of Size K using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If a String Contains All Binary Codes of Size K |
| LeetCode | #1461 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a binary string `s` and an integer `k`, return `true` *if every binary code of length* `k` *is a substring of* `s`. Otherwise, return `false`.

## Constraints
- `1 <= s.length <= 5 * 10^5`
- `s[i]` is either `'0'` or `'1'`.
- `1 <= k <= 20`

## Examples
### Example 1
- **Input:** `s = "00110110", k = 2`
- **Output:** `true`
- **Explanation:** The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

### Example 2
- **Input:** `s = "0110", k = 1`
- **Output:** `true`
- **Explanation:** The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.

### Example 3
- **Input:** `s = "0110", k = 2`
- **Output:** `false`
- **Explanation:** The binary code "00" is of length 2 and does not exist in the array.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check If a String Contains All Binary Codes of Size K**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "00110110", k = 2`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        if len(s) - k + 1 < need:
            return False
        mask = need - 1
        seen = [False] * need
        count = 0
        h = 0
        for i, ch in enumerate(s):
            h = ((h << 1) | (ord(ch) - 48)) & mask
            if i >= k - 1 and not seen[h]:
                seen[h] = True
                count += 1
                if count == need:
                    return True
        return False
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1437. Check If All 1's Are at Least Length K Places Away](../../1001-1500/1437-check-if-all-1s-are-at-least-length-k-places-away/)
- [2133. Check if Every Row and Column Contains All Numbers](../../2001-2500/2133-check-if-every-row-and-column-contains-all-numbers/)
- [1784. Check if Binary String Has at Most One Segment of Ones](../../1501-2000/1784-check-if-binary-string-has-at-most-one-segment-of-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)
