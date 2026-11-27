# LeetCode 434: Number of Segments in a String

**LeetCode Problem #434 — Number of Segments in a String**
Solve LeetCode Number of Segments in a String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Segments in a String |
| LeetCode | #434 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, return *the number of segments in the string*.

A **segment** is defined to be a contiguous sequence of **non-space characters**.

## Constraints
- `0 <= s.length <= 300`
- `s` consists of lowercase and uppercase English letters, digits, or one of the following characters `"!@#$%^&*()_+-=',.:"`.
- The only space character in `s` is `' '`.

## Examples
### Example 1
- **Input:** `s = "Hello, my name is John"`
- **Output:** `5`
- **Explanation:** The five segments are ["Hello,", "my", "name", "is", "John"]

### Example 2
- **Input:** `s = "Hello"`
- **Output:** `1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Segments in a String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "Hello, my name is John"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The five segments are ["Hello,", "my", "name", "is", "John"]

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
    def countSegments(self, s):
        count = 0

        for i in range(len(s)):
            # Current character is not a space
            # and either it's the first character
            # or the previous character is a space
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
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
- [806. Number of Lines To Write String](../../0501-1000/0806-number-of-lines-to-write-string/)
- [1375. Number of Times Binary String Is Prefix-Aligned](../../1001-1500/1375-number-of-times-binary-string-is-prefix-aligned/)
- [1525. Number of Good Ways to Split a String](../../1501-2000/1525-number-of-good-ways-to-split-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-segments-in-a-string/)
