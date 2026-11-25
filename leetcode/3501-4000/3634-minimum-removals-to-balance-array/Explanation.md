# LeetCode 3634: Minimum Removals to Balance Array

**LeetCode Problem #3634 — Minimum Removals to Balance Array**
Solve LeetCode Minimum Removals to Balance Array using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Removals to Balance Array |
| LeetCode | #3634 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

An array is considered **balanced** if the value of its **maximum** element is **at most** `k` times the **minimum** element.

You may remove **any** number of elements from `nums`​​​​​​​ without making it **empty**.

Return the **minimum** number of elements to remove so that the remaining array is balanced.

**Note:** An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,1,5], k = 2`
- **Output:** `1`
- **Explanation:** Remove `nums[2] = 5` to get `nums = [2, 1]`. 
 Now `max = 2`, `min = 1` and `max <= min * k` as `2 <= 1 * 2`. Thus, the answer is 1.

### Example 2
- **Input:** `nums = [1,6,2,9], k = 3`
- **Output:** `2`
- **Explanation:** Remove `nums[0] = 1` and `nums[3] = 9` to get `nums = [6, 2]`. 
 Now `max = 6`, `min = 2` and `max <= min * k` as `6 <= 2 * 3`. Thus, the answer is 2.

### Example 3
- **Input:** `nums = [4,6], k = 2`
- **Output:** `0`
- **Explanation:** Since `nums` is already balanced as `6 <= 4 * 2`, no elements need to be removed.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Removals to Balance Array**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,5], k = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Remove `nums[2] = 5` to get `nums = [2, 1]`. 
 Now `max = 2`, `min = 1` and `max <= min * k` as `2 <= 1 * 2`. Thus, the answer is 1.

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
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        best = 0
        for r, x in enumerate(nums):
            while x > k * nums[l]:
                l += 1
            best = max(best, r - l + 1)
        return len(nums) - best
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
- [1671. Minimum Number of Removals to Make Mountain Array](../../1501-2000/1671-minimum-number-of-removals-to-make-mountain-array/)
- [2856. Minimum Array Length After Pair Removals](../../2501-3000/2856-minimum-array-length-after-pair-removals/)
- [153. Find Minimum in Rotated Sorted Array](../../0001-0500/0153-find-minimum-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-removals-to-balance-array/)
