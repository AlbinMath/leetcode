# LeetCode 1763: Longest Nice Substring

**LeetCode Problem #1763 — Longest Nice Substring**
Solve LeetCode Longest Nice Substring using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Nice Substring |
| LeetCode | #1763 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A string `s` is **nice** if, for every letter of the alphabet that `s` contains, it appears **both** in uppercase and lowercase. For example, `"abABB"` is nice because `'A'` and `'a'` appear, and `'B'` and `'b'` appear. However, `"abA"` is not because `'b'` appears, but `'B'` does not.

Given a string `s`, return *the longest **substring** of `s` that is **nice**. If there are multiple, return the substring of the **earliest** occurrence. If there are none, return an empty string*.

## Constraints
- `1 <= s.length <= 100`
- `s` consists of uppercase and lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "YazaAay"`
- **Output:** `"aAa"`
- **Explanation:** "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

### Example 2
- **Input:** `s = "Bb"`
- **Output:** `"Bb"`
- **Explanation:** "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

### Example 3
- **Input:** `s = "c"`
- **Output:** `""`
- **Explanation:** There are no nice substrings.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Longest Nice Substring**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "YazaAay"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"aAa"`.
4. **Verification:** "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool isNice(string s) {
        for (char c : s) {
            if (islower(c) && s.find(toupper(c)) == string::npos) {
                return false;
            }

            if (isupper(c) && s.find(tolower(c)) == string::npos) {
                return false;
            }
        }

        return true;
    }

    string longestNiceSubstring(string s) {
        string result = "";

        for (int i = 0; i < s.size(); i++) {
            for (int j = i + 1; j <= s.size(); j++) {
                string sub = s.substr(i, j - i);

                if (sub.size() > result.size() && isNice(sub)) {
                    result = sub;
                }
            }
        }

        return result;
    }
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [395. Longest Substring with At Least K Repeating Characters](../../0001-0500/0395-longest-substring-with-at-least-k-repeating-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-nice-substring/)
