# LeetCode 1997: First Day Where You Have Been in All the Rooms

**LeetCode Problem #1997 — First Day Where You Have Been in All the Rooms**
Solve LeetCode First Day Where You Have Been in All the Rooms using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | First Day Where You Have Been in All the Rooms |
| LeetCode | #1997 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are `n` rooms you need to visit, labeled from `0` to `n - 1`. Each day is labeled, starting from `0`. You will go in and visit one room a day.

Initially on day `0`, you visit room `0`. The **order** you visit the rooms for the coming days is determined by the following **rules** and a given **0-indexed** array `nextVisit` of length `n`:

Assuming that on a day, you visit room `i`, 
 if you have been in room `i` an **odd** number of times (**including** the current visit), on the **next** day you will visit a room with a **lower or equal room number** specified by `nextVisit[i]` where `0 <= nextVisit[i] <= i`; 
 if you have been in room `i` an **even** number of times (**including** the current visit), on the **next** day you will visit room `(i + 1) mod n`.

Return *the label of the **first** day where you have been in **all** the rooms*. It can be shown that such a day exists. Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `n == nextVisit.length`
- `2 <= n <= 10^5`
- `0 <= nextVisit[i] <= i`

## Examples
### Example 1
- **Input:** `nextVisit = [0,0]`
- **Output:** `2`
- **Explanation:** - On day 0, you visit room 0. The total times you have been in room 0 is 1, which is odd.
 On the next day you will visit room nextVisit[0] = 0
- On day 1, you visit room 0, The total times you have been in room 0 is 2, which is even.
 On the next day you will visit room (0 + 1) mod 2 = 1
- On day 2, you visit room 1. This is the first day where you have been in all the rooms.

### Example 2
- **Input:** `nextVisit = [0,0,2]`
- **Output:** `6`
- **Explanation:** Your room visiting order for each day is: [0,0,1,0,0,1,2,...].
Day 6 is the first day where you have been in all the rooms.

### Example 3
- **Input:** `nextVisit = [0,1,2,0]`
- **Output:** `6`
- **Explanation:** Your room visiting order for each day is: [0,0,1,1,2,2,3,...].
Day 6 is the first day where you have been in all the rooms.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **First Day Where You Have Been in All the Rooms**, we observe the problem requirements and utilize the **Array / General** technique. We decompose the problem into overlapping subproblems using a **Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nextVisit = [0,0]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** - On day 0, you visit room 0. The total times you have been in room 0 is 1, which is odd.
 On the next day you will visit room nextVisit[0] = 0
- On day 1, you visit room 0, The total times you have been in room 0 is 2, which is even.
 On the next day you will visit room (0 + 1) mod 2 = 1
- On day 2, you visit room 1. This is the first day where you have been in all the rooms.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nextVisit)
        
        dp = [0] * n
        
        for i in range(n - 1):
            dp[i + 1] = (2 * dp[i] - dp[nextVisit[i]] + 2) % MOD
            
        return dp[n - 1]
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [1970. Last Day Where You Can Still Cross](../../1501-2000/1970-last-day-where-you-can-still-cross/)
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)
- [1941. Check if All Characters Have Equal Number of Occurrences](../../1501-2000/1941-check-if-all-characters-have-equal-number-of-occurrences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/)
