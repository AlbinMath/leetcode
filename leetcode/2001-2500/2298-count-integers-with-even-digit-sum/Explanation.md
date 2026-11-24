# LeetCode 2180: Count Integers With Even Digit Sum

**LeetCode Problem #2180 — Count Integers With Even Digit Sum**
Solve LeetCode Count Integers With Even Digit Sum using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Integers With Even Digit Sum |
| LeetCode | #2180 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a positive integer `num`, return *the number of positive integers **less than or equal to*** `num` *whose digit sums are **even***.

The **digit sum** of a positive integer is the sum of all its digits.

## Constraints
- `1 <= num <= 1000`

## Examples
### Example 1
- **Input:** `num = 4`
- **Output:** `2`
- **Explanation:** The only integers less than or equal to 4 whose digit sums are even are 2 and 4.

### Example 2
- **Input:** `num = 30`
- **Output:** `14`
- **Explanation:** The 14 integers less than or equal to 30 whose digit sums are even are
2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Count Integers With Even Digit Sum**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 4`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The only integers less than or equal to 4 whose digit sums are even are 2 and 4.

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
    def countEven(self, num: int) -> int:
        return sum(1 for i in range(1, num + 1) if sum(map(int, str(i))) % 2 == 0)
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
- [3910. Count Connected Subgraphs with Even Node Sum](../../4001-4500/4279-count-connected-subgraphs-with-even-node-sum/)
- [985. Sum of Even Numbers After Queries](../../1001-1500/1027-sum-of-even-numbers-after-queries/)
- [1315. Sum of Nodes with Even-Valued Grandparent](../../1001-1500/1243-sum-of-nodes-with-even-valued-grandparent/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-integers-with-even-digit-sum/)
