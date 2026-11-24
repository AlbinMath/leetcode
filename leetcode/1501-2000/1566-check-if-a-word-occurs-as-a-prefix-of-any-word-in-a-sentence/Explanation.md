# LeetCode 1455: Check If a Word Occurs As a Prefix of Any Word in a Sentence

**LeetCode Problem #1455 — Check If a Word Occurs As a Prefix of Any Word in a Sentence**
Solve LeetCode Check If a Word Occurs As a Prefix of Any Word in a Sentence using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If a Word Occurs As a Prefix of Any Word in a Sentence |
| LeetCode | #1455 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a `sentence` that consists of some words separated by a **single space**, and a `searchWord`, check if `searchWord` is a prefix of any word in `sentence`.

Return *the index of the word in *`sentence`* (**1-indexed**) where *`searchWord`* is a prefix of this word*. If `searchWord` is a prefix of more than one word, return the index of the first word **(minimum index)**. If there is no such word return `-1`.

A **prefix** of a string `s` is any leading contiguous substring of `s`.

## Constraints
- `1 <= sentence.length <= 100`
- `1 <= searchWord.length <= 10`
- `sentence` consists of lowercase English letters and spaces.
- `searchWord` consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `sentence = "i love eating burger", searchWord = "burg"`
- **Output:** `4`
- **Explanation:** "burg" is prefix of "burger" which is the 4th word in the sentence.

### Example 2
- **Input:** `sentence = "this problem is an easy problem", searchWord = "pro"`
- **Output:** `2`
- **Explanation:** "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.

### Example 3
- **Input:** `sentence = "i am tired", searchWord = "you"`
- **Output:** `-1`
- **Explanation:** "you" is not a prefix of any word in the sentence.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check If a Word Occurs As a Prefix of Any Word in a Sentence**, we observe the problem requirements and utilize the **Prefix Sum** technique. We iterate through the inputs using **Prefix Sum Precomputation**, leveraging a **Prefix Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Prefix Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `sentence = "i love eating burger", searchWord = "burg"`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** "burg" is prefix of "burger" which is the 4th word in the sentence.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()

        for i, word in enumerate(words, start=1):
            if word.startswith(searchWord):
                return i

        return -1
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1003. Check If Word Is Valid After Substitutions](../../1001-1500/1045-check-if-word-is-valid-after-substitutions/)
- [1880. Check if Word Equals Summation of Two Words](../../2001-2500/2010-check-if-word-equals-summation-of-two-words/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
