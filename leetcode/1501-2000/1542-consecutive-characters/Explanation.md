# LeetCode 1446: Consecutive Characters

**LeetCode Problem #1446 — Consecutive Characters**
Solve LeetCode Consecutive Characters using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Consecutive Characters |
| LeetCode | #1446 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **power** of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string `s`, return *the **power** of* `s`.

## Constraints
- `1 <= s.length <= 500`
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "leetcode"`
- **Output:** `2`
- **Explanation:** The substring "ee" is of length 2 with the character 'e' only.

### Example 2
- **Input:** `s = "abbcccddddeeeeedcba"`
- **Output:** `5`
- **Explanation:** The substring "eeeee" is of length 5 with the character 'e' only.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Consecutive Characters**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "leetcode"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The substring "ee" is of length 2 with the character 'e' only.

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
    def maxPower(self, s: str) -> int:
        current = 1
        maximum = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                current = 1

            maximum = max(maximum, current)

        return maximum
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
- [1576. Replace All ?'s to Avoid Consecutive Repeating Characters](../../1501-2000/1698-replace-all-s-to-avoid-consecutive-repeating-characters/)
- [3970. Shortest Path With At Most K Consecutive Identical Characters](../../4001-4500/4104-shortest-path-with-at-most-k-consecutive-identical-characters/)
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/consecutive-characters/)
