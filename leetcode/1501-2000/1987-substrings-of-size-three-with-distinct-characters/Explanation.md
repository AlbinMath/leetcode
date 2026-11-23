# LeetCode 1876: Substrings of Size Three with Distinct Characters

**LeetCode Problem #1876 — Substrings of Size Three with Distinct Characters**
Solve LeetCode Substrings of Size Three with Distinct Characters using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Substrings of Size Three with Distinct Characters |
| LeetCode | #1876 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A string is **good** if there are no repeated characters.

Given a string `s`​​​​​, return *the number of **good substrings** of length **three **in *`s`​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A **substring** is a contiguous sequence of characters in a string.

## Constraints
- `1 <= s.length <= 100`
- `s`​​​​​​ consists of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "xyzzaz"`
- **Output:** `1`
- **Explanation:** There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

### Example 2
- **Input:** `s = "aababcabc"`
- **Output:** `4`
- **Explanation:** There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Substrings of Size Three with Distinct Characters**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "xyzzaz"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

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
    int countGoodSubstrings(string s) {
        int count = 0;

        for (int i = 0; i + 2 < s.length(); i++) {
            if (s[i] != s[i + 1] &&
                s[i + 1] != s[i + 2] &&
                s[i] != s[i + 2]) {
                count++;
            }
        }

        return count;
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
- [1358. Number of Substrings Containing All Three Characters](../../1001-1500/1460-number-of-substrings-containing-all-three-characters/)
- [828. Count Unique Characters of All Substrings of a Given String](../../0501-1000/0855-count-unique-characters-of-all-substrings-of-a-given-string/)
- [1316. Distinct Echo Substrings](../../1001-1500/1244-distinct-echo-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/)
