# LeetCode 2405: Optimal Partition of String

**LeetCode Problem #2405 — Optimal Partition of String**
Solve LeetCode Optimal Partition of String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Optimal Partition of String |
| LeetCode | #2405 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, partition the string into one or more **substrings** such that the characters in each substring are **unique**. That is, no letter appears in a single substring more than **once**.

Return *the **minimum** number of substrings in such a partition.*

Note that each character should belong to exactly one substring in a partition.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only English lowercase letters.

## Examples
### Example 1
- **Input:** `s = "abacaba"`
- **Output:** `4`
- **Explanation:** Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

### Example 2
- **Input:** `s = "ssssss"`
- **Output:** `6`
- **Explanation:** The only valid partition is ("s","s","s","s","s","s").

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Optimal Partition of String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abacaba"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

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
    def partitionString(self, s: str) -> int:
        seen = set()
        count = 1
        for ch in s:
            if ch in seen:
                count += 1
                seen.clear()
            seen.add(ch)
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
- [2522. Partition String Into Substrings With Values at Most K](../../2501-3000/2522-partition-string-into-substrings-with-values-at-most-k/)
- [2767. Partition String Into Minimum Beautiful Substrings](../../2501-3000/2767-partition-string-into-minimum-beautiful-substrings/)
- [3597. Partition String ](../../3501-4000/3597-partition-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/optimal-partition-of-string/)
