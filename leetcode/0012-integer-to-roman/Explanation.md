# LeetCode 12: Integer to Roman

**LeetCode Problem #12 — Integer to Roman**
Solve LeetCode Integer to Roman using JavaScript and Heap. This solution finds the optimal result using Priority Queue Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Integer to Roman |
| LeetCode | #12 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Priority Queue Selection |
| Data Structure | Min/Max Heap |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Seven different symbols represent Roman numerals with the following values:

## Key Insight
Leverage **Heap** with **Min/Max Heap** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a greedy approach to convert the integer by repeatedly subtracting the largest possible Roman numeral values.

1. **Mapping Values and Symbols:** It defines two parallel arrays: `values` and `symbols`. These arrays map the numerical values to their corresponding Roman numeral strings. Crucially, this list includes the special subtraction cases (like `900 -> CM`, `400 -> CD`, `90 -> XC`, `40 -> XL`, `9 -> IX`, and `4 -> IV`) so they can be treated just like normal numerals. They are arranged in descending order from largest (`1000`) to smallest (`1`).
2. **Greedy Subtraction:** It initializes an empty `result` string. Then, it loops through the `values` array.
3. For each value, it uses a `while (num >= values[i])` loop. As long as the remaining `num` is greater than or equal to the current Roman value, it:
   - Appends the corresponding Roman `symbol` to the `result` string.
   - Subtracts the `value` from `num`.
4. Because the values are checked from largest to smallest, the algorithm guarantees the correct Roman numeral format (e.g., it will always use `M` before it attempts to use `CM` or `D`).
5. **Completion:** The loop continues until `num` is reduced to 0, at which point the complete Roman numeral string is returned.

The time complexity is $O(1)$ because the number of values is fixed (13 symbols) and the `while` loop will run at most a constant number of times (since the maximum input is 3999). The space complexity is also $O(1)$ since the arrays are of fixed size.

## Algorithm
1. Initialize state variables / data structure (**Min/Max Heap**).
2. Process elements sequentially using **Priority Queue Selection**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Integer to Roman**. Applying **Priority Queue Selection** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [13. Roman to Integer](../0013-roman-to-integer/)
- [7. Reverse Integer](../0007-reverse-integer/)
- [3236. CEO Subordinate Hierarchy](../3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/integer-to-roman/)
