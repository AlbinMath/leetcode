# LeetCode 1186: Maximum Subarray Sum with One Deletion

**LeetCode Problem #1186 — Maximum Subarray Sum with One Deletion**
Solve LeetCode Maximum Subarray Sum with One Deletion using C++ and Database / SQL. This solution finds the optimal result using SQL Query / Relational Join & Grouping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Subarray Sum with One Deletion |
| LeetCode | #1186 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | SQL Query / Relational Join & Grouping |
| Data Structure | Relational Table |
| Pattern | Database / SQL |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are two kinds of threads:  oxygen  and  hydrogen . Your goal is to group these threads to form water molecules.

## Key Insight
Leverage **Database / SQL** with **Relational Table** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **mutex** and **condition variable** for thread synchronization.

1. **Shared State:** `hydrogenCount` and `oxygenCount` track how many of each have been released in the current molecule.
2. **Hydrogen Thread:**
   - Waits until `hydrogenCount < 2` (room for more hydrogen in the current molecule).
   - Increments `hydrogenCount` and releases the hydrogen.
   - If `hydrogenCount == 2`, notifies all waiting threads (the oxygen thread can now proceed).
3. **Oxygen Thread:**
   - Waits until both hydrogens are ready (`hydrogenCount == 2`) and no oxygen has been released yet (`oxygenCount == 0`).
   - Increments `oxygenCount` and releases the oxygen.
   - Resets both counters to `0` and notifies all threads, allowing the next molecule to start forming.

This ensures every water molecule has exactly 2 H atoms and 1 O atom before any thread proceeds.

## Algorithm
1. Initialize state variables / data structure (**Relational Table**).
2. Process elements sequentially using **SQL Query / Relational Join & Grouping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Maximum Subarray Sum with One Deletion**. Applying **SQL Query / Relational Join & Grouping** yields the target result step by step.

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
- [1968. Array With Elements Not Equal to Average of Neighbors](../1968-maximum-building-height/)
- [10. Regular Expression Matching](../0010-regular-expression-matching/)
- [12. Integer to Roman](../0012-integer-to-roman/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/building-h2o/)
