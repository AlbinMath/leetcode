# LeetCode 1961: Check If String Is a Prefix of Array

**LeetCode Problem #1961 — Check If String Is a Prefix of Array**
Solve LeetCode Check If String Is a Prefix of Array using C++ and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If String Is a Prefix of Array |
| LeetCode | #1961 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `s` and an array of strings `words`, determine whether `s` is a **prefix string** of `words`.

A string `s` is a **prefix string** of `words` if `s` can be made by concatenating the first `k` strings in `words` for some **positive** `k` no larger than `words.length`.

Return `true`* if *`s`* is a **prefix string** of *`words`*, or *`false`* otherwise*.

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 20`
- `1 <= s.length <= 1000`
- `words[i]` and `s` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "iloveleetcode", words = ["i","love","leetcode","apples"]`
- **Output:** `true`
- **Explanation:** s can be made by concatenating "i", "love", and "leetcode" together.

### Example 2
- **Input:** `s = "iloveleetcode", words = ["apples","i","love","leetcode"]`
- **Output:** `false`
- **Explanation:** It is impossible to make s using a prefix of arr.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check If String Is a Prefix of Array**, we observe the problem requirements and utilize the **Prefix Sum** technique. We iterate through the inputs using **Prefix Sum Precomputation**, leveraging a **Prefix Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Prefix Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "iloveleetcode", words = ["i","love","leetcode","apples"]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** s can be made by concatenating "i", "love", and "leetcode" together.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        string prefix = "";

        for (string word : words) {
            prefix += word;

            if (prefix == s) {
                return true;
            }

            if (prefix.size() > s.size()) {
                return false;
            }
        }

        return false;
    }
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1250. Check If It Is a Good Array](../../1001-1500/1372-check-if-it-is-a-good-array/)
- [1497. Check If Array Pairs Are Divisible by k](../../1501-2000/1620-check-if-array-pairs-are-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/)
