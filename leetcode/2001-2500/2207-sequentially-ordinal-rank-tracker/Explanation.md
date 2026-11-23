# LeetCode 2102: Sequentially Ordinal Rank Tracker

**LeetCode Problem #2102 — Sequentially Ordinal Rank Tracker**
Solve LeetCode Sequentially Ordinal Rank Tracker using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sequentially Ordinal Rank Tracker |
| LeetCode | #2102 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
A scenic location is represented by its  name  and attractiveness  score , where  name  is a  unique  string among all locations and  score  is an integer. Locations can be ranked from the best to the worst. The  higher  the score, the better the location. If the scores of two locations are equal, then the location with the  lexicographically smaller  name is better.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Sequentially Ordinal Rank Tracker**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
Python

## Source Code
- [solution.py](./solution.py)

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
- [178. Rank Scores](../../0001-0500/0178-rank-scores/)
- [1331. Rank Transform of an Array](../../1001-1500/1256-rank-transform-of-an-array/)
- [1366. Rank Teams by Votes](../../1001-1500/1483-rank-teams-by-votes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sequentially-ordinal-rank-tracker/)
