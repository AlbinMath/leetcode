# LeetCode 645: Set Mismatch

**LeetCode Problem #645 — Set Mismatch**
Solve LeetCode Set Mismatch using TypeScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Set Mismatch |
| LeetCode | #645 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have a set of integers  s , which originally contains all the numbers from  1  to  n . Unfortunately, due to some error, one of the numbers in  s  got duplicated to another number in the set, which results in  repetition of one  number and  loss of another  number.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **HashSet** for straightforward detection.

1. **Find Duplicate:** It iterates through `nums`, adding each number to a `Set`. If a number is already in the set, it's the duplicate.
2. **Find Missing:** It loops from `1` to `n` and checks which number is not in the set — that's the missing number.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Set Mismatch**. Applying **Bitwise Masking & Bit Shift** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [73. Set Matrix Zeroes](../0073-set-matrix-zeroes/)
- [762. Prime Number of Set Bits in Binary Representation](../0767-prime-number-of-set-bits-in-binary-representation/)
- [7. Reverse Integer](../0007-reverse-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/set-mismatch/)
