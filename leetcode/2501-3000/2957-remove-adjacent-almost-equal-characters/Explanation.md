# LeetCode 2957: Remove Adjacent Almost-Equal Characters

**LeetCode Problem #2957 — Remove Adjacent Almost-Equal Characters**
Solve LeetCode Remove Adjacent Almost-Equal Characters using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Adjacent Almost-Equal Characters |
| LeetCode | #2957 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string `word`.

In one operation, you can pick any index `i` of `word` and change `word[i]` to any lowercase English letter.

Return *the **minimum** number of operations needed to remove all adjacent **almost-equal** characters from* `word`.

Two characters `a` and `b` are **almost-equal** if `a == b` or `a` and `b` are adjacent in the alphabet.

## Constraints
- `1 <= word.length <= 100`
- `word` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `word = "aaaaa"`
- **Output:** `2`
- **Explanation:** We can change word into "a

### Example 2
- **Input:** `word = "abddez"`
- **Output:** `2`
- **Explanation:** We can change word into "

### Example 3
- **Input:** `word = "zyxyxyz"`
- **Output:** `3`
- **Explanation:** We can change word into "z

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Remove Adjacent Almost-Equal Characters**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "aaaaa"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can change word into "a

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var removeAlmostEqualCharacters = function(word) {
    let count = 0;

    for (let i = 0; i < word.length - 1; i++) {
        let diff = Math.abs(
            word.charCodeAt(i) - word.charCodeAt(i + 1)
        );

        if (diff <= 1) {
            count++;
            i++;
        }
    }

    return count;
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
- [1624. Largest Substring Between Two Equal Characters](../../1501-2000/1624-largest-substring-between-two-equal-characters/)
- [1897. Redistribute Characters to Make All Strings Equal](../../1501-2000/1897-redistribute-characters-to-make-all-strings-equal/)
- [1941. Check if All Characters Have Equal Number of Occurrences](../../1501-2000/1941-check-if-all-characters-have-equal-number-of-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-adjacent-almost-equal-characters/)
