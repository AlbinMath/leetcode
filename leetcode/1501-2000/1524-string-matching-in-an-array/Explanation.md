# LeetCode 1408: String Matching in an Array

**LeetCode Problem #1408 — String Matching in an Array**
Solve LeetCode String Matching in an Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | String Matching in an Array |
| LeetCode | #1408 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of string `words`, return all strings in* *`words`* *that are a substring of another word. You can return the answer in **any order**.

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 30`
- `words[i]` contains only lowercase English letters.
- All the strings of `words` are **unique**.

## Examples
### Example 1
- **Input:** `words = ["mass","as","hero","superhero"]`
- **Output:** `["as","hero"]`
- **Explanation:** "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

### Example 2
- **Input:** `words = ["leetcode","et","code"]`
- **Output:** `["et","code"]`
- **Explanation:** "et", "code" are substring of "leetcode".

### Example 3
- **Input:** `words = ["blue","green","bu"]`
- **Output:** `[]`
- **Explanation:** No string of words is substring of another string.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **String Matching in an Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["mass","as","hero","superhero"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["as","hero"]`.
4. **Verification:** "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

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
    def stringMatching(self, words: list[str]) -> list[str]:
        result = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break

        return result
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
- [1961. Check If String Is a Prefix of Array](../../2001-2500/2093-check-if-string-is-a-prefix-of-array/)
- [2053. Kth Distinct String in an Array](../../2001-2500/2163-kth-distinct-string-in-an-array/)
- [2108. Find First Palindromic String in the Array](../../2001-2500/2231-find-first-palindromic-string-in-the-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/string-matching-in-an-array/)
