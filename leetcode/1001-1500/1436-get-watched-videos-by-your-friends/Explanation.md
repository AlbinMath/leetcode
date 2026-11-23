# LeetCode 1311: Get Watched Videos by Your Friends

**LeetCode Problem #1311 — Get Watched Videos by Your Friends**
Solve LeetCode Get Watched Videos by Your Friends using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Get Watched Videos by Your Friends |
| LeetCode | #1311 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
There are  n  people, each person has a unique  id  between  0  and  n-1 . Given the arrays  watchedVideos  and  friends , where  watchedVideos[i]  and  friends[i]  contain the list of watched videos and the list of friends respectively for the person with  id = i .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
We iterate through the input using **Complement Lookup / Hash Table Frequency**. By maintaining state efficiently in a **Dictionary / Hash Map**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Get Watched Videos by Your Friends**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
- [864. Shortest Path to Get All Keys](../../0501-1000/0895-shortest-path-to-get-all-keys/)
- [1208. Get Equal Substrings Within Budget](../../1001-1500/1321-get-equal-substrings-within-budget/)
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1424-maximum-candies-you-can-get-from-boxes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/get-watched-videos-by-your-friends/)
