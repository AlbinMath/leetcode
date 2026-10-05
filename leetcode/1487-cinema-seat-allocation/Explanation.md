# LeetCode 1386: Cinema Seat Allocation

**LeetCode Problem #1386 — Cinema Seat Allocation**
Solve LeetCode Cinema Seat Allocation using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Cinema Seat Allocation |
| LeetCode | #1386 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem
A cinema has  n  rows of seats, numbered from 1 to  n . Each row has 10 seats, numbered from 1 to 10.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The code uses **Bitmasks** for efficient seat tracking.

1. **Bitmask per Row:** For each reserved seat, set the corresponding bit in a bitmask for that row. Only rows with reservations are stored in a hash map.
2. **Unreserved Rows:** Rows without any reservations can always fit 2 groups (left: seats 2–5, right: seats 6–9). Contribute `2 * (n - reservedRows)`.
3. **Reserved Rows:** For each row with reservations, check three possible group positions using bitwise AND:
   - **Left** (seats 2–5): bits 2,3,4,5 must be free.
   - **Middle** (seats 4–7): bits 4,5,6,7 must be free.
   - **Right** (seats 6–9): bits 6,7,8,9 must be free.
   - If both left and right fit → 2 groups. Else if any one fits → 1 group.

Time complexity is $O(R)$ where $R$ is the number of reserved seats, and space complexity is $O(R)$.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example
Consider the standard input for **Cinema Seat Allocation**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)

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
- [1. Two Sum](../0001-two-sum/)
- [13. Roman to Integer](../0013-roman-to-integer/)
- [192. Word Frequency](../0192-word-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/cinema-seat-allocation/)
