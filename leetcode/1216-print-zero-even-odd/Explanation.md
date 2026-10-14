# LeetCode 1116: Print Zero Even Odd

**LeetCode Problem #1116 — Print Zero Even Odd**
Solve LeetCode Print Zero Even Odd using Java and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Print Zero Even Odd |
| LeetCode | #1116 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem
You have a function  printNumber  that can be called with an integer parameter and prints it to the console.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
The code uses three **Semaphores** for synchronization.

1. **Semaphore State:** `zero` starts at `1` (goes first), `even` and `odd` start at `0`.
2. **zero thread:** For each number `i` from `1` to `n`, acquires the `zero` semaphore, prints `0`, then releases either `odd` (if `i` is odd) or `even` (if `i` is even).
3. **odd thread:** For each odd number, acquires the `odd` semaphore, prints the odd number, then releases `zero`.
4. **even thread:** For each even number, acquires the `even` semaphore, prints the even number, then releases `zero`.

This creates the pattern: zero→odd→zero→even→zero→odd→... producing `"010203..."`.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Print Zero Even Odd**. Applying **Two Pointer Convergence & Scanning** yields the target result step by step.

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
Java

## Source Code
- [solution.java](./solution.java)

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
- [328. Odd Even Linked List](../0328-odd-even-linked-list/)
- [3220. Odd and Even Transactions](../3530-odd-and-even-transactions/)
- [3658. GCD of Odd and Even Sums](../3995-gcd-of-odd-and-even-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/print-zero-even-odd/)
