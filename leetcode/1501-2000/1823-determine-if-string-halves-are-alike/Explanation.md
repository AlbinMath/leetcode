# LeetCode 1704: Determine if String Halves Are Alike

**LeetCode Problem #1704 — Determine if String Halves Are Alike**
Solve LeetCode Determine if String Halves Are Alike using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Determine if String Halves Are Alike |
| LeetCode | #1704 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` of even length. Split this string into two halves of equal lengths, and let `a` be the first half and `b` be the second half.

Two strings are **alike** if they have the same number of vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`, `'A'`, `'E'`, `'I'`, `'O'`, `'U'`). Notice that `s` contains uppercase and lowercase letters.

Return `true`* if *`a`* and *`b`* are **alike***. Otherwise, return `false`.

## Constraints
- `2 <= s.length <= 1000`
- `s.length` is even.
- `s` consists of **uppercase and lowercase** letters.

## Examples
### Example 1
- **Input:** `s = "book"`
- **Output:** `true`
- **Explanation:** a = "b o " and b = " o k". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

### Example 2
- **Input:** `s = "textbook"`
- **Output:** `false`
- **Explanation:** a = "t e xt" and b = "b oo k". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Determine if String Halves Are Alike**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "book"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** a = "b o " and b = " o k". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

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
    bool halvesAreAlike(string s) {
        int n = s.size();
        int count = 0;

        string vowels = "aeiouAEIOU";

        for (int i = 0; i < n / 2; i++) {
            if (vowels.find(s[i]) != string::npos) {
                count++;
            }
        }

        for (int i = n / 2; i < n; i++) {
            if (vowels.find(s[i]) != string::npos) {
                count--;
            }
        }

        return count == 0;
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1662. Check If Two String Arrays are Equivalent](../../1501-2000/1781-check-if-two-string-arrays-are-equivalent/)
- [3461. Check If Digits Are Equal in String After Operations I](../../3501-4000/3768-check-if-digits-are-equal-in-string-after-operations-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/determine-if-string-halves-are-alike/)
