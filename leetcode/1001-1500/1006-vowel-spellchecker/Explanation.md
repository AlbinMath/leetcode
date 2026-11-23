# LeetCode 966: Vowel Spellchecker

**LeetCode Problem #966 — Vowel Spellchecker**
Solve LeetCode Vowel Spellchecker using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Vowel Spellchecker |
| LeetCode | #966 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a `wordlist`, we want to implement a spellchecker that converts a query word into a correct word.

For a given `query` word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (**case-insensitive**), then the query word is returned with the same case as the case in the wordlist.

Example: `wordlist = ["yellow"]`, `query = "YellOw"`: `correct = "yellow"` 
 Example: `wordlist = ["Yellow"]`, `query = "yellow"`: `correct = "Yellow"` 
 Example: `wordlist = ["yellow"]`, `query = "yellow"`: `correct = "yellow"` 
 
 
 Vowel Errors: If after replacing the vowels `('a', 'e', 'i', 'o', 'u')` of the query word with any vowel individually, it matches a word in the wordlist (**case-insensitive**), then the query word is returned with the same case as the match in the wordlist.
 
 Example: `wordlist = ["YellOw"]`, `query = "yollow"`: `correct = "YellOw"` 
 Example: `wordlist = ["YellOw"]`, `query = "yeellow"`: `correct = ""` (no match) 
 Example: `wordlist = ["YellOw"]`, `query = "yllw"`: `correct = ""` (no match)

In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (**case-sensitive**), you should return the same word back. 
 When the query matches a word up to capitalization, you should return the first such match in the wordlist. 
 When the query matches a word up to vowel errors, you should return the first such match in the wordlist. 
 If the query has no matches in the wordlist, you should return the empty string.

Given some `queries`, return a list of words `answer`, where `answer[i]` is the correct word for `query = queries[i]`.

## Constraints
- `1 <= wordlist.length, queries.length <= 5000`
- `1 <= wordlist[i].length, queries[i].length <= 7`
- `wordlist[i]` and `queries[i]` consist only of only English letters.

## Examples
### Example 1
- **Input:** `wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]`
- **Output:** `["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]`

### Example 2
- **Input:** `wordlist = ["yellow"], queries = ["YellOw"]`
- **Output:** `["yellow"]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Vowel Spellchecker**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def devowel(w: str) -> str:
            return ''.join('*' if ch in vowels else ch for ch in w.lower())

        exact = set(wordlist)
        case_map = {}
        vowel_map = {}

        for w in wordlist:
            case_map.setdefault(w.lower(), w)
            vowel_map.setdefault(devowel(w), w)

        res = []
        for q in queries:
            if q in exact:
                res.append(q)
            elif q.lower() in case_map:
                res.append(case_map[q.lower()])
            else:
                res.append(vowel_map.get(devowel(q), ""))
        return res
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1641. Count Sorted Vowel Strings](../../1501-2000/1761-count-sorted-vowel-strings/)
- [2062. Count Vowel Substrings of a String](../../2001-2500/2186-count-vowel-substrings-of-a-string/)
- [3305. Count of Substrings Containing Every Vowel and K Consonants I](../../3501-4000/3570-count-of-substrings-containing-every-vowel-and-k-consonants-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/vowel-spellchecker/)
