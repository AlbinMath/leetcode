# LeetCode 1972: First and Last Call On the Same Day

**LeetCode Problem #1972 — First and Last Call On the Same Day**
Solve LeetCode First and Last Call On the Same Day using C++ and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | First and Last Call On the Same Day |
| LeetCode | #1972 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given an  m x n  matrix of characters  boxGrid  representing a side-view of a box. Each cell of the box is one of the following:

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
1. **Apply Gravity (rightward):** Before rotating, simulate gravity in each row by moving stones as far right as possible, stopping at obstacles or the edge.
2. **Rotate 90° Clockwise:** Create a new matrix where `result[j][m-1-i] = box[i][j]`.

Time complexity is $O(M \times N)$ and space complexity is $O(M \times N)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **First and Last Call On the Same Day**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Database / SQL**

## Topics
- Database
- SQL
- Data Aggregation

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Database / SQL**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2043. Simple Bank System](../2043-cyclically-rotating-a-grid/)
- [10. Regular Expression Matching](../0010-regular-expression-matching/)
- [12. Integer to Roman](../0012-integer-to-roman/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotating-the-box/)
