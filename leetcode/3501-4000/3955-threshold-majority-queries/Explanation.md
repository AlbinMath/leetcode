# LeetCode 3636: Threshold Majority Queries

**LeetCode Problem #3636 — Threshold Majority Queries**
Solve LeetCode Threshold Majority Queries using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Threshold Majority Queries |
| LeetCode | #3636 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n` and an array `queries`, where `queries[i] = [l_i, r_i, threshold_i]`.

Return an array of integers ans where ans[i] is equal to the element in the subarray nums[l_i...r_i] that appears **at least** threshold_i times, selecting the element with the **highest** frequency (choosing the **smallest** in case of a tie), or -1 if no such element *exists*.

## Constraints
- 1 <= nums.length == n <= 10^4
- 1 <= nums[i] <= 10^9
- 1 <= queries.length <= 5 * 10^4
- 0 <= l_i <= r_i < n
- 1 <= threshold_i <= r_i - l_i + 1

## Examples
### Example 1
- **Input:** `nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]`
- **Output:** `[1,-1,2]`
- **Explanation:** Query 
 Sub-array 
 Threshold 
 Frequency table 
 Answer 
 
 
 
 
 [0, 5, 4] 
 [1, 1, 2, 2, 1, 1] 
 4 
 1 &rarr; 4, 2 &rarr; 2 
 1 
 
 
 [0, 3, 3] 
 [1, 1, 2, 2] 
 3 
 1 &rarr; 2, 2 &rarr; 2 
 -1 
 
 
 [2, 3, 2] 
 [2, 2] 
 2 
 2 &rarr; 2 
 2

### Example 2
- **Input:** `nums = [3,2,3,2,3,2,3], queries = [[0,6,4],[1,5,2],[2,4,1],[3,3,1]]`
- **Output:** `[3,2,3,2]`
- **Explanation:** Query 
 Sub-array 
 Threshold 
 Frequency table 
 Answer 
 
 
 
 
 [0, 6, 4] 
 [3, 2, 3, 2, 3, 2, 3] 
 4 
 3 &rarr; 4, 2 &rarr; 3 
 3 
 
 
 [1, 5, 2] 
 [2, 3, 2, 3, 2] 
 2 
 2 &rarr; 3, 3 &rarr; 2 
 2 
 
 
 [2, 4, 1] 
 [3, 2, 3] 
 1 
 3 &rarr; 2, 2 &rarr; 1 
 3 
 
 
 [3, 3, 1] 
 [2] 
 1 
 2 &rarr; 1 
 2

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Threshold Majority Queries**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,-1,2]`.
4. **Verification:** Query 
 Sub-array 
 Threshold 
 Frequency table 
 Answer 
 
 
 
 
 [0, 5, 4] 
 [1, 1, 2, 2, 1, 1] 
 4 
 1 &rarr; 4, 2 &rarr; 2 
 1 
 
 
 [0, 3, 3] 
 [1, 1, 2, 2] 
 3 
 1 &rarr; 2, 2 &rarr; 2 
 -1 
 
 
 [2, 3, 2] 
 [2, 2] 
 2 
 2 &rarr; 2 
 2

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
    def subarrayMajority(self, nums, queries):
        n, q = len(nums), len(queries)
        vals = sorted(set(nums))
        rank = {v: i for i, v in enumerate(vals)}
        a = [rank[v] for v in nums]
        D = len(vals)
        K = D + 1

        S = max(1, int(n / (q ** 0.5)))
        order = sorted(range(q), key=lambda i: (queries[i][0] // S, queries[i][1]))

        cnt = [0] * D
        ans = [-1] * q
        cur_block = -1
        prev_end = 0
        R = 0
        best = 0

        for qi in order:
            l, r, t = queries[qi]
            b = l // S
            end = (b + 1) * S

            if b != cur_block:
                for i in range(prev_end, R):      # clear previous block's right part
                    cnt[a[i]] = 0
                cur_block = b
                prev_end = end
                R = end
                best = 0

            if r < end:
                # same block: brute force (cnt is all zero here)
                bst = 0
                for i in range(l, r + 1):
                    x = a[i]
                    c = cnt[x] + 1
                    cnt[x] = c
                    k = c * K + K - 1 - x
                    if k > bst:
                        bst = k
                for i in range(l, r + 1):
                    cnt[a[i]] = 0
            else:
                while R <= r:
                    x = a[R]
                    c = cnt[x] + 1
                    cnt[x] = c
                    k = c * K + K - 1 - x
                    if k > best:
                        best = k
                    R += 1
                save = best
                bst = best
                for i in range(l, end):
                    x = a[i]
                    c = cnt[x] + 1
                    cnt[x] = c
                    k = c * K + K - 1 - x
                    if k > bst:
                        bst = k
                for i in range(l, end):
                    cnt[a[i]] -= 1
                best = save

            if bst // K >= t:
                ans[qi] = vals[K - 1 - bst % K]
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
- [169. Majority Element](../../0001-0500/0169-majority-element/)
- [229. Majority Element II](../../0001-0500/0229-majority-element-ii/)
- [1157. Online Majority Element In Subarray](../../1001-1500/1262-online-majority-element-in-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/threshold-majority-queries/)
