# LeetCode 839: Similar String Groups

**LeetCode Problem #839 — Similar String Groups**
Solve LeetCode Similar String Groups using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Similar String Groups |
| LeetCode | #839 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Two strings,  X  and  Y , are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string  X .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Similar String Groups**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

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
- [1750. Minimum Length of String After Deleting Similar Ends](../1850-minimum-length-of-string-after-deleting-similar-ends/)
- [2138. Divide a String Into Groups of Size k](../2260-divide-a-string-into-groups-of-size-k/)
- [2267.  Check if There Is a Valid Parentheses String Path](../2349-check-if-there-is-a-valid-parentheses-string-path/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/similar-string-groups/)
