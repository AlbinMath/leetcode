# LeetCode 316: Remove Duplicate Letters

**LeetCode Problem #316 — Remove Duplicate Letters**
Solve LeetCode Remove Duplicate Letters using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Duplicate Letters |
| LeetCode | #316 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s`, remove duplicate letters so that every letter appears once and only once. The relative order of the letters that were not removed must be preserved. You must make sure your result is **the smallest in lexicographical order** among all possible results.

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "bcabc"`
- **Output:** `"abc"`

### Example 2
- **Input:** `s = "cbacdcbc"`
- **Output:** `"acdb"`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove Duplicate Letters**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "bcabc"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"abc"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c in in_stack:
                continue
            while stack and stack[-1] > c and last[stack[-1]] > i:
                in_stack.discard(stack.pop())
            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [848. Shifting Letters](../../0501-1000/0878-shifting-letters/)
- [917. Reverse Only Letters](../../0501-1000/0953-reverse-only-letters/)
- [1255. Maximum Score Words Formed by Letters](../../1001-1500/1381-maximum-score-words-formed-by-letters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-duplicate-letters/)
