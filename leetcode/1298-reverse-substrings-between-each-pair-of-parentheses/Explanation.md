# LeetCode 1298: Maximum Candies You Can Get from Boxes

**LeetCode Problem #1298 — Maximum Candies You Can Get from Boxes**
Solve LeetCode Maximum Candies You Can Get from Boxes using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Candies You Can Get from Boxes |
| LeetCode | #1298 |
| Difficulty | Hard |
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
Consider the standard input for **Maximum Candies You Can Get from Boxes**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

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
- [7. Reverse Integer](../0007-reverse-integer/)
- [20. Valid Parentheses](../0020-valid-parentheses/)
- [150. Evaluate Reverse Polish Notation](../0150-evaluate-reverse-polish-notation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)
