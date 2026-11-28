# LeetCode 3488: Closest Equal Element Queries

**LeetCode Problem #3488 — Closest Equal Element Queries**
Solve LeetCode Closest Equal Element Queries using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Closest Equal Element Queries |
| LeetCode | #3488 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **circular** array `nums` and an array `queries`.

For each query `i`, you have to find the following:

The **minimum** distance between the element at index `queries[i]` and **any** other index `j` in the **circular** array, where `nums[j] == nums[queries[i]]`. If no such index exists, the answer for that query should be -1.

Return an array `answer` of the **same** size as `queries`, where `answer[i]` represents the result for query `i`.

## Constraints
- `1 <= queries.length <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`
- `0 <= queries[i] < nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,3,1,4,1,3,2], queries = [0,3,5]`
- **Output:** `[2,-1,3]`
- **Explanation:** Query 0: The element at `queries[0] = 0` is `nums[0] = 1`. The nearest index with the same value is 2, and the distance between them is 2. 
 Query 1: The element at `queries[1] = 3` is `nums[3] = 4`. No other index contains 4, so the result is -1. 
 Query 2: The element at `queries[2] = 5` is `nums[5] = 3`. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: `5 -> 6 -> 0 -> 1`).

### Example 2
- **Input:** `nums = [1,2,3,4], queries = [0,1,2,3]`
- **Output:** `[-1,-1,-1,-1]`
- **Explanation:** Each value in `nums` is unique, so no index shares the same value as the queried element. This results in -1 for all queries.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Closest Equal Element Queries**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,1,4,1,3,2], queries = [0,3,5]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,-1,3]`.
4. **Verification:** Query 0: The element at `queries[0] = 0` is `nums[0] = 1`. The nearest index with the same value is 2, and the distance between them is 2. 
 Query 1: The element at `queries[1] = 3` is `nums[3] = 4`. No other index contains 4, so the result is -1. 
 Query 2: The element at `queries[2] = 5` is `nums[5] = 3`. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: `5 -> 6 -> 0 -> 1`).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import defaultdict
from typing import List

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        ans = [-1] * n
        for lst in pos.values():
            m = len(lst)
            if m == 1:
                continue
            for k, i in enumerate(lst):
                best = n
                for j in (lst[k - 1], lst[(k + 1) % m]):
                    d = abs(i - j)
                    best = min(best, d, n - d)
                ans[i] = best

        return [ans[q] for q in queries]
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [2476. Closest Nodes Queries in a Binary Search Tree](../../2001-2500/2476-closest-nodes-queries-in-a-binary-search-tree/)
- [416. Partition Equal Subset Sum](../../0001-0500/0416-partition-equal-subset-sum/)
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/closest-equal-element-queries/)
