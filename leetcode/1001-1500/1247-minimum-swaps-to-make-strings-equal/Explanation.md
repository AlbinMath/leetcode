# LeetCode 1247: Minimum Swaps to Make Strings Equal

**LeetCode Problem #1247 — Minimum Swaps to Make Strings Equal**
Solve LeetCode Minimum Swaps to Make Strings Equal using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Swaps to Make Strings Equal |
| LeetCode | #1247 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `s1` and `s2` of equal length consisting of letters `"x"` and `"y"` **only**. Your task is to make these two strings equal to each other. You can swap any two characters that belong to **different** strings, which means: swap `s1[i]` and `s2[j]`.

Return the minimum number of swaps required to make `s1` and `s2` equal, or return `-1` if it is impossible to do so.

## Constraints
- `1 <= s1.length, s2.length <= 1000`
- `s1.length == s2.length`
- `s1, s2` only contain `'x'` or `'y'`.

## Examples
### Example 1
- **Input:** `s1 = "xx", s2 = "yy"`
- **Output:** `1`
- **Explanation:** Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

### Example 2
- **Input:** `s1 = "xy", s2 = "yx"`
- **Output:** `2`
- **Explanation:** Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

### Example 3
- **Input:** `s1 = "xx", s2 = "xy"`
- **Output:** `-1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Swaps to Make Strings Equal**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s1 = "xx", s2 = "yy"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

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
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1

        if (xy + yx) % 2:
            return -1

        return xy // 2 + yx // 2 + 2 * (xy % 2)
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
- [3800. Minimum Cost to Make Two Binary Strings Equal](../../3501-4000/3800-minimum-cost-to-make-two-binary-strings-equal/)
- [1318. Minimum Flips to Make a OR b Equal to c](../../1001-1500/1318-minimum-flips-to-make-a-or-b-equal-to-c/)
- [1551. Minimum Operations to Make Array Equal](../../1501-2000/1551-minimum-operations-to-make-array-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/)
