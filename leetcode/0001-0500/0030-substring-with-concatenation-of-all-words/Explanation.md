# LeetCode 30: Substring with Concatenation of All Words

**LeetCode Problem #30 — Substring with Concatenation of All Words**
Solve LeetCode Substring with Concatenation of All Words using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Substring with Concatenation of All Words |
| LeetCode | #30 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and an array of strings `words`. All the strings of `words` are of **the same length**.

A **concatenated string** is a string that exactly contains all the strings of any permutation of `words` concatenated.

For example, if `words = ["ab","cd","ef"]`, then `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all concatenated strings. `"acdbef"` is not a concatenated string because it is not the concatenation of any permutation of `words`.

Return an array of *the starting indices* of all the concatenated substrings in `s`. You can return the answer in **any order**.

## Constraints
- `1 <= s.length <= 10^4`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 30`
- `s` and `words[i]` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "barfoothefoobarman", words = ["foo","bar"]`
- **Output:** `[0,9]`
- **Explanation:** The substring starting at 0 is `"barfoo"`. It is the concatenation of `["bar","foo"]` which is a permutation of `words`. 
The substring starting at 9 is `"foobar"`. It is the concatenation of `["foo","bar"]` which is a permutation of `words`.

### Example 2
- **Input:** `s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]`
- **Output:** `[]`
- **Explanation:** There is no concatenated substring.

### Example 3
- **Input:** `s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]`
- **Output:** `[6,9,12]`
- **Explanation:** The substring starting at 6 is `"foobarthe"`. It is the concatenation of `["foo","bar","the"]`. 
The substring starting at 9 is `"barthefoo"`. It is the concatenation of `["bar","the","foo"]`. 
The substring starting at 12 is `"thefoobar"`. It is the concatenation of `["the","foo","bar"]`.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Substring with Concatenation of All Words**, we observe the problem requirements and utilize the **Sliding Window** technique. By maintaining a **Array / Hash Set**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array / Hash Set** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "barfoothefoobarman", words = ["foo","bar"]`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,9]`.
4. **Verification:** The substring starting at 0 is `"barfoo"`. It is the concatenation of `["bar","foo"]` which is a permutation of `words`. 
The substring starting at 9 is `"foobar"`. It is the concatenation of `["foo","bar"]` which is a permutation of `words`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        # Required frequency of each word
        target = Counter(words)

        result = []

        # Try each possible alignment
        for offset in range(word_len):
            left = offset
            right = offset

            current = Counter()
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                # Word is not in words
                if word not in target:
                    current.clear()
                    count = 0
                    left = right
                    continue

                current[word] += 1
                count += 1

                # Too many occurrences of this word
                while current[word] > target[word]:
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

                # Found all words
                if count == word_count:
                    result.append(left)

                    # Move window forward
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

        return result
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [3503. Longest Palindrome After Substring Concatenation I](../../3501-4000/3503-longest-palindrome-after-substring-concatenation-i/)
- [1839. Longest Substring Of All Vowels in Order](../../1501-2000/1839-longest-substring-of-all-vowels-in-order/)
- [1910. Remove All Occurrences of a Substring](../../1501-2000/1910-remove-all-occurrences-of-a-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)
