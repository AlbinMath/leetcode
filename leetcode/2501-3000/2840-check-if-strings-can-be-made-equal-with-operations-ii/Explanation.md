# LeetCode 2840: Check if Strings Can be Made Equal With Operations II

**LeetCode Problem #2840 — Check if Strings Can be Made Equal With Operations II**
Solve LeetCode Check if Strings Can be Made Equal With Operations II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Strings Can be Made Equal With Operations II |
| LeetCode | #2840 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `s1` and `s2`, both of length `n`, consisting of **lowercase** English letters.

You can apply the following operation on **any** of the two strings **any** number of times:

Choose any two indices `i` and `j` such that `i < j` and the difference `j - i` is **even**, then **swap** the two characters at those indices in the string.

Return `true`* if you can make the strings *`s1`* and *`s2`* equal, and *`false`* otherwise*.

## Constraints
- `n == s1.length == s2.length`
- `1 <= n <= 10^5`
- `s1` and `s2` consist only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s1 = "abcdba", s2 = "cabdab"`
- **Output:** `true`
- **Explanation:** We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

### Example 2
- **Input:** `s1 = "abe", s2 = "bea"`
- **Output:** `false`
- **Explanation:** It is not possible to make the two strings equal.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check if Strings Can be Made Equal With Operations II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s1 = "abcdba", s2 = "cabdab"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.

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
var checkStrings = function(s1, s2) {
    const even = new Array(26).fill(0);
    const odd = new Array(26).fill(0);

    for (let i = 0; i < s1.length; i++) {
        const index1 = s1.charCodeAt(i) - 97;
        const index2 = s2.charCodeAt(i) - 97;

        if (i % 2 === 0) {
            even[index1]++;
            even[index2]--;
        } else {
            odd[index1]++;
            odd[index2]--;
        }
    }

    for (let i = 0; i < 26; i++) {
        if (even[i] !== 0 || odd[i] !== 0) {
            return false;
        }
    }

    return true;
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
- [1790. Check if One String Swap Can Make Strings Equal](../../1501-2000/1790-check-if-one-string-swap-can-make-strings-equal/)
- [2018. Check if Word Can Be Placed In Crossword](../../2001-2500/2018-check-if-word-can-be-placed-in-crossword/)
- [2116. Check if a Parentheses String Can Be Valid](../../2001-2500/2116-check-if-a-parentheses-string-can-be-valid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/)
