# LeetCode 1528: Shuffle String

**LeetCode Problem #1528 — Shuffle String**
Solve LeetCode Shuffle String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shuffle String |
| LeetCode | #1528 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and an integer array `indices` of the **same length**. The string `s` will be shuffled such that the character at the `i^th` position moves to `indices[i]` in the shuffled string.

Return *the shuffled string*.

## Constraints
- `s.length == indices.length == n`
- `1 <= n <= 100`
- `s` consists of only lowercase English letters.
- `0 <= indices[i] < n`
- All values of `indices` are **unique**.

## Examples
### Example 1
- **Input:** `s = "codeleet", `indices` = [4,5,6,7,0,2,1,3]`
- **Output:** `"leetcode"`
- **Explanation:** As shown, "codeleet" becomes "leetcode" after shuffling.

### Example 2
- **Input:** `s = "abc", `indices` = [0,1,2]`
- **Output:** `"abc"`
- **Explanation:** After shuffling, each character remains in its position.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shuffle String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "codeleet", `indices` = [4,5,6,7,0,2,1,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"leetcode"`.
4. **Verification:** As shown, "codeleet" becomes "leetcode" after shuffling.

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
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = [""] * len(s)

        for i, char in enumerate(s):
            result[indices[i]] = char

        return "".join(result)
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
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)
- [87. Scramble String](../../0001-0500/0087-scramble-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shuffle-string/)
