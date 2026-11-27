# LeetCode 1221: Split a String in Balanced Strings

**LeetCode Problem #1221 — Split a String in Balanced Strings**
Solve LeetCode Split a String in Balanced Strings using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split a String in Balanced Strings |
| LeetCode | #1221 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
**Balanced** strings are those that have an equal quantity of `'L'` and `'R'` characters.

Given a **balanced** string `s`, split it into some number of substrings such that:

Each substring is balanced.

Return *the **maximum** number of balanced strings you can obtain.*

## Constraints
- `2 <= s.length <= 1000`
- `s[i]` is either `'L'` or `'R'`.
- `s` is a **balanced** string.

## Examples
### Example 1
- **Input:** `s = "RLRRLLRLRL"`
- **Output:** `4`
- **Explanation:** s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

### Example 2
- **Input:** `s = "RLRRRLLRLL"`
- **Output:** `2`
- **Explanation:** s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2^nd and 5^th substrings are not balanced.

### Example 3
- **Input:** `s = "LLLLRRRR"`
- **Output:** `1`
- **Explanation:** s can be split into "LLLLRRRR".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Split a String in Balanced Strings**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "RLRRLLRLRL"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0

        for char in s:
            if char == 'R':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                count += 1

        return count
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1234. Replace the Substring for Balanced String](../../1001-1500/1234-replace-the-substring-for-balanced-string/)
- [1653. Minimum Deletions to Make String Balanced](../../1501-2000/1653-minimum-deletions-to-make-string-balanced/)
- [1963. Minimum Number of Swaps to Make the String Balanced](../../1501-2000/1963-minimum-number-of-swaps-to-make-the-string-balanced/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-a-string-in-balanced-strings/)
