# LeetCode 1117: Building H2O

**LeetCode Problem #1117 — Building H2O**
Solve LeetCode Building H2O using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Building H2O |
| LeetCode | #1117 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
There are two kinds of threads:  oxygen  and  hydrogen . Your goal is to group these threads to form water molecules.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

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
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Building H2O**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1840. Maximum Building Height](../1968-maximum-building-height/)
- [5. Longest Palindromic Substring](../0005-longest-palindromic-substring/)
- [6. Zigzag Conversion](../0006-zigzag-conversion/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/building-h2o/)
