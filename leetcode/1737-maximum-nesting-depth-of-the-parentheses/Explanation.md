# LeetCode 1614: Maximum Nesting Depth of the Parentheses

**LeetCode Problem #1614 — Maximum Nesting Depth of the Parentheses**
Solve LeetCode Maximum Nesting Depth of the Parentheses using Java and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Nesting Depth of the Parentheses |
| LeetCode | #1614 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a  valid parentheses string   s , return the  nesting depth  of    s . The nesting depth is the  maximum  number of nested parentheses.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code tracks the current `depth` using a counter. For each `(`, increment depth and update `maxDepth`. For each `)`, decrement depth. The maximum value of `depth` during the scan is the answer.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Nesting Depth of the Parentheses**. Applying **Stack Push / Pop Parsing** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Java

## Source Code
- [solution.java](./solution.java)

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
- [1111. Maximum Nesting Depth of Two Valid Parentheses Strings](../1208-maximum-nesting-depth-of-two-valid-parentheses-strings/)
- [20. Valid Parentheses](../0020-valid-parentheses/)
- [22. Generate Parentheses](../0022-generate-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)
