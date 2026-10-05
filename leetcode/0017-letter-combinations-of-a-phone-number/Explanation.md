# LeetCode 17: Letter Combinations of a Phone Number

**LeetCode Problem #17 — Letter Combinations of a Phone Number**
Solve LeetCode Letter Combinations of a Phone Number using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Letter Combinations of a Phone Number |
| LeetCode | #17 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Search |
| Data Structure | Recursion Tree / Array |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given a string containing digits from  2-9  inclusive, return all possible letter combinations that the number could represent. Return the answer in  any order .

## Key Insight
Leverage **Backtracking** with **Recursion Tree / Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Backtracking** to explore all possible letter combinations.

1. **Base Case:** If the input string is empty, it returns an empty array immediately.
2. **Digit-to-Letter Map:** A `map` object stores the mapping from each digit (`'2'` through `'9'`) to its corresponding letters.
3. **Backtracking Function:** The recursive function `backtrack(index, current)` builds one combination at a time:
   - **Termination:** When `index` equals the length of `digits`, the current combination `current` is complete and is pushed to the `result` array.
   - **Branching:** Otherwise, it looks up the letters for `digits[index]` and iterates over each letter. For each letter, it recurses with `index + 1` and `current + letter`, which extends the current combination by one character.
4. The function is initially called with `backtrack(0, "")`, starting from the first digit with an empty string.

Since each digit maps to at most 4 letters, the time complexity is $O(4^N)$ where $N$ is the number of digits, and space complexity is $O(N)$ for the recursion stack.

## Algorithm
1. Initialize state variables / data structure (**Recursion Tree / Array**).
2. Process elements sequentially using **Backtracking Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Letter Combinations of a Phone Number**. Applying **Backtracking Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [9. Palindrome Number](../0009-palindrome-number/)
- [193. Valid Phone Numbers](../0193-valid-phone-numbers/)
- [586. Customer Placing the Largest Number of Orders](../0586-customer-placing-the-largest-number-of-orders/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
