# LeetCode 2977: Minimum Cost to Convert String II

**LeetCode Problem #2977 — Minimum Cost to Convert String II**
Solve LeetCode Minimum Cost to Convert String II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Convert String II |
| LeetCode | #2977 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two **0-indexed** strings `source` and `target`, both of length `n` and consisting of **lowercase** English characters. You are also given two **0-indexed** string arrays `original` and `changed`, and an integer array `cost`, where `cost[i]` represents the cost of converting the string `original[i]` to the string `changed[i]`.

You start with the string `source`. In one operation, you can pick a **substring** `x` from the string, and change it to `y` at a cost of `z` **if** there exists **any** index `j` such that `cost[j] == z`, `original[j] == x`, and `changed[j] == y`. You are allowed to do **any** number of operations, but any pair of operations must satisfy **either** of these two conditions:

The substrings picked in the operations are `source[a..b]` and `source[c..d]` with either `b < c` **or** `d < a`. In other words, the indices picked in both operations are **disjoint**. 
 The substrings picked in the operations are `source[a..b]` and `source[c..d]` with `a == c` **and** `b == d`. In other words, the indices picked in both operations are **identical**.

Return *the **minimum** cost to convert the string *`source`* to the string *`target`* using **any** number of operations*. *If it is impossible to convert* `source` *to* `target`,* return* `-1`.

**Note** that there may exist indices `i`, `j` such that `original[j] == original[i]` and `changed[j] == changed[i]`.

## Constraints
- `1 <= source.length == target.length <= 1000`
- `source`, `target` consist only of lowercase English characters.
- `1 <= cost.length == original.length == changed.length <= 100`
- `1 <= original[i].length == changed[i].length <= source.length`
- `original[i]`, `changed[i]` consist only of lowercase English characters.
- `original[i] != changed[i]`
- `1 <= cost[i] <= 10^6`

## Examples
### Example 1
- **Input:** `source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]`
- **Output:** `28`
- **Explanation:** To convert "abcd" to "acbe", do the following operations:
- Change substring source[1..1] from "b" to "c" at a cost of 5.
- Change substring source[2..2] from "c" to "e" at a cost of 1.
- Change substring source[2..2] from "e" to "b" at a cost of 2.
- Change substring source[3..3] from "d" to "e" at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28. 
It can be shown that this is the minimum possible cost.

### Example 2
- **Input:** `source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]`
- **Output:** `9`
- **Explanation:** To convert "abcdefgh" to "acdeeghh", do the following operations:
- Change substring source[1..3] from "bcd" to "cde" at a cost of 1.
- Change substring source[5..7] from "fgh" to "thh" at a cost of 3. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation.
- Change substring source[5..7] from "thh" to "ghh" at a cost of 5. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
The total cost incurred is 1 + 3 + 5 = 9.
It can be shown that this is the minimum possible cost.

### Example 3
- **Input:** `source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"], cost = [100,1578]`
- **Output:** `-1`
- **Explanation:** It is impossible to convert "abcdefgh" to "addddddd".
If you select substring source[1..3] as the first operation to change "abcdefgh" to "adddefgh", you cannot select substring source[3..7] as the second operation because it has a common index, 3, with the first operation.
If you select substring source[3..7] as the first operation to change "abcdefgh" to "abcddddd", you cannot select substring source[1..3] as the second operation because it has a common index, 3, with the first operation.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Cost to Convert String II**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `28`.
4. **Verification:** To convert "abcd" to "acbe", do the following operations:
- Change substring source[1..1] from "b" to "c" at a cost of 5.
- Change substring source[2..2] from "c" to "e" at a cost of 1.
- Change substring source[2..2] from "e" to "b" at a cost of 2.
- Change substring source[3..3] from "d" to "e" at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28. 
It can be shown that this is the minimum possible cost.

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
from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        words = set(original + changed)
        ids = {w: i for i, w in enumerate(words)}
        m = len(ids)
        g = [[] for _ in range(m)]
        for a, b, c in zip(original, changed, cost):
            g[ids[a]].append((ids[b], c))

        d = [[float('inf')] * m for _ in range(m)]
        for s in range(m):
            d[s][s] = 0
            h = [(0, s)]
            while h:
                c, u = heappop(h)
                if c != d[s][u]:
                    continue
                for v, w in g[u]:
                    nc = c + w
                    if nc < d[s][v]:
                        d[s][v] = nc
                        heappush(h, (nc, v))

        lens = set(map(len, words))
        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == float('inf'):
                continue
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            for l in lens:
                j = i + l
                if j > n:
                    continue
                a, b = source[i:j], target[i:j]
                if a in ids and b in ids:
                    c = d[ids[a]][ids[b]]
                    if c < float('inf'):
                        dp[j] = min(dp[j], dp[i] + c)

        return dp[n] if dp[n] < float('inf') else -1
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
- [2976. Minimum Cost to Convert String I](../../2501-3000/2976-minimum-cost-to-convert-string-i/)
- [3864. Minimum Cost to Partition a Binary String](../../3501-4000/3864-minimum-cost-to-partition-a-binary-string/)
- [2027. Minimum Moves to Convert String](../../2001-2500/2027-minimum-moves-to-convert-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/)
