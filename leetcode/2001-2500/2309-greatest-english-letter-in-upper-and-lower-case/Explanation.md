# LeetCode 2309: Greatest English Letter in Upper and Lower Case

**LeetCode Problem #2309 — Greatest English Letter in Upper and Lower Case**
Solve LeetCode Greatest English Letter in Upper and Lower Case using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Greatest English Letter in Upper and Lower Case |
| LeetCode | #2309 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string of English letters `s`, return *the **greatest **English letter which occurs as **both** a lowercase and uppercase letter in* `s`. The returned letter should be in **uppercase**. If no such letter exists, return *an empty string*.

An English letter `b` is **greater** than another letter `a` if `b` appears **after** `a` in the English alphabet.

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase and uppercase English letters.

## Examples
### Example 1
- **Input:** `s = "l`
- **Output:** `"E"`
- **Explanation:** The letter 'E' is the only letter to appear in both lower and upper case.

### Example 2
- **Input:** `s = "a`
- **Output:** `"R"`
- **Explanation:** The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

### Example 3
- **Input:** `s = "AbCdEfGhIjK"`
- **Output:** `""`
- **Explanation:** There is no letter that appears in both lower and upper case.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Greatest English Letter in Upper and Lower Case**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "l`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"E"`.
4. **Verification:** The letter 'E' is the only letter to appear in both lower and upper case.

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
class Solution(object):
    def greatestLetter(self, s):
        seen = set(s)
        for code in range(ord('Z'), ord('A') - 1, -1):
            upper = chr(code)
            if upper in seen and upper.lower() in seen:
                return upper
        return ""
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
- [784. Letter Case Permutation](../../0501-1000/0784-letter-case-permutation/)
- [709. To Lower Case](../../0501-1000/0709-to-lower-case/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/)
