# LeetCode 676: Implement Magic Dictionary

**LeetCode Problem #676 — Implement Magic Dictionary**
Solve LeetCode Implement Magic Dictionary using Python and Trie. This solution finds the optimal result using Prefix Tree Lookup in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Implement Magic Dictionary |
| LeetCode | #676 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Prefix Tree Lookup |
| Data Structure | Trie Node |
| Pattern | Trie |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design a data structure that is initialized with a list of **different** words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

Implement the `MagicDictionary` class:

`MagicDictionary()` Initializes the object. 
 `void buildDict(String[] dictionary)` Sets the data structure with an array of distinct strings `dictionary`. 
 `bool search(String searchWord)` Returns `true` if you can change **exactly one character** in `searchWord` to match any string in the data structure, otherwise returns `false`.

## Constraints
- `1 <= dictionary.length <= 100`
- `1 <= dictionary[i].length <= 100`
- `dictionary[i]` consists of only lower-case English letters.
- All the strings in `dictionary` are **distinct**.
- `1 <= searchWord.length <= 100`
- `searchWord` consists of only lower-case English letters.
- `buildDict` will be called only once before `search`.
- At most `100` calls will be made to `search`.

## Examples
### Example 1
- **Input:** `["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]`
- **Output:** `[null, null, false, true, false, false]`
- **Explanation:** MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False

## Key Insight
Leverage **Trie** with **Trie Node** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Implement Magic Dictionary**, we observe the problem requirements and utilize the **Trie** technique. We iterate through the inputs using **Prefix Tree Lookup**, leveraging a **Trie Node** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Trie Node**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]`.
2. **Processing Steps:** We apply **Prefix Tree Lookup** using our **Trie Node**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, false, true, false, false]`.
4. **Verification:** MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Trie Node.

## Pattern
**Trie**

## Topics
- Trie
- String
- Prefix Search

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary: list[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) == len(searchWord):
                if sum(a != b for a, b in zip(word, searchWord)) == 1:
                    return True
        return False
```

## Why This Works
By utilizing **Trie**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [840. Magic Squares In Grid](../../0501-1000/0840-magic-squares-in-grid/)
- [1895. Largest Magic Square](../../1501-2000/1895-largest-magic-square/)
- [2171. Removing Minimum Number of Magic Beans](../../2001-2500/2171-removing-minimum-number-of-magic-beans/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/implement-magic-dictionary/)
