# LeetCode 985: Sum of Even Numbers After Queries

**LeetCode Problem #985 — Sum of Even Numbers After Queries**
Solve LeetCode Sum of Even Numbers After Queries using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Even Numbers After Queries |
| LeetCode | #985 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an array `queries` where `queries[i] = [val_i, index_i]`.

For each query `i`, first, apply `nums[index_i] = nums[index_i] + val_i`, then print the sum of the even values of `nums`.

Return *an integer array *`answer`* where *`answer[i]`* is the answer to the *`i^th`* query*.

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= queries.length <= 10^4`
- `-10^4 <= val_i <= 10^4`
- `0 <= index_i < nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]`
- **Output:** `[8,6,2,4]`
- **Explanation:** At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

### Example 2
- **Input:** `nums = [1], queries = [[4,0]]`
- **Output:** `[0]`

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Sum of Even Numbers After Queries**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We decompose the problem into overlapping subproblems using a **DP Table / Array**. Optimal intermediate states are saved so that each subproblem is solved exactly once.

## Algorithm
1. Establish base cases in the DP structure.
2. Iterate through subproblem states following recurrence relations.
3. Derive final answer from completed subproblem state.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[8,6,2,4]`.
4. **Verification:** At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

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
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)
        ans = []

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even_sum += nums[idx]
            ans.append(even_sum)

        return ans
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
- [2458. Height of Binary Tree After Subtree Removal Queries](../../2501-3000/2545-height-of-binary-tree-after-subtree-removal-queries/)
- [2736. Maximum Sum Queries](../../2501-3000/2839-maximum-sum-queries/)
- [3243. Shortest Distance After Road Addition Queries I](../../3501-4000/3517-shortest-distance-after-road-addition-queries-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-even-numbers-after-queries/)
