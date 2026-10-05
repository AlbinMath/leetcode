# LeetCode 9: Palindrome Number

**LeetCode Problem #9 — Palindrome Number**
Solve LeetCode Palindrome Number using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence / Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Palindrome Number |
| LeetCode | #9 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence / Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
Given an integer  x , return  true  if  x  is a   palindrome  , and  false  otherwise.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
If the number is negative, it cannot be a palindrome (due to the minus sign), so we return `False`.
We store the `original` number and create a `reversed_num` variable initialized to `0`.
Using a `while` loop, we extract the last digit of the number using modulo 10 (`x % 10`) and append it to `reversed_num` by multiplying the current `reversed_num` by 10 and adding the digit.
Then, we remove the last digit from `x` using integer division (`x //= 10`).
Finally, we check if the `original` number is equal to the `reversed_num`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence / Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Palindrome Number**. Applying **Two Pointer Convergence / Scanning** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2559. Count Vowel Strings in Ranges](../2559-maximum-number-of-non-overlapping-palindrome-substrings/)
- [17. Letter Combinations of a Phone Number](../0017-letter-combinations-of-a-phone-number/)
- [586. Customer Placing the Largest Number of Orders](../0586-customer-placing-the-largest-number-of-orders/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/palindrome-number/)
