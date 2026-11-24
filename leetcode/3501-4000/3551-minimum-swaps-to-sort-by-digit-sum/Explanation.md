# LeetCode 3551: Minimum Swaps to Sort by Digit Sum

**LeetCode Problem #3551 — Minimum Swaps to Sort by Digit Sum**
Solve LeetCode Minimum Swaps to Sort by Digit Sum using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Swaps to Sort by Digit Sum |
| LeetCode | #3551 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `nums` of **distinct** positive integers. You need to sort the array in **increasing** order based on the sum of the digits of each number. If two numbers have the same digit sum, the **smaller** number appears first in the sorted order.

Return the **minimum** number of swaps required to rearrange `nums` into this sorted order.

A **swap** is defined as exchanging the values at two distinct positions in the array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `nums` consists of **distinct** positive integers.

## Examples
### Example 1
- **Input:** `nums = [37,100]`
- **Output:** `1`
- **Explanation:** Compute the digit sum for each integer: `[3 + 7 = 10, 1 + 0 + 0 = 1] &rarr; [10, 1]` 
 Sort the integers based on digit sum: `[100, 37]`. Swap `37` with `100` to obtain the sorted order. 
 Thus, the minimum number of swaps required to rearrange `nums` is 1.

### Example 2
- **Input:** `nums = [22,14,33,7]`
- **Output:** `0`
- **Explanation:** Compute the digit sum for each integer: `[2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] &rarr; [4, 5, 6, 7]` 
 Sort the integers based on digit sum: `[22, 14, 33, 7]`. The array is already sorted. 
 Thus, the minimum number of swaps required to rearrange `nums` is 0.

### Example 3
- **Input:** `nums = [18,43,34,16]`
- **Output:** `2`
- **Explanation:** Compute the digit sum for each integer: `[1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] &rarr; [9, 7, 7, 7]` 
 Sort the integers based on digit sum: `[16, 34, 43, 18]`. Swap `18` with `16`, and swap `43` with `34` to obtain the sorted order. 
 Thus, the minimum number of swaps required to rearrange `nums` is 2.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Swaps to Sort by Digit Sum**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [37,100]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Compute the digit sum for each integer: `[3 + 7 = 10, 1 + 0 + 0 = 1] &rarr; [10, 1]` 
 Sort the integers based on digit sum: `[100, 37]`. Swap `37` with `100` to obtain the sorted order. 
 Thus, the minimum number of swaps required to rearrange `nums` is 1.

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
    def minSwaps(self, nums):
        a = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        pos = {v: i for i, v in enumerate(nums)}
        p = [pos[x] for x in a]
        ans = 0
        for i in range(len(p)):
            while p[i] != i:
                j = p[i]
                p[i], p[j] = p[j], p[i]
                ans += 1
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
- [3300. Minimum Element After Replacement With Digit Sum](../../3001-3500/3300-minimum-element-after-replacement-with-digit-sum/)
- [2180. Count Integers With Even Digit Sum](../../2001-2500/2180-count-integers-with-even-digit-sum/)
- [2243. Calculate Digit Sum of a String](../../2001-2500/2243-calculate-digit-sum-of-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/)
