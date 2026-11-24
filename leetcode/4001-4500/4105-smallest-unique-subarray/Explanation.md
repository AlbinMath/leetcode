# LeetCode 3934: Smallest Unique Subarray

**LeetCode Problem #3934 — Smallest Unique Subarray**
Solve LeetCode Smallest Unique Subarray using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Unique Subarray |
| LeetCode | #3934 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Find the **minimum **length of a subarray that is **not** **identical** to any other **subarray** in `nums`.

Return an integer denoting the **minimum possible length** of such a **subarray**.

Two **subarrays** are considered identical if they have the same length and the same elements in corresponding positions.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [3,3,3]`
- **Output:** `3`
- **Explanation:** Subarrays of length 1: `[3]` &rarr; appears 3 times 
 Subarrays of length 2: `[3, 3]` &rarr; appears 2 times 
 Subarrays of length 3: `[3, 3, 3]` &rarr; appears once 
 

 The subarray `[3, 3, 3]` is unique, so the smallest unique subarray length is 3.

### Example 2
- **Input:** `nums = [2,1,2,3,3]`
- **Output:** `1`
- **Explanation:** Subarrays of length 1: 

 
 `[2]` &rarr; appears 2 times 
 `[1]` &rarr; appears once 
 `[3]` &rarr; appears 2 times 
 
The subarray `[1]` is unique, so the smallest unique subarray length is 1.

### Example 3
- **Input:** `nums = [1,1,2,2,1]`
- **Output:** `2`
- **Explanation:** Subarrays of length 1: 

 
 `[1]` &rarr; appears 3 times 
 `[2]` &rarr; appears 2 times 
 

 Subarrays of length 2: 

 
 `[1, 1]` &rarr; appears once 
 `[1, 2]` &rarr; appears once 
 `[2, 2]` &rarr; appears once 
 `[2, 1]` &rarr; appears once 
 
There is at least one subarray of length 2 that is unique, so the smallest unique subarray length is 2.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Smallest Unique Subarray**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,3,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Subarrays of length 1: `[3]` &rarr; appears 3 times 
 Subarrays of length 2: `[3, 3]` &rarr; appears 2 times 
 Subarrays of length 3: `[3, 3, 3]` &rarr; appears once 
 

 The subarray `[3, 3, 3]` is unique, so the smallest unique subarray length is 3.

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

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = [{}]
        link = [-1]
        ln = [0]
        cnt = [0]
        last = 0

        for c in nums:
            cur = len(ln)
            nxt.append({})
            link.append(0)
            ln.append(ln[last] + 1)
            cnt.append(1)
            p = last
            while p != -1 and c not in nxt[p]:
                nxt[p][c] = cur
                p = link[p]
            if p != -1:
                q = nxt[p][c]
                if ln[p] + 1 == ln[q]:
                    link[cur] = q
                else:
                    cl = len(ln)
                    nxt.append(dict(nxt[q]))
                    link.append(link[q])
                    ln.append(ln[p] + 1)
                    cnt.append(0)
                    while p != -1 and nxt[p].get(c) == q:
                        nxt[p][c] = cl
                        p = link[p]
                    link[q] = cl
                    link[cur] = cl
            last = cur

        order = sorted(range(1, len(ln)), key=lambda v: -ln[v])
        for v in order:
            cnt[link[v]] += cnt[v]

        ans = n
        for v in range(1, len(ln)):
            if cnt[v] == 1:
                cand = ln[link[v]] + 1
                if cand < ans:
                    ans = cand
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
- [2841. Maximum Sum of Almost Unique Subarray](../../2501-3000/2954-maximum-sum-of-almost-unique-subarray/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)
- [152. Maximum Product Subarray](../../0001-0500/0152-maximum-product-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-unique-subarray/)
