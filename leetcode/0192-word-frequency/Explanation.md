# LeetCode 192: Word Frequency

**LeetCode Problem #192 — Word Frequency**
Solve LeetCode Word Frequency using Shell and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Word Frequency |
| LeetCode | #192 |
| Difficulty | Medium |
| Language | Shell |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Write a bash script to calculate the  frequency  of each word in a text file  words.txt .

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The solution chains four Unix commands together using pipes:
1. `tr -s ' ' '\n'`: Translates (replaces) all spaces with newlines, splitting the text into one word per line. The `-s` flag squeezes consecutive spaces into a single newline.
2. `sort`: Sorts the words alphabetically. This is necessary for the next step.
3. `uniq -c`: Counts consecutive identical lines (which is why sorting first is essential), producing a count followed by the word.
4. `sort -nr`: Sorts the output numerically (`-n`) in reverse order (`-r`), putting the most frequent words first.
5. `awk '{print $2, $1}'`: Swaps the column order so the word comes before the count (since `uniq -c` outputs count first).

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Word Frequency**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
Shell

## Source Code
- [solution.sh](./solution.sh)

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
- [2099. Find Subsequence of Length K With the Largest Sum](../2099-number-of-strings-that-appear-as-substrings-in-word/)
- [3225. Maximum Score From Grid Operations](../3225-length-of-longest-subarray-with-at-most-k-frequency/)
- [3275. K-th Nearest Obstacle Queries](../3275-minimum-number-of-pushes-to-type-word-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/word-frequency/)
