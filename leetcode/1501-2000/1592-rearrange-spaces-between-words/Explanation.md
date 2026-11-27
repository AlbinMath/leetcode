# LeetCode 1592: Rearrange Spaces Between Words

**LeetCode Problem #1592 — Rearrange Spaces Between Words**
Solve LeetCode Rearrange Spaces Between Words using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rearrange Spaces Between Words |
| LeetCode | #1592 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `text` of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that `text` **contains at least one word**.

Rearrange the spaces so that there is an **equal** number of spaces between every pair of adjacent words and that number is **maximized**. If you cannot redistribute all the spaces equally, place the **extra spaces at the end**, meaning the returned string should be the same length as `text`.

Return *the string after rearranging the spaces*.

## Constraints
- `1 <= text.length <= 100`
- `text` consists of lowercase English letters and `' '`.
- `text` contains at least one word.

## Examples
### Example 1
- **Input:** `text = " this is a sentence "`
- **Output:** `"this is a sentence"`
- **Explanation:** There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.

### Example 2
- **Input:** `text = " practice makes perfect"`
- **Output:** `"practice makes perfect "`
- **Explanation:** There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Rearrange Spaces Between Words**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `text = " this is a sentence "`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"this is a sentence"`.
4. **Verification:** There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.

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
    string reorderSpaces(string text) {
        int spaces = 0;
        vector<string> words;
        string word;

        // Count spaces and extract words
        for (char c : text) {
            if (c == ' ') {
                spaces++;
            } else {
                word += c;
            }

            if (c == ' ' && !word.empty()) {
                words.push_back(word);
                word.clear();
            }
        }

        // Add the last word, if any
        if (!word.empty()) {
            words.push_back(word);
        }

        int n = words.size();
        int between = 0;
        int extra = spaces;

        if (n > 1) {
            between = spaces / (n - 1);
            extra = spaces % (n - 1);
        }

        string result;

        for (int i = 0; i < n; i++) {
            result += words[i];

            if (i < n - 1) {
                result += string(between, ' ');
            }
        }

        result += string(extra, ' ');

        return result;
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
- [1795. Rearrange Products Table](../../1501-2000/1795-rearrange-products-table/)
- [1866. Number of Ways to Rearrange Sticks With K Sticks Visible](../../1501-2000/1866-number-of-ways-to-rearrange-sticks-with-k-sticks-visible/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rearrange-spaces-between-words/)
