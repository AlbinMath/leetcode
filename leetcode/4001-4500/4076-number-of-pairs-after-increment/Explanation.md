# LeetCode 3943: Number of Pairs After Increment

**LeetCode Problem #3943 — Number of Pairs After Increment**
Solve LeetCode Number of Pairs After Increment using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Pairs After Increment |
| LeetCode | #3943 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2`, and a 2D integer array `queries`.

Each `queries[i]` is one of the following types:

`[1, x, y, val]` &ndash; **Add** `val` to every element in `nums2[x..y]`. 
 `[2, tot]` &ndash; **Compute** the number of pairs `(j, k)` such that `nums1[j] + nums2[k] == tot`.

Return an integer array `answer`, where `answer[j]` is the number of pairs for the `j^th` query of type 2.

## Constraints
- `1 <= nums1.length <= 5`
- `1 <= nums2.length <= 5 * 10^4`
- `1 <= nums1[i], nums2[i] <= 10^5`
- `1 <= queries.length <= 5 * 10^4`
- `queries[i].length == 2 or 4`
 
 `queries[i] == [1, x, y, val], or`
- `queries[i] == [2, tot]`
- `0 <= x <= y < nums2.length`
- `1 <= val <= 10^5`
- `1 <= tot <= 10^9​​​​​​​`

## Examples
### Example 1
- **Input:** `nums1 = [1,2], nums2 = [3,4], queries = [[2,5],[1,0,0,2],[2,5]]`
- **Output:** `[2,1]`
- **Explanation:** `queries[0] = [2, 5]`: Valid pairs are `nums1[0] + nums2[1] = 1 + 4 = 5` and `nums1[1] + nums2[0] = 2 + 3 = 5`. 
 `queries[1] = [1, 0, 0, 2]`: Add 2 to `nums2[0]`, resulting in `nums2 = [5, 4]`. 
 `queries[2] = [2, 5]`: Valid pair is `nums1[0] + nums2[1] = 1 + 4 = 5`. 
 Thus, the `answer = [2, 1]`.

### Example 2
- **Input:** `nums1 = [1,1], nums2 = [2,2,3], queries = [[2,4],[1,0,1,1],[2,4]]`
- **Output:** `[2,6]`
- **Explanation:** `queries[0] = [2, 4]`: Valid pairs are `nums1[0] + nums2[2] = 1 + 3` and `nums1[1] + nums2[2] = 1 + 3`. 
 `queries[1] = [1, 0, 1, 1]`: Add 1 to `nums2[0]` and `nums2[1]`, resulting in `nums2 = [3, 3, 3]`. 
 `queries[2] = [2, 4]`: Every element of `nums1 = [1, 1]` pairs with every element of `nums2 = [3, 3, 3]` as `1 + 3 = 4`. That gives `2 &times; 3 = 6` pairs in total. 
 Thus, the `answer = [2, 6]`.

### Example 3
- **Input:** `nums1 = [2,5,8,4], nums2 = [1,3,8], queries = [[2,9],[1,1,2,1],[2,10]]`
- **Output:** `[1,0]`
- **Explanation:** `queries[0] = [2, 9]`: Only valid pair is `nums1[2] + nums2[0] = 8 + 1 = 9`. 
 `queries[1] = [1, 1, 2, 1]`: Add 1 to `nums2[1]` and `nums2[2]`, resulting in​​​​​​​ `nums2 = [1, 4, 9]`. 
 `queries[2] = [2, 10]`: No pair sums to `10`. 
 Thus, the `answer = [1, 0]`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Pairs After Increment**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2], nums2 = [3,4], queries = [[2,5],[1,0,0,2],[2,5]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1]`.
4. **Verification:** `queries[0] = [2, 5]`: Valid pairs are `nums1[0] + nums2[1] = 1 + 4 = 5` and `nums1[1] + nums2[0] = 2 + 3 = 5`. 
 `queries[1] = [1, 0, 0, 2]`: Add 2 to `nums2[0]`, resulting in `nums2 = [5, 4]`. 
 `queries[2] = [2, 5]`: Valid pair is `nums1[0] + nums2[1] = 1 + 4 = 5`. 
 Thus, the `answer = [2, 1]`.

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
from collections import Counter

class Solution:
    def numberOfPairs(self, nums1, nums2, queries):
        n = len(nums2)
        B = 300
        nb = (n + B - 1) // B

        a = nums2[:]                      # base values (without block lazy)
        lz = [0] * nb
        cnt = [dict() for _ in range(nb)]
        for i, v in enumerate(a):
            d = cnt[i // B]
            d[v] = d.get(v, 0) + 1

        mult = list(Counter(nums1).items())   # (value, multiplicity)

        def partial(b, lo, hi, val):          # inclusive range inside block b
            d = cnt[b]
            for i in range(lo, hi + 1):
                old = a[i]
                d[old] -= 1
                new = old + val
                a[i] = new
                d[new] = d.get(new, 0) + 1

        ans = []
        for q in queries:
            if q[0] == 1:
                _, x, y, val = q
                bx, by = x // B, y // B
                if bx == by:
                    partial(bx, x, y, val)
                else:
                    partial(bx, x, (bx + 1) * B - 1, val)
                    partial(by, by * B, y, val)
                    for b in range(bx + 1, by):
                        lz[b] += val
            else:
                tot = q[1]
                res = 0
                for av, m in mult:
                    t = tot - av
                    s = 0
                    for b in range(nb):
                        s += cnt[b].get(t - lz[b], 0)
                    res += m * s
                ans.append(res)
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
- [1128. Number of Equivalent Domino Pairs](../../1001-1500/1227-number-of-equivalent-domino-pairs/)
- [1481. Least Number of Unique Integers after K Removals](../../1501-2000/1604-least-number-of-unique-integers-after-k-removals/)
- [1512. Number of Good Pairs](../../1501-2000/1635-number-of-good-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-pairs-after-increment/)
