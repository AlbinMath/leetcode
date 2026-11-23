# LeetCode 1967: Number of Strings That Appear as Substrings in Word

**LeetCode Problem #1967 — Number of Strings That Appear as Substrings in Word**
Solve LeetCode Number of Strings That Appear as Substrings in Word using Kotlin and Linked List. This solution finds the optimal result using Pointer Traversal & Node Manipulation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Strings That Appear as Substrings in Word |
| LeetCode | #1967 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Pointer Traversal & Node Manipulation |
| Data Structure | Linked List |
| Pattern | Linked List |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an array of strings  patterns  and a string  word , return  the  number  of strings in   patterns   that exist as a  substring  in   word .

## Key Insight
Leverage **Linked List** with **Linked List** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code iterates through each pattern and checks if it exists as a substring of `word` using the built-in `contains`/`indexOf` method. Count and return the matches.

Time complexity is $O(P \times W)$ where $P$ is total pattern length and $W$ is word length, and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Linked List**).
2. Process elements sequentially using **Pointer Traversal & Node Manipulation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Number of Strings That Appear as Substrings in Word**. Applying **Pointer Traversal & Node Manipulation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Linked List**

## Topics
- Linked List
- Two Pointers

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)

## Why This Works
By utilizing **Linked List**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1358. Number of Substrings Containing All Three Characters](../1460-number-of-substrings-containing-all-three-characters/)
- [1513. Number of Substrings With Only 1s](../1636-number-of-substrings-with-only-1s/)
- [1520. Maximum Number of Non-Overlapping Substrings](../1644-maximum-number-of-non-overlapping-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/)
