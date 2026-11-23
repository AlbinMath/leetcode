# LeetCode 886: Possible Bipartition

**LeetCode Problem #886 — Possible Bipartition**
Solve LeetCode Possible Bipartition using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Possible Bipartition |
| LeetCode | #886 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
We want to split a group of `n` people (labeled from `1` to `n`) into two groups of **any size**. Each person may dislike some other people, and they should not go into the same group.

Given the integer `n` and the array `dislikes` where `dislikes[i] = [a_i, b_i]` indicates that the person labeled `a_i` does not like the person labeled `b_i`, return `true` *if it is possible to split everyone into two groups in this way*.

## Constraints
- `1 <= n <= 2000`
- `0 <= dislikes.length <= 10^4`
- `dislikes[i].length == 2`
- `1 <= a_i < b_i <= n`
- All the pairs of `dislikes` are **unique**.

## Examples
### Example 1
- **Input:** `n = 4, dislikes = [[1,2],[1,3],[2,4]]`
- **Output:** `true`
- **Explanation:** The first group has [1,4], and the second group has [2,3].

### Example 2
- **Input:** `n = 3, dislikes = [[1,2],[1,3],[2,3]]`
- **Output:** `false`
- **Explanation:** We need at least 3 groups to divide them. We cannot put them in two groups.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Possible Bipartition**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, dislikes = [[1,2],[1,3],[2,4]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The first group has [1,4], and the second group has [2,3].

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
from collections import deque, defaultdict
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Build adjacency graph
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = [0] * (n + 1)  # 0: uncolored, 1: group 1, -1: group 2

        for i in range(1, n + 1):
            if color[i] != 0:
                continue

            # Start BFS for uncolored component
            queue = deque([i])
            color[i] = 1

            while queue:
                u = queue.popleft()
                for neighbor in graph[u]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[u]
                        queue.append(neighbor)
                    elif color[neighbor] == color[u]:
                        return False

        return True
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
- [894. All Possible Full Binary Trees](../../0501-1000/0930-all-possible-full-binary-trees/)
- [1162. As Far from Land as Possible](../../1001-1500/1117-as-far-from-land-as-possible/)
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/possible-bipartition/)
