# LeetCode 3979: Maximum Valid Pair Sum

**LeetCode Problem #3979 — Maximum Valid Pair Sum**
Solve LeetCode Maximum Valid Pair Sum using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Valid Pair Sum |
| LeetCode | #3979 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer `k`.

A pair of indices `(i, j)` is called **valid** if:

`0 <= i < j < n` 
 `j - i >= k`

Return the **maximum** value of `nums[i] + nums[j]` among all valid pairs.

## Constraints
- `2 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= n - 1`

## Examples
### Example 1
- **Input:** `nums = [1,3,5,2,8], k = 2`
- **Output:** `13`
- **Explanation:** The valid pairs are: 

 
 `(0, 2)`: `nums[0] + nums[2] = 6` 
 `(0, 3)`: `nums[0] + nums[3] = 3` 
 `(0, 4)`: `nums[0] + nums[4] = 9` 
 `(1, 3)`: `nums[1] + nums[3] = 5` 
 `(1, 4)`: `nums[1] + nums[4] = 11` 
 `(2, 4)`: `nums[2] + nums[4] = 13` 
 

 Thus, the answer is 13.​​​​​​​

### Example 2
- **Input:** `nums = [5,1,9], k = 1`
- **Output:** `14`
- **Explanation:** Since `k = 1`, every pair is valid. 
 The maximum value is obtained from a pair `(0, 2)`​​​​​​​, which is `nums[0] + nums[2] = 5 + 9 = 14`. 
 Thus, the answer is 14.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Maximum Valid Pair Sum**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,5,2,8], k = 2`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `13`.
4. **Verification:** The valid pairs are: 

 
 `(0, 2)`: `nums[0] + nums[2] = 6` 
 `(0, 3)`: `nums[0] + nums[3] = 3` 
 `(0, 4)`: `nums[0] + nums[4] = 9` 
 `(1, 3)`: `nums[1] + nums[3] = 5` 
 `(1, 4)`: `nums[1] + nums[4] = 11` 
 `(2, 4)`: `nums[2] + nums[4] = 13` 
 

 Thus, the answer is 13.​​​​​​​

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
from typing import List

class Solution:
    def maxValidPairSum(self, nums: List[int], k: int) -> int:
        ans = 0
        best = 0
        for j in range(k, len(nums)):
            best = max(best, nums[j - k])
            ans = max(ans, best + nums[j])
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
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [918. Maximum Sum Circular Subarray](../../0501-1000/0954-maximum-sum-circular-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-valid-pair-sum/)
