# LeetCode 1743: Restore the Array From Adjacent Pairs

**LeetCode Problem #1743 — Restore the Array From Adjacent Pairs**
Solve LeetCode Restore the Array From Adjacent Pairs using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Restore the Array From Adjacent Pairs |
| LeetCode | #1743 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is an integer array `nums` that consists of `n` **unique **elements, but you have forgotten it. However, you do remember every pair of adjacent elements in `nums`.

You are given a 2D integer array `adjacentPairs` of size `n - 1` where each `adjacentPairs[i] = [u_i, v_i]` indicates that the elements `u_i` and `v_i` are adjacent in `nums`.

It is guaranteed that every adjacent pair of elements `nums[i]` and `nums[i+1]` will exist in `adjacentPairs`, either as `[nums[i], nums[i+1]]` or `[nums[i+1], nums[i]]`. The pairs can appear **in any order**.

Return *the original array *`nums`*. If there are multiple solutions, return **any of them***.

## Constraints
- `nums.length == n`
- `adjacentPairs.length == n - 1`
- `adjacentPairs[i].length == 2`
- `2 <= n <= 10^5`
- `-10^5 <= nums[i], u_i, v_i <= 10^5`
- There exists some `nums` that has `adjacentPairs` as its pairs.

## Examples
### Example 1
- **Input:** `adjacentPairs = [[2,1],[3,4],[3,2]]`
- **Output:** `[1,2,3,4]`
- **Explanation:** This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.

### Example 2
- **Input:** `adjacentPairs = [[4,-2],[1,4],[-3,1]]`
- **Output:** `[-2,4,1,-3]`
- **Explanation:** There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.

### Example 3
- **Input:** `adjacentPairs = [[100000,-100000]]`
- **Output:** `[100000,-100000]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Restore the Array From Adjacent Pairs**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `adjacentPairs = [[2,1],[3,4],[3,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,4]`.
4. **Verification:** This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            
        # Find either endpoint (degree == 1)
        start = next(node for node, neighbors in graph.items() if len(neighbors) == 1)
        
        n = len(adjacentPairs) + 1
        nums = [start, graph[start][0]]
        
        # Walk along the chain without needing a visited set by avoiding the previous node
        while len(nums) < n:
            prev, curr = nums[-2], nums[-1]
            a, b = graph[curr]
            nums.append(b if a == prev else a)
            
        return nums
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [80. Remove Duplicates from Sorted Array II](../../0001-0500/0080-remove-duplicates-from-sorted-array-ii/)
- [532. K-diff Pairs in an Array](../../0501-1000/0532-k-diff-pairs-in-an-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/)
