# LeetCode 1819: Number of Different Subsequences GCDs

**LeetCode Problem #1819 — Number of Different Subsequences GCDs**
Solve LeetCode Number of Different Subsequences GCDs using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Different Subsequences GCDs |
| LeetCode | #1819 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `nums` that consists of positive integers.

The **GCD** of a sequence of numbers is defined as the greatest integer that divides **all** the numbers in the sequence evenly.

For example, the GCD of the sequence `[4,6,16]` is `2`.

A **subsequence** of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, `[2,5,10]` is a subsequence of `[1,2,1,** 2 **,4,1, **5** , **10** ]`.

Return *the **number** of **different** GCDs among all **non-empty** subsequences of* `nums`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 2 * 10^5`

## Examples
### Example 1
- **Input:** `nums = [6,10,3]`
- **Output:** `5`
- **Explanation:** The figure shows all the non-empty subsequences and their GCDs.
The different GCDs are 6, 10, 3, 2, and 1.

### Example 2
- **Input:** `nums = [5,15,40,5,6]`
- **Output:** `7`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Number of Different Subsequences GCDs**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [6,10,3]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The figure shows all the non-empty subsequences and their GCDs.
The different GCDs are 6, 10, 3, 2, and 1.

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
from math import gcd

class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        max_num = max(nums)
        present = [False] * (max_num + 1)

        for num in nums:
            present[num] = True

        count = 0

        for target in range(1, max_num + 1):
            current_gcd = 0

            for multiple in range(target, max_num + 1, target):
                if present[multiple]:
                    current_gcd = gcd(current_gcd, multiple)

                    if current_gcd == target:
                        count += 1
                        break

        return count
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
- [730. Count Different Palindromic Subsequences](../../0501-1000/0730-count-different-palindromic-subsequences/)
- [1434. Number of Ways to Wear Different Hats to Each Other](../../1501-2000/1531-number-of-ways-to-wear-different-hats-to-each-other/)
- [1805. Number of Different Integers in a String](../../1501-2000/1933-number-of-different-integers-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-different-subsequences-gcds/)
