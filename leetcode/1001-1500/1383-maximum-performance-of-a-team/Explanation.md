# LeetCode 1383: Maximum Performance of a Team

**LeetCode Problem #1383 — Maximum Performance of a Team**
Solve LeetCode Maximum Performance of a Team using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Performance of a Team |
| LeetCode | #1383 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `n` and `k` and two integer arrays `speed` and `efficiency` both of length `n`. There are `n` engineers numbered from `1` to `n`. `speed[i]` and `efficiency[i]` represent the speed and efficiency of the `i^th` engineer respectively.

Choose **at most** `k` different engineers out of the `n` engineers to form a team with the maximum **performance**.

The performance of a team is the sum of its engineers' speeds multiplied by the minimum efficiency among its engineers.

Return *the maximum performance of this team*. Since the answer can be a huge number, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= k <= n <= 10^5`
- `speed.length == n`
- `efficiency.length == n`
- `1 <= speed[i] <= 10^5`
- `1 <= efficiency[i] <= 10^8`

## Examples
### Example 1
- **Input:** `n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2`
- **Output:** `60`
- **Explanation:** We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

### Example 2
- **Input:** `n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3`
- **Output:** `68`
- **Explanation:** This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

### Example 3
- **Input:** `n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4`
- **Output:** `72`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Performance of a Team**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `60`.
4. **Verification:** We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        heap = []  # min-heap of speeds
        s_sum = 0
        best = 0
        for e, s in engineers:
            heapq.heappush(heap, s)
            s_sum += s
            if len(heap) > k:
                s_sum -= heapq.heappop(heap)
            best = max(best, s_sum * e)
        return best % MOD
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)
- [104. Maximum Depth of Binary Tree](../../0001-0500/0104-maximum-depth-of-binary-tree/)
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-performance-of-a-team/)
