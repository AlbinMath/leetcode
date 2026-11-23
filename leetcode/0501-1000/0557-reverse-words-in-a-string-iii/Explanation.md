# LeetCode 557: Reverse Words in a String III

**LeetCode Problem #557 — Reverse Words in a String III**
Solve LeetCode Reverse Words in a String III using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Words in a String III |
| LeetCode | #557 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `s` contains printable **ASCII** characters.
- `s` does not contain any leading or trailing spaces.
- There is **at least one** word in `s`.
- All the words in `s` are separated by a single space.

## Examples
### Example 1
- **Input:** `s = "Let's take LeetCode contest"`
- **Output:** `"s'teL ekat edoCteeL tsetnoc"`

### Example 2
- **Input:** `s = "Mr Ding"`
- **Output:** `"rM gniD"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reverse Words in a String III**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "Let's take LeetCode contest"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"s'teL ekat edoCteeL tsetnoc"`.

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
    def reverseWords(self, s):
        words = s.split()

        for i in range(len(words)):
            words[i] = words[i][::-1]

        return ' '.join(words)
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
- [151. Reverse Words in a String](../../0001-0500/0151-reverse-words-in-a-string/)
- [3775. Reverse Words With Same Vowel Count](../../4001-4500/4157-reverse-words-with-same-vowel-count/)
- [344. Reverse String](../../0001-0500/0344-reverse-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-iii/)
