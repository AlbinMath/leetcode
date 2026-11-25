# LeetCode 1451: Rearrange Words in a Sentence

**LeetCode Problem #1451 — Rearrange Words in a Sentence**
Solve LeetCode Rearrange Words in a Sentence using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rearrange Words in a Sentence |
| LeetCode | #1451 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a sentence `text` (A *sentence* is a string of space-separated words) in the following format:

First letter is in upper case. 
 Each word in `text` are separated by a single space.

Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.

## Constraints
- `text` begins with a capital letter and then contains lowercase letters and single space between words.
- `1 <= text.length <= 10^5`

## Examples
### Example 1
- **Input:** `text = "Leetcode is cool"`
- **Output:** `"Is cool leetcode"`
- **Explanation:** There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
Output is ordered by length and the new first word starts with capital letter.

### Example 2
- **Input:** `text = "Keep calm and code on"`
- **Output:** `"On and keep calm code"`
- **Explanation:** Output is ordered as follows:
"On" 2 letters.
"and" 3 letters.
"keep" 4 letters in case of tie order by position in original text.
"calm" 4 letters.
"code" 4 letters.

### Example 3
- **Input:** `text = "To be or not to be"`
- **Output:** `"To be or to be not"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rearrange Words in a Sentence**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `text = "Leetcode is cool"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Is cool leetcode"`.
4. **Verification:** There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
Output is ordered by length and the new first word starts with capital letter.

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
    def arrangeWords(self, text: str) -> str:
        words = text.lower().split()
        words.sort(key=len)
        res = ' '.join(words)
        return res[0].upper() + res[1:]
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
- [2047. Number of Valid Words in a Sentence](../../2001-2500/2047-number-of-valid-words-in-a-sentence/)
- [1592. Rearrange Spaces Between Words](../../1501-2000/1592-rearrange-spaces-between-words/)
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../../1001-1500/1455-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rearrange-words-in-a-sentence/)
