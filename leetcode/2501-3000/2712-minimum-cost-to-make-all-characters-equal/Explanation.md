# LeetCode 2712: Minimum Cost to Make All Characters Equal

**LeetCode Problem #2712 — Minimum Cost to Make All Characters Equal**
Solve LeetCode Minimum Cost to Make All Characters Equal using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Make All Characters Equal |
| LeetCode | #2712 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** binary string `s` of length `n` on which you can apply two types of operations:

Choose an index `i` and invert all characters from index `0` to index `i` (both inclusive), with a cost of `i + 1` 
 Choose an index `i` and invert all characters from index `i` to index `n - 1` (both inclusive), with a cost of `n - i`

Return *the **minimum cost **to make all characters of the string **equal***.

**Invert** a character means if its value is '0' it becomes '1' and vice-versa.

## Constraints
- `1 <= s.length == n <= 10^5`
- `s[i]` is either `'0'` or `'1'`

## Examples
### Example 1
- **Input:** `s = "0011"`
- **Output:** `2`
- **Explanation:** Apply the second operation with `i = 2` to obtain `s = "0000" for a cost of 2`. It can be shown that 2 is the minimum cost to make all characters equal.

### Example 2
- **Input:** `s = "010101"`
- **Output:** `9`
- **Explanation:** Apply the first operation with i = 2 to obtain s = "101101" for a cost of 3.
Apply the first operation with i = 1 to obtain s = "011101" for a cost of 2. 
Apply the first operation with i = 0 to obtain s = "111101" for a cost of 1. 
Apply the second operation with i = 4 to obtain s = "111110" for a cost of 2.
Apply the second operation with i = 5 to obtain s = "111111" for a cost of 1. 
The total cost to make all characters equal is 9. It can be shown that 9 is the minimum cost to make all characters equal.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost to Make All Characters Equal**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "0011"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Apply the second operation with `i = 2` to obtain `s = "0000" for a cost of 2`. It can be shown that 2 is the minimum cost to make all characters equal.

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
    def minimumCost(self, s: str) -> int:
        n = len(s)
        total = 0
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                total += min(i + 1, n - i - 1)
        return total
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
- [3784. Minimum Deletion Cost to Make All Characters Equal](../../3501-4000/3784-minimum-deletion-cost-to-make-all-characters-equal/)
- [1897. Redistribute Characters to Make All Strings Equal](../../1501-2000/1897-redistribute-characters-to-make-all-strings-equal/)
- [2448. Minimum Cost to Make Array Equal](../../2001-2500/2448-minimum-cost-to-make-array-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/)
