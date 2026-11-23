# LeetCode 4044: Count Good Cyclic Rotations

**LeetCode Problem #4044 — Count Good Cyclic Rotations**
Solve LeetCode Count Good Cyclic Rotations using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Good Cyclic Rotations |
| LeetCode | #4044 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of even length `n`.

A **cyclic rotation** of `nums` is obtained by choosing a prefix of `nums` whose length is between 0 and `n - 1` (inclusive), and moving it to the end of the array while preserving the order of all elements.

A cyclic rotation is **good** if the sum of its first `n / 2` elements is **strictly greater** than the sum of its last `n / 2` elements.

Return the number of cyclic rotations of `nums` that are good.

## Constraints
- `2 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `n` is even.

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5,6]`
- **Output:** `3`
- **Explanation:** The cyclic rotations of `nums` are: 

 
 
 
 Cyclic rotation 
 Sum of first `n / 2` elements 
 Sum of last `n / 2` elements 
 
 
 
 
 `[1, 2, 3, 4, 5, 6]` 
 `1 + 2 + 3 = 6` 
 `4 + 5 + 6 = 15` 
 
 
 `[2, 3, 4, 5, 6, 1]` 
 `2 + 3 + 4 = 9` 
 `5 + 6 + 1 = 12` 
 
 
 `[3, 4, 5, 6, 1, 2]` 
 `3 + 4 + 5 = 12` 
 `6 + 1 + 2 = 9` 
 
 
 `[4, 5, 6, 1, 2, 3]` 
 `4 + 5 + 6 = 15` 
 `1 + 2 + 3 = 6` 
 
 
 `[5, 6, 1, 2, 3, 4]` 
 `5 + 6 + 1 = 12` 
 `2 + 3 + 4 = 9` 
 
 
 `[6, 1, 2, 3, 4, 5]` 
 `6 + 1 + 2 = 9` 
 `3 + 4 + 5 = 12` 
 
 
 

 The first half has a greater sum than the second half for 3 rotations. Thus, the answer is 3.

### Example 2
- **Input:** `nums = [1,2,1,2]`
- **Output:** `0`
- **Explanation:** The cyclic rotations of `nums` are: 

 
 
 
 Cyclic rotation 
 Sum of first `n / 2` elements 
 Sum of last `n / 2` elements 
 
 
 
 
 `[1, 2, 1, 2]` 
 `1 + 2 = 3` 
 `1 + 2 = 3` 
 
 
 `[2, 1, 2, 1]` 
 `2 + 1 = 3` 
 `2 + 1 = 3` 
 
 
 `[1, 2, 1, 2]` 
 `1 + 2 = 3` 
 `1 + 2 = 3` 
 
 
 `[2, 1, 2, 1]` 
 `2 + 1 = 3` 
 `2 + 1 = 3` 
 
 
 

 No cyclic rotation is good because the two sums are equal for every rotation. Thus, the answer is 0.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Good Cyclic Rotations**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5,6]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The cyclic rotations of `nums` are: 

 
 
 
 Cyclic rotation 
 Sum of first `n / 2` elements 
 Sum of last `n / 2` elements 
 
 
 
 
 `[1, 2, 3, 4, 5, 6]` 
 `1 + 2 + 3 = 6` 
 `4 + 5 + 6 = 15` 
 
 
 `[2, 3, 4, 5, 6, 1]` 
 `2 + 3 + 4 = 9` 
 `5 + 6 + 1 = 12` 
 
 
 `[3, 4, 5, 6, 1, 2]` 
 `3 + 4 + 5 = 12` 
 `6 + 1 + 2 = 9` 
 
 
 `[4, 5, 6, 1, 2, 3]` 
 `4 + 5 + 6 = 15` 
 `1 + 2 + 3 = 6` 
 
 
 `[5, 6, 1, 2, 3, 4]` 
 `5 + 6 + 1 = 12` 
 `2 + 3 + 4 = 9` 
 
 
 `[6, 1, 2, 3, 4, 5]` 
 `6 + 1 + 2 = 9` 
 `3 + 4 + 5 = 12` 
 
 
 

 The first half has a greater sum than the second half for 3 rotations. Thus, the answer is 3.

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
    def countGoodRotations(self, nums: List[int]) -> int:
        n = len(nums)
        h = n // 2
        total = sum(nums)
        w = sum(nums[:h])
        ans = 0
        for r in range(n):
            if 2 * w > total:
                ans += 1
            w += nums[(r + h) % n] - nums[r]
        return ans
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
- [1448. Count Good Nodes in Binary Tree](../../1501-2000/1544-count-good-nodes-in-binary-tree/)
- [1534. Count Good Triplets](../../1501-2000/1656-count-good-triplets/)
- [1922. Count Good Numbers](../../2001-2500/2050-count-good-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-good-cyclic-rotations/)
