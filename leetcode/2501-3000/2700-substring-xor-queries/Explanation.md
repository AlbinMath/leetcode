# LeetCode 2564: Substring XOR Queries

**LeetCode Problem #2564 — Substring XOR Queries**
Solve LeetCode Substring XOR Queries using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Substring XOR Queries |
| LeetCode | #2564 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **binary string** `s`, and a **2D** integer array `queries` where `queries[i] = [first_i, second_i]`.

For the `i^th` query, find the **shortest substring** of `s` whose **decimal value**, `val`, yields `second_i` when **bitwise XORed** with `first_i`. In other words, `val ^ first_i == second_i`.

The answer to the `i^th` query is the endpoints (**0-indexed**) of the substring `[left_i, right_i]` or `[-1, -1]` if no such substring exists. If there are multiple answers, choose the one with the **minimum** `left_i`.

*Return an array* `ans` *where* `ans[i] = [left_i, right_i]` *is the answer to the* `i^th` *query.*

A **substring** is a contiguous non-empty sequence of characters within a string.

## Constraints
- `1 <= s.length <= 10^4`
- `s[i]` is either `'0'` or `'1'`.
- `1 <= queries.length <= 10^5`
- `0 <= first_i, second_i <= 10^9`

## Examples
### Example 1
- **Input:** `s = "101101", queries = [[0,5],[1,2]]`
- **Output:** `[[0,2],[2,3]]`
- **Explanation:** For the first query the substring in range `[0,2]` is

### Example 2
- **Input:** `s = "0101", queries = [[12,8]]`
- **Output:** `[[-1,-1]]`
- **Explanation:** In this example there is no substring that answers the query, hence `[-1,-1] is returned`.

### Example 3
- **Input:** `s = "1", queries = [[4,5]]`
- **Output:** `[[0,0]]`
- **Explanation:** For this example, the substring in range `[0,0]` has a decimal value of

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Substring XOR Queries**, we observe the problem requirements and utilize the **Dynamic Programming** technique. By maintaining a **DP Table / Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **DP Table / Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "101101", queries = [[0,5],[1,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[0,2],[2,3]]`.
4. **Verification:** For the first query the substring in range `[0,2]` is

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
class Solution(object):
    def substringXorQueries(self, s, queries):
        n = len(s)
        best = {}  # value -> (length, left, right)
        for i in range(n):
            if s[i] == '0':
                if 0 not in best or 1 < best[0][0]:
                    best[0] = (1, i, i)
                continue
            v = 0
            for j in range(i, min(n, i + 31)):
                v = (v << 1) | (s[j] == '1')
                L = j - i + 1
                if v not in best or L < best[v][0]:
                    best[v] = (L, i, j)

        res = []
        for a, b in queries:
            t = a ^ b
            if t in best:
                res.append([best[t][1], best[t][2]])
            else:
                res.append([-1, -1])
        return res
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
- [1310. XOR Queries of a Subarray](../../1001-1500/1435-xor-queries-of-a-subarray/)
- [3653. XOR After Range Multiplication Queries I](../../3501-4000/3974-xor-after-range-multiplication-queries-i/)
- [3655. XOR After Range Multiplication Queries II](../../3501-4000/3975-xor-after-range-multiplication-queries-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/substring-xor-queries/)
