# LeetCode 2567: Minimum Score by Changing Two Elements

**LeetCode Problem #2567 — Minimum Score by Changing Two Elements**
Solve LeetCode Minimum Score by Changing Two Elements using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Score by Changing Two Elements |
| LeetCode | #2567 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

The **low** score of `nums` is the **minimum** absolute difference between any two integers. 
 The **high** score of `nums` is the **maximum** absolute difference between any two integers. 
 The **score** of `nums` is the sum of the **high** and **low** scores.

Return the **minimum score** after **changing two elements** of `nums`.

## Constraints
- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,4,7,8,5]`
- **Output:** `3`
- **Explanation:** Change `nums[0]` and `nums[1]` to be 6 so that `nums` becomes [6,6,7,8,5]. 
 The low score is the minimum absolute difference: |6 - 6| = 0. 
 The high score is the maximum absolute difference: |8 - 5| = 3. 
 The sum of high and low score is 3.

### Example 2
- **Input:** `nums = [1,4,3]`
- **Output:** `0`
- **Explanation:** Change `nums[1]` and `nums[2]` to 1 so that `nums` becomes [1,1,1]. 
 The sum of maximum absolute difference and minimum absolute difference is 0.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Score by Changing Two Elements**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,4,7,8,5]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Change `nums[0]` and `nums[1]` to be 6 so that `nums` becomes [6,6,7,8,5]. 
 The low score is the minimum absolute difference: |6 - 6| = 0. 
 The high score is the maximum absolute difference: |8 - 5| = 3. 
 The sum of high and low score is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return min(nums[-1] - nums[2],
                   nums[-2] - nums[1],
                   nums[-3] - nums[0])
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2492. Minimum Score of a Path Between Two Cities](../../2001-2500/2492-minimum-score-of-a-path-between-two-cities/)
- [2139. Minimum Moves to Reach Target Score](../../2001-2500/2139-minimum-moves-to-reach-target-score/)
- [2322. Minimum Score After Removals on a Tree](../../2001-2500/2322-minimum-score-after-removals-on-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-score-by-changing-two-elements/)
