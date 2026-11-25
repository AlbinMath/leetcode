# LeetCode 1722: Minimize Hamming Distance After Swap Operations

**LeetCode Problem #1722 — Minimize Hamming Distance After Swap Operations**
Solve LeetCode Minimize Hamming Distance After Swap Operations using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimize Hamming Distance After Swap Operations |
| LeetCode | #1722 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays, `source` and `target`, both of length `n`. You are also given an array `allowedSwaps` where each `allowedSwaps[i] = [a_i, b_i]` indicates that you are allowed to swap the elements at index `a_i` and index `b_i` **(0-indexed)** of array `source`. Note that you can swap elements at a specific pair of indices **multiple** times and in **any** order.

The **Hamming distance** of two arrays of the same length, `source` and `target`, is the number of positions where the elements are different. Formally, it is the number of indices `i` for `0 <= i <= n-1` where `source[i] != target[i]` **(0-indexed)**.

Return *the **minimum Hamming distance** of *`source`* and *`target`* after performing **any** amount of swap operations on array *`source`*.*

## Constraints
- `n == source.length == target.length`
- `1 <= n <= 10^5`
- `1 <= source[i], target[i] <= 10^5`
- `0 <= allowedSwaps.length <= 10^5`
- `allowedSwaps[i].length == 2`
- `0 <= a_i, b_i <= n - 1`
- `a_i != b_i`

## Examples
### Example 1
- **Input:** `source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]`
- **Output:** `1`
- **Explanation:** source can be transformed the following way:
- Swap indices 0 and 1: source = [ 2 , 1 ,3,4]
- Swap indices 2 and 3: source = [2,1, 4 , 3 ]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.

### Example 2
- **Input:** `source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []`
- **Output:** `2`
- **Explanation:** There are no allowed swaps.
The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.

### Example 3
- **Input:** `source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]`
- **Output:** `0`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimize Hamming Distance After Swap Operations**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** source can be transformed the following way:
- Swap indices 0 and 1: source = [ 2 , 1 ,3,4]
- Swap indices 2 and 3: source = [2,1, 4 , 3 ]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.

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
from collections import defaultdict, Counter
from typing import List

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry

        # 1. Group indices into components
        for u, v in allowedSwaps:
            union(u, v)

        # 2. Count frequencies of source elements in each component
        component_counts = defaultdict(Counter)
        for i in range(n):
            root = find(i)
            component_counts[root][source[i]] += 1

        # 3. Match with target elements
        hamming_distance = 0
        for i in range(n):
            root = find(i)
            val = target[i]
            if component_counts[root][val] > 0:
                component_counts[root][val] -= 1
            else:
                hamming_distance += 1

        return hamming_distance
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
- [461. Hamming Distance](../../0001-0500/0461-hamming-distance/)
- [477. Total Hamming Distance](../../0001-0500/0477-total-hamming-distance/)
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/)
