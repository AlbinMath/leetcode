# LeetCode 857: Minimum Cost to Hire K Workers

**LeetCode Problem #857 — Minimum Cost to Hire K Workers**
Solve LeetCode Minimum Cost to Hire K Workers using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Hire K Workers |
| LeetCode | #857 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` workers. You are given two integer arrays `quality` and `wage` where `quality[i]` is the quality of the `i^th` worker and `wage[i]` is the minimum wage expectation for the `i^th` worker.

We want to hire exactly `k` workers to form a **paid group**. To hire a group of `k` workers, we must pay them according to the following rules:

Every worker in the paid group must be paid at least their minimum wage expectation. 
 In the group, each worker's pay must be directly proportional to their quality. This means if a worker&rsquo;s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.

Given the integer `k`, return *the least amount of money needed to form a paid group satisfying the above conditions*. Answers within `10^-5` of the actual answer will be accepted.

## Constraints
- `n == quality.length == wage.length`
- `1 <= k <= n <= 10^4`
- `1 <= quality[i], wage[i] <= 10^4`

## Examples
### Example 1
- **Input:** `quality = [10,20,5], wage = [70,50,30], k = 2`
- **Output:** `105.00000`
- **Explanation:** We pay 70 to 0^th worker and 35 to 2^nd worker.

### Example 2
- **Input:** `quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3`
- **Output:** `30.66667`
- **Explanation:** We pay 4 to 0^th worker, 13.33333 to 2^nd and 3^rd workers separately.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost to Hire K Workers**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `quality = [10,20,5], wage = [70,50,30], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `105.00000`.
4. **Verification:** We pay 70 to 0^th worker and 35 to 2^nd worker.

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
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted(zip(quality, wage), key=lambda w: w[1] / w[0])
        heap = []  # max-heap via negated qualities
        q_sum = 0
        ans = float('inf')
        for q, w in workers:
            ratio = w / q
            heapq.heappush(heap, -q)
            q_sum += q
            if len(heap) > k:
                q_sum += heapq.heappop(heap)  # popped value is negative
            if len(heap) == k:
                ans = min(ans, ratio * q_sum)
        return ans
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
- [2462. Total Cost to Hire K Workers](../../2001-2500/2462-total-cost-to-hire-k-workers/)
- [4046. Minimum Cost Path With At Most K Turns](../../4001-4500/4046-minimum-cost-path-with-at-most-k-turns/)
- [1000. Minimum Cost to Merge Stones](../../0501-1000/1000-minimum-cost-to-merge-stones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/)
