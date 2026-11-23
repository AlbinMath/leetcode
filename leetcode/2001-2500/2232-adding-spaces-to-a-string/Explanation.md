# LeetCode 2109: Adding Spaces to a String

**LeetCode Problem #2109 — Adding Spaces to a String**
Solve LeetCode Adding Spaces to a String using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Adding Spaces to a String |
| LeetCode | #2109 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string `s` and a **0-indexed** integer array `spaces` that describes the indices in the original string where spaces will be added. Each space should be inserted **before** the character at the given index.

For example, given `s = "EnjoyYourCoffee"` and `spaces = [5, 9]`, we place spaces before `'Y'` and `'C'`, which are at indices `5` and `9` respectively. Thus, we obtain `"Enjoy ** Y **our **C** offee"`.

Return** ***the modified string **after** the spaces have been added.*

## Constraints
- `1 <= s.length <= 3 * 10^5`
- `s` consists only of lowercase and uppercase English letters.
- `1 <= spaces.length <= 3 * 10^5`
- `0 <= spaces[i] <= s.length - 1`
- All the values of `spaces` are **strictly increasing**.

## Examples
### Example 1
- **Input:** `s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]`
- **Output:** `"Leetcode Helps Me Learn"`
- **Explanation:** The indices 8, 13, and 15 correspond to the underlined characters in "Leetcode

### Example 2
- **Input:** `s = "icodeinpython", spaces = [1,5,7,9]`
- **Output:** `"i code in py thon"`
- **Explanation:** The indices 1, 5, 7, and 9 correspond to the underlined characters in "i

### Example 3
- **Input:** `s = "spacing", spaces = [0,1,2,3,4,5,6]`
- **Output:** `" s p a c i n g"`
- **Explanation:** We are also able to place spaces before the first character of the string.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Adding Spaces to a String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"Leetcode Helps Me Learn"`.
4. **Verification:** The indices 8, 13, and 15 correspond to the underlined characters in "Leetcode

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
var addSpaces = function(s, spaces) {
    let result = "";
    let j = 0;

    for (let i = 0; i < s.length; i++) {
        if (j < spaces.length && i === spaces[j]) {
            result += " ";
            j++;
        }

        result += s[i];
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/adding-spaces-to-a-string/)
