# LeetCode 3106: Lexicographically Smallest String After Operations With Constraint

**LeetCode Problem #3106 — Lexicographically Smallest String After Operations With Constraint**
Solve LeetCode Lexicographically Smallest String After Operations With Constraint using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest String After Operations With Constraint |
| LeetCode | #3106 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` and an integer `k`.

Define a function `distance(s_1, s_2)` between two strings `s_1` and `s_2` of the same length `n` as:

The** sum** of the **minimum distance** between `s_1[i]` and `s_2[i]` when the characters from `'a'` to `'z'` are placed in a **cyclic** order, for all `i` in the range `[0, n - 1]`.

For example, `distance("ab", "cd") == 4`, and `distance("a", "z") == 1`.

You can **change** any letter of `s` to **any** other lowercase English letter, **any** number of times.

Return a string denoting the ** lexicographically smallest ** string `t` you can get after some changes, such that `distance(s, t) <= k`.

## Constraints
- `1 <= s.length <= 100`
- `0 <= k <= 2000`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "zbbz", k = 3`
- **Output:** `"aaaz"`
- **Explanation:** Change `s` to `"aaaz"`. The distance between `"zbbz"` and `"aaaz"` is equal to `k = 3`.

### Example 2
- **Input:** `s = "xaxcd", k = 4`
- **Output:** `"aawcd"`
- **Explanation:** The distance between "xaxcd" and "aawcd" is equal to k = 4.

### Example 3
- **Input:** `s = "lol", k = 0`
- **Output:** `"lol"`
- **Explanation:** It's impossible to change any character as `k = 0`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Lexicographically Smallest String After Operations With Constraint**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "zbbz", k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"aaaz"`.
4. **Verification:** Change `s` to `"aaaz"`. The distance between `"zbbz"` and `"aaaz"` is equal to `k = 3`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var getSmallestString = function(s, k) {
    let result = "";

    for (let ch of s) {
        const current = ch.charCodeAt(0) - 97;
        const cost = Math.min(current, 26 - current);

        if (k >= cost) {
            result += 'a';
            k -= cost;
        } else {
            result += String.fromCharCode(97 + current - k);
            k = 0;
        }
    }

    return result;
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
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)
- [2734. Lexicographically Smallest String After Substring Operation](../../2501-3000/2734-lexicographically-smallest-string-after-substring-operation/)
- [3216. Lexicographically Smallest String After a Swap](../../3001-3500/3216-lexicographically-smallest-string-after-a-swap/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/)
