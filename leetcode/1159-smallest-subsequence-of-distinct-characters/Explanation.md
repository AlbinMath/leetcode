# LeetCode 1081: Smallest Subsequence of Distinct Characters

**LeetCode Problem #1081 — Smallest Subsequence of Distinct Characters**
Solve LeetCode Smallest Subsequence of Distinct Characters using C++ and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Subsequence of Distinct Characters |
| LeetCode | #1081 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given a string  s , return  the    lexicographically smallest     subsequence    of   s   that contains all the distinct characters of   s   exactly once .

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
The code uses a **Monotonic Stack** (greedy) approach.

1. **Last Occurrence:** It records the last index of each character in the string.
2. **Used Array:** Tracks which characters are currently in the result to avoid duplicates.
3. **Build the Result String:** For each character `c` at index `i`:
   - If `c` is already in the result (`used[c]` is true), skip it.
   - While the last character in the result (`st.back()`) is greater than `c` AND that character appears again later (`last[st.back()] > i`): remove it from the result and mark it as unused. This ensures we keep the smallest characters first when possible.
   - Add `c` to the result and mark it as used.
4. The result is the lexicographically smallest subsequence containing all distinct characters.

Time complexity is $O(N)$ and space complexity is $O(1)$ (at most 26 characters in the stack).

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest Subsequence of Distinct Characters**. Applying **Monotonic Stack Filtering** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [1876. Substrings of Size Three with Distinct Characters](../1987-substrings-of-size-three-with-distinct-characters/)
- [3. Longest Substring Without Repeating Characters](../0003-longest-substring-without-repeating-characters/)
- [115. Distinct Subsequences](../0115-distinct-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)
