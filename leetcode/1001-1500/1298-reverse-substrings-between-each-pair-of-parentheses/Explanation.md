# LeetCode 1190: Reverse Substrings Between Each Pair of Parentheses

**LeetCode Problem #1190 — Reverse Substrings Between Each Pair of Parentheses**
Solve LeetCode Reverse Substrings Between Each Pair of Parentheses using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Substrings Between Each Pair of Parentheses |
| LeetCode | #1190 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given a string  s  that consists of lower case English letters and brackets.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **Stack of Strings**.

1. **Maintain `current`:** A string being built from the current nesting level.
2. **On `(`:** Push `current` onto the stack (save progress) and reset `current` to empty.
3. **On `)`:** Reverse `current`, then prepend the string from the top of the stack (pop it). This effectively reverses the content within the parentheses and concatenates it with the content before the opening parenthesis.
4. **On any other character:** Append it to `current`.
5. After processing all characters, `current` holds the final result.

Time complexity is $O(N^2)$ in the worst case (due to reversals) and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Reverse Substrings Between Each Pair of Parentheses**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3918. Sum of Primes Between Number and Its Reverse](../../4001-4500/4297-sum-of-primes-between-number-and-its-reverse/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [116. Populating Next Right Pointers in Each Node](../../0001-0500/0116-populating-next-right-pointers-in-each-node/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)
