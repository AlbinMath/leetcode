# LeetCode 290: Word Pattern

**LeetCode Problem #290 — Word Pattern**
Solve LeetCode Word Pattern using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Word Pattern |
| LeetCode | #290 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a `pattern` and a string `s`, find if `s` follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`. Specifically:

Each letter in `pattern` maps to **exactly** one unique word in `s`. 
 Each unique word in `s` maps to **exactly** one letter in `pattern`. 
 No two letters map to the same word, and no two words map to the same letter.

## Constraints
- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters.
- `1 <= s.length <= 3000`
- `s` contains only lowercase English letters and spaces `' '`.
- `s` **does not contain** any leading or trailing spaces.
- All the words in `s` are separated by a **single space**.

## Examples
### Example 1
- **Input:** `pattern = "abba", s = "dog cat cat dog"`
- **Output:** `true`
- **Explanation:** The bijection can be established as: 

 
 `'a'` maps to `"dog"`. 
 `'b'` maps to `"cat"`.

### Example 2
- **Input:** `pattern = "abba", s = "dog cat cat fish"`
- **Output:** `false`

### Example 3
- **Input:** `pattern = "aaaa", s = "dog cat cat dog"`
- **Output:** `false`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Word Pattern**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `pattern = "abba", s = "dog cat cat dog"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The bijection can be established as: 

 
 `'a'` maps to `"dog"`. 
 `'b'` maps to `"cat"`.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool wordPattern(string pattern, string s) {
        vector<string> words;
        string word;

        // Split string into words
        stringstream ss(s);
        while (ss >> word) {
            words.push_back(word);
        }

        // Number of characters and words must match
        if (pattern.length() != words.size()) {
            return false;
        }

        unordered_map<char, string> charToWord;
        unordered_map<string, char> wordToChar;

        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern[i];
            string w = words[i];

            // Character already mapped to a different word
            if (charToWord.count(c) && charToWord[c] != w) {
                return false;
            }

            // Word already mapped to a different character
            if (wordToChar.count(w) && wordToChar[w] != c) {
                return false;
            }

            charToWord[c] = w;
            wordToChar[w] = c;
        }

        return true;
    }
};
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
- [58. Length of Last Word](../../0001-0500/0058-length-of-last-word/)
- [79. Word Search](../../0001-0500/0079-word-search/)
- [126. Word Ladder II](../../0001-0500/0126-word-ladder-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/word-pattern/)
