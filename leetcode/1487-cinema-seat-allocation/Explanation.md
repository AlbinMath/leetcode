# LeetCode 1487: Making File Names Unique

**LeetCode Problem #1487 — Making File Names Unique**
Solve LeetCode Making File Names Unique using C++ and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Making File Names Unique |
| LeetCode | #1487 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
A cinema has  n  rows of seats, numbered from 1 to  n . Each row has 10 seats, numbered from 1 to 10.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Bitmasks** for efficient seat tracking.

1. **Bitmask per Row:** For each reserved seat, set the corresponding bit in a bitmask for that row. Only rows with reservations are stored in a hash map.
2. **Unreserved Rows:** Rows without any reservations can always fit 2 groups (left: seats 2–5, right: seats 6–9). Contribute `2 * (n - reservedRows)`.
3. **Reserved Rows:** For each row with reservations, check three possible group positions using bitwise AND:
   - **Left** (seats 2–5): bits 2,3,4,5 must be free.
   - **Middle** (seats 4–7): bits 4,5,6,7 must be free.
   - **Right** (seats 6–9): bits 6,7,8,9 must be free.
   - If both left and right fit → 2 groups. Else if any one fits → 1 group.

Time complexity is $O(R)$ where $R$ is the number of reserved seats, and space complexity is $O(R)$.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Making File Names Unique**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
- [10. Regular Expression Matching](../0010-regular-expression-matching/)
- [12. Integer to Roman](../0012-integer-to-roman/)
- [13. Roman to Integer](../0013-roman-to-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cinema-seat-allocation/)
