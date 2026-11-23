# LeetCode 1374: Generate a String With Characters That Have Odd Counts

**LeetCode Problem #1374 — Generate a String With Characters That Have Odd Counts**
Solve LeetCode Generate a String With Characters That Have Odd Counts using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Generate a String With Characters That Have Odd Counts |
| LeetCode | #1374 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer `n`, *return a string with `n` characters such that each character in such string occurs **an odd number of times***.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return **any** of them.

## Constraints
- `1 <= n <= 500`

## Examples
### Example 1
- **Input:** `n = 4`
- **Output:** `"pppz"`
- **Explanation:** "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".

### Example 2
- **Input:** `n = 2`
- **Output:** `"xy"`
- **Explanation:** "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".

### Example 3
- **Input:** `n = 7`
- **Output:** `"holasss"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Generate a String With Characters That Have Odd Counts**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"pppz"`.
4. **Verification:** "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".

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
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a' * n

        return 'a' * (n - 1) + 'b'
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
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0855-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1239. Maximum Length of a Concatenated String with Unique Characters](../../1001-1500/1360-maximum-length-of-a-concatenated-string-with-unique-characters/)
- [1903. Largest Odd Number in String](../../2001-2500/2032-largest-odd-number-in-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/)
