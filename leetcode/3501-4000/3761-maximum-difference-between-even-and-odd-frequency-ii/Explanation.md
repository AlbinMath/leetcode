# LeetCode 3445: Maximum Difference Between Even and Odd Frequency II

**LeetCode Problem #3445 — Maximum Difference Between Even and Odd Frequency II**
Solve LeetCode Maximum Difference Between Even and Odd Frequency II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Difference Between Even and Odd Frequency II |
| LeetCode | #3445 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` and an integer `k`. Your task is to find the **maximum** difference between the frequency of **two** characters, `freq[a] - freq[b]`, in a substring `subs` of `s`, such that:

`subs` has a size of **at least** `k`. 
 Character `a` has an *odd frequency* in `subs`. 
 Character `b` has a **non-zero** *even frequency* in `subs`.

Return the **maximum** difference.

**Note** that `subs` can contain more than 2 **distinct** characters.

## Constraints
- `3 <= s.length <= 3 * 10^4`
- `s` consists only of digits `'0'` to `'4'`.
- The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
- `1 <= k <= s.length`

## Examples
### Example 1
- **Input:** `s = "12233", k = 4`
- **Output:** `-1`
- **Explanation:** For the substring `"12233"`, the frequency of `'1'` is 1 and the frequency of `'3'` is 2. The difference is `1 - 2 = -1`.

### Example 2
- **Input:** `s = "1122211", k = 3`
- **Output:** `1`
- **Explanation:** For the substring `"11222"`, the frequency of `'2'` is 3 and the frequency of `'1'` is 2. The difference is `3 - 2 = 1`.

### Example 3
- **Input:** `s = "110", k = 3`
- **Output:** `-1`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Difference Between Even and Odd Frequency II**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "12233", k = 4`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `-1`.
4. **Verification:** For the substring `"12233"`, the frequency of `'1'` is 1 and the frequency of `'3'` is 2. The difference is `1 - 2 = -1`.

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
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        NEG = float('-inf')
        ans = NEG

        for a in "01234":
            for b in "01234":
                if a == b:
                    continue
                pa = [0] * (n + 1)
                pb = [0] * (n + 1)
                for i, ch in enumerate(s):
                    pa[i + 1] = pa[i] + (ch == a)
                    pb[i + 1] = pb[i] + (ch == b)

                INF = float('inf')
                best = [INF] * 4   # index = (pa%2)*2 + (pb%2) of left endpoint
                l = 0
                for r in range(k, n + 1):
                    while r - l >= k and pb[r] - pb[l] >= 2:
                        st = (pa[l] & 1) * 2 + (pb[l] & 1)
                        v = pa[l] - pb[l]
                        if v < best[st]:
                            best[st] = v
                        l += 1
                    need = ((pa[r] & 1) ^ 1) * 2 + (pb[r] & 1)
                    if best[need] != INF:
                        ans = max(ans, pa[r] - pb[r] - best[need])
        return ans
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
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1092-maximum-difference-between-node-and-ancestor/)
- [1913. Maximum Product Difference Between Two Pairs](../../2001-2500/2042-maximum-product-difference-between-two-pairs/)
- [328. Odd Even Linked List](../../0001-0500/0328-odd-even-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/)
