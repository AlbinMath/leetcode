# LeetCode 1790: Check if One String Swap Can Make Strings Equal

**LeetCode Problem #1790 — Check if One String Swap Can Make Strings Equal**
Solve LeetCode Check if One String Swap Can Make Strings Equal using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if One String Swap Can Make Strings Equal |
| LeetCode | #1790 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `s1` and `s2` of equal length. A **string swap** is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return `true` *if it is possible to make both strings equal by performing **at most one string swap **on **exactly one** of the strings. *Otherwise, return `false`.

## Constraints
- `1 <= s1.length, s2.length <= 100`
- `s1.length == s2.length`
- `s1` and `s2` consist of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s1 = "bank", s2 = "kanb"`
- **Output:** `true`
- **Explanation:** For example, swap the first character with the last character of s2 to make "bank".

### Example 2
- **Input:** `s1 = "attack", s2 = "defend"`
- **Output:** `false`
- **Explanation:** It is impossible to make them equal with one string swap.

### Example 3
- **Input:** `s1 = "kelb", s2 = "kelb"`
- **Output:** `true`
- **Explanation:** The two strings are already equal, so no string swap operation is required.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if One String Swap Can Make Strings Equal**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s1 = "bank", s2 = "kanb"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** For example, swap the first character with the last character of s2 to make "bank".

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
    bool areAlmostEqual(string s1, string s2) {
        vector<int> diff;

        for (int i = 0; i < s1.size(); i++) {
            if (s1[i] != s2[i]) {
                diff.push_back(i);
            }
        }

        if (diff.size() == 0) {
            return true;
        }

        if (diff.size() == 2) {
            int i = diff[0];
            int j = diff[1];

            return s1[i] == s2[j] && s1[j] == s2[i];
        }

        return false;
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
- [3461. Check If Digits Are Equal in String After Operations I](../../3001-3500/3461-check-if-digits-are-equal-in-string-after-operations-i/)
- [3463. Check If Digits Are Equal in String After Operations II](../../3001-3500/3463-check-if-digits-are-equal-in-string-after-operations-ii/)
- [1433. Check If a String Can Break Another String](../../1001-1500/1433-check-if-a-string-can-break-another-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/)
