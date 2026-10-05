# LeetCode 804: Unique Morse Code Words

**LeetCode Problem #804 — Unique Morse Code Words**
Solve LeetCode Unique Morse Code Words using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unique Morse Code Words |
| LeetCode | #804 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
An integer  x  is a  good  if after rotating each digit individually by 180 degrees, we get a valid number that is different from  x . Each digit must be rotated - we cannot choose to leave it alone.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code checks each number from `1` to `n` individually.

1. For each number, it extracts digits one by one using `x % 10` and `x /= 10`.
2. It tracks two flags:
   - `valid`: Remains `true` unless a digit `3`, `4`, or `7` is found (which makes the number invalid after rotation).
   - `different`: Set to `true` if any digit is `2`, `5`, `6`, or `9` (meaning the rotated number differs from the original).
3. A number is "good" only if `valid && different` — it must be valid after rotation AND actually change.

Time complexity is $O(N \log N)$ (each number has at most $\log_{10}(N)$ digits) and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Unique Morse Code Words**. Applying **Modified Binary Search** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [33. Search in Rotated Sorted Array](../0033-search-in-rotated-sorted-array/)
- [153. Find Minimum in Rotated Sorted Array](../0153-find-minimum-in-rotated-sorted-array/)
- [154. Find Minimum in Rotated Sorted Array II](../0154-find-minimum-in-rotated-sorted-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rotated-digits/)
