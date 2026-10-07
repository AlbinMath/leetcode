# LeetCode 1345: Jump Game IV

**LeetCode Problem #1345 — Jump Game IV**
Solve LeetCode Jump Game IV using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Jump Game IV |
| LeetCode | #1345 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an array of integers  arr , you are initially positioned at the first index of the array.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The code uses **BFS** for shortest path.

1. **Group by Value:** Build a map from each value to all indices containing it.
2. **BFS:** Start from index `0`. Each level of BFS represents one jump. For each index, explore three types of neighbors: `i-1`, `i+1`, and all indices with the same value.
3. **Optimization:** After processing all indices of a value, erase that value from the map. This prevents revisiting the same group and ensures $O(N)$ total work.
4. Return the number of BFS levels when reaching index `n-1`.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Jump Game IV**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [45. Jump Game II](../0045-jump-game-ii/)
- [55. Jump Game](../0055-jump-game/)
- [550. Game Play Analysis IV](../1182-game-play-analysis-iv/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/jump-game-iv/)
