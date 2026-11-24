# LeetCode 2037: Minimum Number of Moves to Seat Everyone

**LeetCode Problem #2037 — Minimum Number of Moves to Seat Everyone**
Solve LeetCode Minimum Number of Moves to Seat Everyone using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Moves to Seat Everyone |
| LeetCode | #2037 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `n` **availabe **seats and `n` students **standing** in a room. You are given an array `seats` of length `n`, where `seats[i]` is the position of the `i^th` seat. You are also given the array `students` of length `n`, where `students[j]` is the position of the `j^th` student.

You may perform the following move any number of times:

Increase or decrease the position of the `i^th` student by `1` (i.e., moving the `i^th` student from position `x` to `x + 1` or `x - 1`)

Return *the **minimum number of moves** required to move each student to a seat** such that no two students are in the same seat.*

Note that there may be **multiple** seats or students in the **same **position at the beginning.

## Constraints
- `n == seats.length == students.length`
- `1 <= n <= 100`
- `1 <= seats[i], students[j] <= 100`

## Examples
### Example 1
- **Input:** `seats = [3,1,5], students = [2,7,4]`
- **Output:** `4`
- **Explanation:** The students are moved as follows:
- The first student is moved from position 2 to position 1 using 1 move.
- The second student is moved from position 7 to position 5 using 2 moves.
- The third student is moved from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.

### Example 2
- **Input:** `seats = [4,1,5,9], students = [1,3,2,6]`
- **Output:** `7`
- **Explanation:** The students are moved as follows:
- The first student is not moved.
- The second student is moved from position 3 to position 4 using 1 move.
- The third student is moved from position 2 to position 5 using 3 moves.
- The fourth student is moved from position 6 to position 9 using 3 moves.
In total, 0 + 1 + 3 + 3 = 7 moves were used.

### Example 3
- **Input:** `seats = [2,2,6,6], students = [1,3,2,6]`
- **Output:** `4`
- **Explanation:** Note that there are two seats at position 2 and two seats at position 6.
The students are moved as follows:
- The first student is moved from position 1 to position 2 using 1 move.
- The second student is moved from position 3 to position 6 using 3 moves.
- The third student is not moved.
- The fourth student is not moved.
In total, 1 + 3 + 0 + 0 = 4 moves were used.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Number of Moves to Seat Everyone**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `seats = [3,1,5], students = [2,7,4]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The students are moved as follows:
- The first student is moved from position 2 to position 1 using 1 move.
- The second student is moved from position 7 to position 5 using 2 moves.
- The third student is moved from position 4 to position 3 using 1 move.
In total, 1 + 2 + 1 = 4 moves were used.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(s - t) for s, t in zip(seats, students))
```

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
- [2193. Minimum Number of Moves to Make Palindrome](../../2001-2500/2193-minimum-number-of-moves-to-make-palindrome/)
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/)
