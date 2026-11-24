# LeetCode 1524: Number of Sub-arrays With Odd Sum

**LeetCode Problem #1524 — Number of Sub-arrays With Odd Sum**
Solve LeetCode Number of Sub-arrays With Odd Sum using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Sub-arrays With Odd Sum |
| LeetCode | #1524 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `arr`, return *the number of subarrays with an **odd** sum*.

Since the answer can be very large, return it modulo `10^9 + 7`.

## Constraints
- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 100`

## Examples
### Example 1
- **Input:** `arr = [1,3,5]`
- **Output:** `4`
- **Explanation:** All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

### Example 2
- **Input:** `arr = [2,4,6]`
- **Output:** `0`
- **Explanation:** All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.

### Example 3
- **Input:** `arr = [1,2,3,4,5,6,7]`
- **Output:** `16`

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Sub-arrays With Odd Sum**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,3,5]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even, odd = 1, 0  # counts of prefix parities seen so far (empty prefix is even)
        parity = 0
        ans = 0
        for x in arr:
            parity ^= (x & 1)
            if parity == 0:
                ans += odd   # need an earlier odd prefix
                even += 1
            else:
                ans += even  # need an earlier even prefix
                odd += 1
        return ans % MOD
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../../1001-1500/1477-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [1775. Equal Sum Arrays With Minimum Number of Operations](../../1501-2000/1775-equal-sum-arrays-with-minimum-number-of-operations/)
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1343-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/)
