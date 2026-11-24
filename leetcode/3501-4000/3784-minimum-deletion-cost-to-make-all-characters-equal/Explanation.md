# LeetCode 3784: Minimum Deletion Cost to Make All Characters Equal

**LeetCode Problem #3784 — Minimum Deletion Cost to Make All Characters Equal**
Solve LeetCode Minimum Deletion Cost to Make All Characters Equal using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Deletion Cost to Make All Characters Equal |
| LeetCode | #3784 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` of length `n` and an integer array `cost` of the same length, where `cost[i]` is the cost to **delete** the `i^th` character of `s`.

You may delete any number of characters from `s` (possibly none), such that the resulting string is **non-empty** and consists of **equal** characters.

Return an integer denoting the **minimum** total deletion cost required.

## Constraints
- `n == s.length == cost.length`
- `1 <= n <= 10^5`
- `1 <= cost[i] <= 10^9`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "aabaac", cost = [1,2,3,4,1,10]`
- **Output:** `11`
- **Explanation:** Deleting the characters at indices 0, 1, 2, 3, 4 results in the string `"c"`, which consists of equal characters, and the total cost is `cost[0] + cost[1] + cost[2] + cost[3] + cost[4] = 1 + 2 + 3 + 4 + 1 = 11`.

### Example 2
- **Input:** `s = "abc", cost = [10,5,8]`
- **Output:** `13`
- **Explanation:** Deleting the characters at indices 1 and 2 results in the string `"a"`, which consists of equal characters, and the total cost is `cost[1] + cost[2] = 5 + 8 = 13`.

### Example 3
- **Input:** `s = "zzzzz", cost = [67,67,67,67,67]`
- **Output:** `0`
- **Explanation:** All characters in `s` are equal, so the deletion cost is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Deletion Cost to Make All Characters Equal**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "aabaac", cost = [1,2,3,4,1,10]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `11`.
4. **Verification:** Deleting the characters at indices 0, 1, 2, 3, 4 results in the string `"c"`, which consists of equal characters, and the total cost is `cost[0] + cost[1] + cost[2] + cost[3] + cost[4] = 1 + 2 + 3 + 4 + 1 = 11`.

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
from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        per = [0] * 26
        for ch, c in zip(s, cost):
            per[ord(ch) - 97] += c
        return sum(cost) - max(per)
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
- [1897. Redistribute Characters to Make All Strings Equal](../../1501-2000/1897-redistribute-characters-to-make-all-strings-equal/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [1941. Check if All Characters Have Equal Number of Occurrences](../../1501-2000/1941-check-if-all-characters-have-equal-number-of-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/)
