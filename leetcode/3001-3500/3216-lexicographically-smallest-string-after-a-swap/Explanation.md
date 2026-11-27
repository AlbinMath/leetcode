# LeetCode 3216: Lexicographically Smallest String After a Swap

**LeetCode Problem #3216 — Lexicographically Smallest String After a Swap**
Solve LeetCode Lexicographically Smallest String After a Swap using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest String After a Swap |
| LeetCode | #3216 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s` containing only digits, return the lexicographically smallest string that can be obtained after swapping **adjacent** digits in `s` with the same **parity** at most **once**.

Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

## Constraints
- `2 <= s.length <= 100`
- `s` consists only of digits.

## Examples
### Example 1
- **Input:** `s = "45320"`
- **Output:** `"43520"`
- **Explanation:** `s[1] == '5'` and `s[2] == '3'` both have the same parity, and swapping them results in the lexicographically smallest string.

### Example 2
- **Input:** `s = "001"`
- **Output:** `"001"`
- **Explanation:** There is no need to perform a swap because `s` is already the lexicographically smallest.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Lexicographically Smallest String After a Swap**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "45320"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"43520"`.
4. **Verification:** `s[1] == '5'` and `s[2] == '3'` both have the same parity, and swapping them results in the lexicographically smallest string.

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
var getSmallestString = function(s) {
    const arr = s.split('');

    for (let i = 0; i < arr.length - 1; i++) {
        const a = Number(arr[i]);
        const b = Number(arr[i + 1]);
        if (a % 2 === b % 2 && a > b) {
            [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
            break;
        }
    }

    return arr.join('');
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
- [3106. Lexicographically Smallest String After Operations With Constraint](../../3001-3500/3106-lexicographically-smallest-string-after-operations-with-constraint/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/)
