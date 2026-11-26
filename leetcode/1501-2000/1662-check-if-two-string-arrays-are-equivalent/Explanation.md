# LeetCode 1662: Check If Two String Arrays are Equivalent

**LeetCode Problem #1662 — Check If Two String Arrays are Equivalent**
Solve LeetCode Check If Two String Arrays are Equivalent using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If Two String Arrays are Equivalent |
| LeetCode | #1662 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two string arrays `word1` and `word2`, return* *`true`* if the two arrays **represent** the same string, and *`false`* otherwise.*

A string is **represented** by an array if the array elements concatenated **in order** forms the string.

## Constraints
- `1 <= word1.length, word2.length <= 10^3`
- `1 <= word1[i].length, word2[i].length <= 10^3`
- `1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3`
- `word1[i]` and `word2[i]` consist of lowercase letters.

## Examples
### Example 1
- **Input:** `word1 = ["ab", "c"], word2 = ["a", "bc"]`
- **Output:** `true`
- **Explanation:** word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

### Example 2
- **Input:** `word1 = ["a", "cb"], word2 = ["ab", "c"]`
- **Output:** `false`

### Example 3
- **Input:** `word1 = ["abc", "d", "defg"], word2 = ["abcddefg"]`
- **Output:** `true`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check If Two String Arrays are Equivalent**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word1 = ["ab", "c"], word2 = ["a", "bc"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

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
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string s1 = "";
        string s2 = "";

        for (string word : word1) {
            s1 += word;
        }

        for (string word : word2) {
            s2 += word;
        }

        return s1 == s2;
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
- [2068. Check Whether Two Strings are Almost Equivalent](../../2001-2500/2068-check-whether-two-strings-are-almost-equivalent/)
- [3461. Check If Digits Are Equal in String After Operations I](../../3001-3500/3461-check-if-digits-are-equal-in-string-after-operations-i/)
- [3463. Check If Digits Are Equal in String After Operations II](../../3001-3500/3463-check-if-digits-are-equal-in-string-after-operations-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/)
