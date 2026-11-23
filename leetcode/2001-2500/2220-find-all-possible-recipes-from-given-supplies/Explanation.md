# LeetCode 2115: Find All Possible Recipes from Given Supplies

**LeetCode Problem #2115 — Find All Possible Recipes from Given Supplies**
Solve LeetCode Find All Possible Recipes from Given Supplies using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find All Possible Recipes from Given Supplies |
| LeetCode | #2115 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have information about  n  different recipes. You are given a string array  recipes  and a 2D string array  ingredients . The  i th   recipe has the name  recipes[i] , and you can  create  it if you have  all  the needed ingredients from  ingredients[i] . A recipe can also be an ingredient for  other  recipes, i.e.,  ingredients[i]  may contain a string that is in  recipes .

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
We iterate through the input using **In-Place Array Traversal & Index Mapping**. By maintaining state efficiently in a **Array**, we eliminate redundant operations and process each element in optimal time.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Find All Possible Recipes from Given Supplies**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)

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
- [894. All Possible Full Binary Trees](../../0501-1000/0930-all-possible-full-binary-trees/)
- [1162. As Far from Land as Possible](../../1001-1500/1117-as-far-from-land-as-possible/)
- [1575. Count All Possible Routes](../../1501-2000/1680-count-all-possible-routes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/)
