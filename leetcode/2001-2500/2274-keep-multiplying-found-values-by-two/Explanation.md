# LeetCode 2154: Keep Multiplying Found Values by Two

**LeetCode Problem #2154 — Keep Multiplying Found Values by Two**
Solve LeetCode Keep Multiplying Found Values by Two using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Keep Multiplying Found Values by Two |
| LeetCode | #2154 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of integers `nums`. You are also given an integer `original` which is the first number that needs to be searched for in `nums`.

You then do the following steps:

If `original` is found in `nums`, **multiply** it by two (i.e., set `original = 2 * original`). 
 Otherwise, **stop** the process. 
 **Repeat** this process with the new number as long as you keep finding the number.

Return *the **final** value of *`original`.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i], original <= 1000`

## Examples
### Example 1
- **Input:** `nums = [5,3,6,1,12], original = 3`
- **Output:** `24`
- **Explanation:** - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.

### Example 2
- **Input:** `nums = [2,7,9], original = 4`
- **Output:** `4`
- **Explanation:** - 4 is not found in nums. Thus, 4 is returned.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Keep Multiplying Found Values by Two**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,3,6,1,12], original = 3`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `24`.
4. **Verification:** - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.

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
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        seen = set(nums)
        while original in seen:
            original *= 2
        return original
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
- [3880. Minimum Absolute Difference Between Two Values](../../4001-4500/4255-minimum-absolute-difference-between-two-values/)
- [807. Max Increase to Keep City Skyline](../../0501-1000/0825-max-increase-to-keep-city-skyline/)
- [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](../../1501-2000/1701-remove-max-number-of-edges-to-keep-graph-fully-traversable/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/keep-multiplying-found-values-by-two/)
