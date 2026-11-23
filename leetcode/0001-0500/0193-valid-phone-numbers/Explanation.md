# LeetCode 193: Valid Phone Numbers

**LeetCode Problem #193 — Valid Phone Numbers**
Solve LeetCode Valid Phone Numbers using Shell and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid Phone Numbers |
| LeetCode | #193 |
| Difficulty | Easy |
| Language | Shell |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a text file `file.txt` that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

## Examples
Consider the standard input for **Valid Phone Numbers**. Applying **In-Place Array Traversal & Index Mapping** yields the target result step by step.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The solution uses `grep -E` (extended regular expressions) to match lines that conform to one of the two valid formats:
- `^([0-9]{3}-[0-9]{3}-[0-9]{4})$` matches the format `xxx-xxx-xxxx`.
- `^(\([0-9]{3}\) [0-9]{3}-[0-9]{4})$` matches the format `(xxx) xxx-xxxx`.
- The `^` and `$` anchors ensure the entire line must match (no extra characters before or after).
- The `|` operator combines both patterns so either format is accepted.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
Applying **In-Place Array Traversal & Index Mapping** step by step to the input yields the expected result.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Shell

## Source Code
- [solution.sh](./solution.sh)


```bash
# Read from the file file.txt and output all valid phone numbers to stdout.
grep -E '^([0-9]{3}-[0-9]{3}-[0-9]{4}|\([0-9]{3}\) [0-9]{3}-[0-9]{4})$' file.txt
```

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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [3465. Find Products with Valid Serial Numbers](../../3501-4000/3803-find-products-with-valid-serial-numbers/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-phone-numbers/)
