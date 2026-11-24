# LeetCode 838: Push Dominoes

**LeetCode Problem #838 — Push Dominoes**
Solve LeetCode Push Dominoes using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Push Dominoes |
| LeetCode | #838 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string `dominoes` representing the initial state where:

`dominoes[i] = 'L'`, if the `i^th` domino has been pushed to the left, 
 `dominoes[i] = 'R'`, if the `i^th` domino has been pushed to the right, and 
 `dominoes[i] = '.'`, if the `i^th` domino has not been pushed.

Return *a string representing the final state*.

## Constraints
- `n == dominoes.length`
- `1 <= n <= 10^5`
- `dominoes[i]` is either `'L'`, `'R'`, or `'.'`.

## Examples
### Example 1
- **Input:** `dominoes = "RR.L"`
- **Output:** `"RR.L"`
- **Explanation:** The first domino expends no additional force on the second domino.

### Example 2
- **Input:** `dominoes = ".L.R...LR..L.."`
- **Output:** `"LL.RR.LLRRLL.."`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Push Dominoes**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `dominoes = "RR.L"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"RR.L"`.
4. **Verification:** The first domino expends no additional force on the second domino.

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
    def pushDominoes(self, dominoes: str) -> str:
        s = 'L' + dominoes + 'R'
        res = []
        prev = 0  # index of the previous force character in s

        for i in range(1, len(s)):
            if s[i] == '.':
                continue

            gap = i - prev - 1
            if prev > 0:
                res.append(s[prev])  # emit the force character itself

            if s[prev] == s[i]:
                res.append(s[i] * gap)             # L..L or R..R
            elif s[prev] == 'L' and s[i] == 'R':
                res.append('.' * gap)              # pushed apart
            else:                                  # R..L
                res.append('R' * (gap // 2))
                res.append('.' * (gap % 2))
                res.append('L' * (gap // 2))

            prev = i

        return ''.join(res)
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
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [27. Remove Element](../../0001-0500/0027-remove-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/push-dominoes/)
