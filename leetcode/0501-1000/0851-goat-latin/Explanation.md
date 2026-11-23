# LeetCode 824: Goat Latin

**LeetCode Problem #824 — Goat Latin**
Solve LeetCode Goat Latin using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Goat Latin |
| LeetCode | #824 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `sentence` that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel (`'a'`, `'e'`, `'i'`, `'o'`, or `'u'`), append `"ma"` to the end of the word.

For example, the word `"apple"` becomes `"applema"`. 
 
 
 If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add `"ma"`.
 
 For example, the word `"goat"` becomes `"oatgma"`. 
 
 
 Add one letter `'a'` to the end of each word per its word index in the sentence, starting with `1`.
 
 For example, the first word gets `"a"` added to the end, the second word gets `"aa"` added to the end, and so on.

Return* the final sentence representing the conversion from sentence to Goat Latin*.

## Constraints
- `1 <= sentence.length <= 150`
- `sentence` consists of English letters and spaces.
- `sentence` has no leading or trailing spaces.
- All the words in `sentence` are separated by a single space.

## Examples
### Example 1
- **Input:** `sentence = "I speak Goat Latin"`
- **Output:** `"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"`

### Example 2
- **Input:** `sentence = "The quick brown fox jumped over the lazy dog"`
- **Output:** `"heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Goat Latin**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `sentence = "I speak Goat Latin"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"`.

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
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []

        for i, word in enumerate(words, start=1):
            if word[0] not in vowels:
                word = word[1:] + word[0]

            word += "ma" + "a" * i
            result.append(word)

        return " ".join(result)
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
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [27. Remove Element](../../0001-0500/0027-remove-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/goat-latin/)
