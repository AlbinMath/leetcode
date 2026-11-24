# LeetCode 796: Rotate String

**LeetCode Problem #796 — Rotate String**
Solve LeetCode Rotate String using C++, JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rotate String |
| LeetCode | #796 |
| Difficulty | Easy |
| Language | C++, JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two strings `s` and `goal`, return `true` *if and only if* `s` *can become* `goal` *after some number of **shifts** on* `s`.

A **shift** on `s` consists of moving the leftmost character of `s` to the rightmost position.

For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

## Constraints
- `1 <= s.length, goal.length <= 100`
- `s` and `goal` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abcde", goal = "cdeab"`
- **Output:** `true`
- **Explanation:** Rotating `s` to the left by 2 positions moves `"ab"` to the end, resulting in `"cdeab"`, which is equal to `goal`.

### Example 2
- **Input:** `s = "abcde", goal = "abced"`
- **Output:** `false`
- **Explanation:** No sequence of rotations of `s` can produce `"abced"`. The characters appear in a different relative order, so `goal` is not a rotation of `s`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a clever **string concatenation** trick:

1. **Length Check:** If the lengths differ, return `false` immediately.
2. **Concatenation:** It concatenates `s` with itself: `s + s`. This doubled string contains every possible rotation of `s` as a substring. For example, `"abcde" + "abcde" = "abcdeabcde"` contains `"cdeab"` as a substring.
3. **Find:** It checks if `goal` exists anywhere in `s + s` using `.find()`. If found, `goal` is a valid rotation.

Time complexity is $O(N)$ with an efficient string search and space complexity is $O(N)$ for the concatenated string.

## Algorithm
1. Initialize state variables / data structure (**Primitive Types**).
2. Process elements sequentially using **Mathematical Simulation & Modular Arithmetic**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcde", goal = "cdeab"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Rotating `s` to the left by 2 positions moves `"ab"` to the end, resulting in `"cdeab"`, which is equal to `goal`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
C++, JavaScript

## Source Code
- [solution.cpp](./solution.cpp)
- [solution.js](./solution.js)


### C++
```cpp
class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length())
            return false;

        return (s + s).find(goal) != string::npos;
    }
};
```

### JavaScript
```javascript
var rotateString = function(s, goal) {
    if (s.length !== goal.length) {
        return false;
    }

    return (s + s).includes(goal);
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotate-string/)
