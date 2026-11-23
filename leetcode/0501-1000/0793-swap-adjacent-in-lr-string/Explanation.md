# LeetCode 777: Swap Adjacent in LR String

**LeetCode Problem #777 — Swap Adjacent in LR String**
Solve LeetCode Swap Adjacent in LR String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Swap Adjacent in LR String |
| LeetCode | #777 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
In a string composed of  &#39;L&#39; ,  &#39;R&#39; , and  &#39;X&#39;  characters, like  "RXXLRXRXL" , a move consists of either replacing one occurrence of  "XL"  with  "LX" , or replacing one occurrence of  "RX"  with  "XR" . Given the starting string  start  and the ending string  result , return  True  if and only if there exists a sequence of moves to transform  start  to  result .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Swap Adjacent in LR String**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1047. Remove All Adjacent Duplicates In String](../../1001-1500/1128-remove-all-adjacent-duplicates-in-string/)
- [1209. Remove All Adjacent Duplicates in String II](../../1001-1500/1320-remove-all-adjacent-duplicates-in-string-ii/)
- [1790. Check if One String Swap Can Make Strings Equal](../../1501-2000/1915-check-if-one-string-swap-can-make-strings-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/swap-adjacent-in-lr-string/)
