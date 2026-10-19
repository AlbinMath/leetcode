# LeetCode 2452: Words Within Two Edits of Dictionary

**LeetCode Problem #2452 — Words Within Two Edits of Dictionary**
Solve LeetCode Words Within Two Edits of Dictionary using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Words Within Two Edits of Dictionary |
| LeetCode | #2452 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
You are given two string arrays,  queries  and  dictionary . All words in each array comprise of lowercase English letters and have the same length.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Words Within Two Edits of Dictionary**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [884. Uncommon Words from Two Sentences](../0920-uncommon-words-from-two-sentences/)
- [1880. Check if Word Equals Summation of Two Words](../2010-check-if-word-equals-summation-of-two-words/)
- [1. Two Sum](../0001-two-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/words-within-two-edits-of-dictionary/)
