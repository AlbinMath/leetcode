# LeetCode 3718: Smallest Missing Multiple of K

**LeetCode Problem #3718 — Smallest Missing Multiple of K**
Solve LeetCode Smallest Missing Multiple of K using C# and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Missing Multiple of K |
| LeetCode | #3718 |
| Difficulty | Easy |
| Language | C# |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
Given an integer array  nums  and an integer  k , return the  smallest positive multiple  of  k  that is  missing  from  nums .

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a `HashSet` to efficiently check for the presence of numbers in $O(1)$ time.
1. First, it converts the `nums` array into a `HashSet<int>` called `set`. This allows us to quickly look up whether a number exists in the array without having to scan the entire array every time.
2. It initializes a variable `multiple` to the first multiple, which is `k`.
3. It uses a `while` loop to continuously check if `set` contains the current `multiple`.
   - If it does, we increment the `multiple` by `k` to check the next multiple (`2k`, `3k`, etc.).
4. The loop stops as soon as it finds a `multiple` that is **not** in the `HashSet`.
5. Finally, it returns that missing `multiple`.

This approach is highly efficient. Converting the array to a HashSet takes $O(N)$ time (where $N$ is the number of elements in `nums`), and the while loop takes at most $O(N)$ steps because there can be at most $N$ multiples of $k$ present in the array. Therefore, the overall time complexity is $O(N)$ and the space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Smallest Missing Multiple of K**. Applying **Prefix Sum Precomputation** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
C#

## Source Code
- [solution.cs](./solution.cs)

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)
- [23. Merge k Sorted Lists](../0023-merge-k-sorted-lists/)
- [25. Reverse Nodes in k-Group](../0025-reverse-nodes-in-k-group/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k/)
