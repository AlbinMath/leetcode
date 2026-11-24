# LeetCode 3374: First Letter Capitalization II

**LeetCode Problem #3374 — First Letter Capitalization II**
Solve LeetCode First Letter Capitalization II using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | First Letter Capitalization II |
| LeetCode | #3374 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Table: `user_content`

+--------------+---------+
| Column Name | Type |
+--------------+---------+
| content_id | int |
| content_text | varchar |
+--------------+---------+
content_id is the unique key for this table.
Each row contains a unique ID and the corresponding text content.

A **word** is a maximal non-empty sequence of characters that does not contain a space.

Write a solution to transform the text in the `content_text` column by applying the following rules to each word:

If the word starts with a character that is **not** an English letter, leave the entire word **unchanged**. 
 Otherwise, if the word consists of two or more non-empty parts of English letters connected by hyphens `-`, convert the **first letter of each part** to uppercase and the **remaining letters of each part** to lowercase. For example, `top-rated` becomes `Top-Rated` and `FR-ONT-end` becomes `Fr-Ont-End`. 
 Otherwise, convert the **first letter** of the word to uppercase and all **remaining English letters** to lowercase. Any special characters remain unchanged.

All other **formatting** and **spacing** must remain **unchanged**.

Return *the result table that includes both the original `content_text` and the modified text following the above rules*.

The result format is in the following example.

## Constraints
- `content_text` contains only English letters, spaces, and the characters `\`, `@`, `-`, `/`, `^`, and `,`.

## Examples
Consider the standard input for **First Letter Capitalization II**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **First Letter Capitalization II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **In-Place Array Traversal & Index Mapping** step by step to the input yields the expected result.

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
import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    def transform_word(word: str) -> str:
        if not word or not word[0].isalpha():
            return word
        
        parts = word.split('-')
        if len(parts) >= 2 and all(p.isalpha() for p in parts):
            return '-'.join(p.capitalize() for p in parts)
        
        return word[0].upper() + word[1:].lower()

    def transform_text(text: str) -> str:
        return ' '.join(transform_word(w) for w in text.split(' '))

    return pd.DataFrame({
        'content_id': user_content['content_id'],
        'original_text': user_content['content_text'],
        'converted_text': user_content['content_text'].apply(transform_text)
    })
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
- [2351. First Letter to Appear Twice](../../2001-2500/2351-first-letter-to-appear-twice/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [744. Find Smallest Letter Greater Than Target](../../0501-1000/0744-find-smallest-letter-greater-than-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/first-letter-capitalization-ii/)
