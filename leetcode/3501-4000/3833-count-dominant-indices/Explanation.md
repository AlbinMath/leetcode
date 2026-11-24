# LeetCode 3833: Count Dominant Indices

**LeetCode Problem #3833 — Count Dominant Indices**
Solve LeetCode Count Dominant Indices using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Dominant Indices |
| LeetCode | #3833 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n`.

An element at index `i` is called **dominant** if: `nums[i] > average(nums[i + 1], nums[i + 2], ..., nums[n - 1])`

Your task is to count the number of indices `i` that are **dominant**.

The **average** of a set of numbers is the value obtained by adding all the numbers together and dividing the sum by the total number of numbers.

**Note**: The **rightmost** element of any array is **not** **dominant**.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`​​​​​​​

## Examples
### Example 1
- **Input:** `nums = [5,4,3]`
- **Output:** `2`
- **Explanation:** At index `i = 0`, the value 5 is dominant as `5 > average(4, 3) = 3.5`. 
 At index `i = 1`, the value 4 is dominant over the subarray `[3]`. 
 Index `i = 2` is not dominant as there are no elements to its right. Thus, the answer is 2.

### Example 2
- **Input:** `nums = [4,1,2]`
- **Output:** `1`
- **Explanation:** At index `i = 0`, the value 4 is dominant over the subarray `[1, 2]`. 
 At index `i = 1`, the value 1 is not dominant. 
 Index `i = 2` is not dominant as there are no elements to its right. Thus, the answer is 1.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Dominant Indices**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [5,4,3]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** At index `i = 0`, the value 5 is dominant as `5 > average(4, 3) = 3.5`. 
 At index `i = 1`, the value 4 is dominant over the subarray `[3]`. 
 Index `i = 2` is not dominant as there are no elements to its right. Thus, the answer is 2.

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
    def dominantIndices(self, nums: List[int]) -> int:
        ans = 0
        suffix_sum = 0
        count = 0
        for i in range(len(nums) - 1, -1, -1):
            if count > 0 and nums[i] * count > suffix_sum:
                ans += 1
            suffix_sum += nums[i]
            count += 1
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
- [3234. Count the Number of Substrings With Dominant Ones](../../3001-3500/3234-count-the-number-of-substrings-with-dominant-ones/)
- [3997. Count Dominant Nodes in a Binary Tree](../../3501-4000/3997-count-dominant-nodes-in-a-binary-tree/)
- [2089. Find Target Indices After Sorting Array](../../2001-2500/2089-find-target-indices-after-sorting-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-dominant-indices/)
