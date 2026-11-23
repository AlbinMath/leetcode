# LeetCode 1996: The Number of Weak Characters in the Game

**LeetCode Problem #1996 — The Number of Weak Characters in the Game**
Solve LeetCode The Number of Weak Characters in the Game using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Number of Weak Characters in the Game |
| LeetCode | #1996 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You are playing a game that contains multiple characters, and each of the characters has  two  main properties:  attack  and  defense . You are given a 2D integer array  properties  where  properties[i] = [attack i , defense i ]  represents the properties of the  i th   character in the game.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **The Number of Weak Characters in the Game**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)

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
- [2974. Minimum Number Game](../3226-minimum-number-game/)
- [1358. Number of Substrings Containing All Three Characters](../1460-number-of-substrings-containing-all-three-characters/)
- [1898. Maximum Number of Removable Characters](../2027-maximum-number-of-removable-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/)
