# LeetCode 1816: Truncate Sentence

**LeetCode Problem #1816 — Truncate Sentence**
Solve LeetCode Truncate Sentence using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Truncate Sentence |
| LeetCode | #1816 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **sentence** is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of **only** uppercase and lowercase English letters (no punctuation).

For example, `"Hello World"`, `"HELLO"`, and `"hello world hello world"` are all sentences.

You are given a sentence `s`​​​​​​ and an integer `k`​​​​​​. You want to **truncate** `s`​​​​​​ such that it contains only the **first** `k`​​​​​​ words. Return `s`​​​​*​​ after **truncating** it.*

## Constraints
- `1 <= s.length <= 500`
- `k` is in the range `[1, the number of words in s]`.
- `s` consist of only lowercase and uppercase English letters and spaces.
- The words in `s` are separated by a single space.
- There are no leading or trailing spaces.

## Examples
### Example 1
- **Input:** `s = "Hello how are you Contestant", k = 4`
- **Output:** `"Hello how are you"`
- **Explanation:** The words in s are ["Hello", "how", "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".

### Example 2
- **Input:** `s = "What is the solution to this problem", k = 4`
- **Output:** `"What is the solution"`
- **Explanation:** The words in s are ["What", "is", "the", "solution", "to", "this", "problem"].
The first 4 words are ["What", "is", "the", "solution"].
Hence, you should return "What is the solution".

### Example 3
- **Input:** `s = "chopper is not a tanuki", k = 5`
- **Output:** `"chopper is not a tanuki"`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Truncate Sentence**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "Hello how are you Contestant", k = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Hello how are you"`.
4. **Verification:** The words in s are ["Hello", "how", "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    string truncateSentence(string s, int k) {
        int spaces = 0;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') {
                spaces++;

                if (spaces == k) {
                    return s.substr(0, i);
                }
            }
        }

        return s;
    }
};
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
- [1451. Rearrange Words in a Sentence](../../1001-1500/1451-rearrange-words-in-a-sentence/)
- [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](../../1001-1500/1455-check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)
- [1813. Sentence Similarity III](../../1501-2000/1813-sentence-similarity-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/truncate-sentence/)
