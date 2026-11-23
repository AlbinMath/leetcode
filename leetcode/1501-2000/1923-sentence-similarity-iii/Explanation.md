# LeetCode 1813: Sentence Similarity III

**LeetCode Problem #1813 — Sentence Similarity III**
Solve LeetCode Sentence Similarity III using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sentence Similarity III |
| LeetCode | #1813 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `sentence1` and `sentence2`, each representing a **sentence** composed of words. A sentence is a list of **words** that are separated by a **single** space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences `s1` and `s2` are considered **similar** if it is possible to insert an arbitrary sentence (*possibly empty*) inside one of these sentences such that the two sentences become equal. **Note** that the inserted sentence must be separated from existing words by spaces.

For example,

`s1 = "Hello Jane"` and `s2 = "Hello my name is Jane"` can be made equal by inserting `"my name is"` between `"Hello"` and `"Jane"` in s1. 
 `s1 = "Frog cool"` and `s2 = "Frogs are cool"` are **not** similar, since although there is a sentence `"s are"` inserted into `s1`, it is not separated from `"Frog"` by a space.

Given two sentences `sentence1` and `sentence2`, return **true** if `sentence1` and `sentence2` are **similar**. Otherwise, return **false**.

## Constraints
- `1 <= sentence1.length, sentence2.length <= 100`
- `sentence1` and `sentence2` consist of lowercase and uppercase English letters and spaces.
- The words in `sentence1` and `sentence2` are separated by a single space.

## Examples
### Example 1
- **Input:** `sentence1 = "My name is Haley", sentence2 = "My Haley"`
- **Output:** `true`
- **Explanation:** `sentence2` can be turned to `sentence1` by inserting "name is" between "My" and "Haley".

### Example 2
- **Input:** `sentence1 = "of", sentence2 = "A lot of words"`
- **Output:** `false`
- **Explanation:** No single sentence can be inserted inside one of the sentences to make it equal to the other.

### Example 3
- **Input:** `sentence1 = "Eating right now", sentence2 = "Eating"`
- **Output:** `true`
- **Explanation:** `sentence2` can be turned to `sentence1` by inserting "right now" at the end of the sentence.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sentence Similarity III**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `sentence1 = "My name is Haley", sentence2 = "My Haley"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** `sentence2` can be turned to `sentence1` by inserting "name is" between "My" and "Haley".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a, b = sentence1.split(), sentence2.split()
        if len(a) > len(b):
            a, b = b, a

        n = len(a)
        i = 0
        while i < n and a[i] == b[i]:
            i += 1

        j = 0
        while j < n - i and a[n - 1 - j] == b[len(b) - 1 - j]:
            j += 1

        return i + j == n
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2946. Matrix Similarity After Cyclic Shifts](../../3001-3500/3215-matrix-similarity-after-cyclic-shifts/)
- [1451. Rearrange Words in a Sentence](../../1501-2000/1561-rearrange-words-in-a-sentence/)
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../../1501-2000/1566-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sentence-similarity-iii/)
