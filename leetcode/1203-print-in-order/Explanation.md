# LeetCode 1114: Print in Order

**LeetCode Problem #1114 — Print in Order**
Solve LeetCode Print in Order using Java and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Print in Order |
| LeetCode | #1114 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
public void first() { print("first"); }

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The code uses **Semaphores** (or equivalent synchronization) to enforce ordering.

1. Two semaphores control the gates: `sem1` (blocks `second`) and `sem2` (blocks `third`), both starting at `0`.
2. **first():** Prints "first", then releases `sem1`.
3. **second():** Waits on `sem1`, prints "second", then releases `sem2`.
4. **third():** Waits on `sem2`, then prints "third".

This chain of semaphores guarantees the correct order regardless of thread scheduling.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Print in Order**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Java

## Source Code
- [solution.java](./solution.java)

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [183. Customers Who Never Order](../0183-customers-who-never-order/)
- [1115. Print FooBar Alternately](../1187-print-foobar-alternately/)
- [1116. Print Zero Even Odd](../1216-print-zero-even-odd/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/print-in-order/)
