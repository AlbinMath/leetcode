# LeetCode 3859: Count Subarrays With K Distinct Integers

**LeetCode Problem #3859 — Count Subarrays With K Distinct Integers**
Solve LeetCode Count Subarrays With K Distinct Integers using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Subarrays With K Distinct Integers |
| LeetCode | #3859 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and two integers `k` and `m`.

Return an integer denoting the count of ** subarrays ** of `nums` such that:

The subarray contains **exactly** `k` **distinct** integers. 
 Within the subarray, each **distinct** integer appears **at least** `m` times.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k, m <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,2,1,2,2], k = 2, m = 2`
- **Output:** `2`
- **Explanation:** The possible subarrays with `k = 2` distinct integers, each appearing at least `m = 2` times are: 

 
 
 
 Subarray 
 Distinct 
 numbers 
 Frequency 
 
 
 
 
 [1, 2, 1, 2] 
 {1, 2} &rarr; 2 
 {1: 2, 2: 2} 
 
 
 [1, 2, 1, 2, 2] 
 {1, 2} &rarr; 2 
 {1: 2, 2: 3} 
 
 
 

 Thus, the answer is 2.

### Example 2
- **Input:** `nums = [3,1,2,4], k = 2, m = 1`
- **Output:** `3`
- **Explanation:** The possible subarrays with `k = 2` distinct integers, each appearing at least `m = 1` times are: 

 
 
 
 Subarray 
 Distinct 
 numbers 
 Frequency 
 
 
 
 
 [3, 1] 
 {3, 1} &rarr; 2 
 {3: 1, 1: 1} 
 
 
 [1, 2] 
 {1, 2} &rarr; 2 
 {1: 1, 2: 1} 
 
 
 [2, 4] 
 {2, 4} &rarr; 2 
 {2: 1, 4: 1} 
 
 
 

 Thus, the answer is 3.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Count Subarrays With K Distinct Integers**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1,2,2], k = 2, m = 2`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The possible subarrays with `k = 2` distinct integers, each appearing at least `m = 2` times are: 

 
 
 
 Subarray 
 Distinct 
 numbers 
 Frequency 
 
 
 
 
 [1, 2, 1, 2] 
 {1, 2} &rarr; 2 
 {1: 2, 2: 2} 
 
 
 [1, 2, 1, 2, 2] 
 {1, 2} &rarr; 2 
 {1: 2, 2: 3} 
 
 
 

 Thus, the answer is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int, m: int) -> int:
        cA = defaultdict(int); dA = 0; lo = 0     # smallest l with distinct <= k
        cB = defaultdict(int); dB = 0; lb = 0     # smallest l with distinct <= k-1
        c3 = defaultdict(int); good = 0; q = 0    # window [q, r], good = values with count >= m
        ans = 0

        for r, x in enumerate(nums):
            if cA[x] == 0: dA += 1
            cA[x] += 1
            while dA > k:
                y = nums[lo]
                cA[y] -= 1
                if cA[y] == 0: dA -= 1
                lo += 1

            if cB[x] == 0: dB += 1
            cB[x] += 1
            while dB > k - 1:
                y = nums[lb]
                cB[y] -= 1
                if cB[y] == 0: dB -= 1
                lb += 1
            hi = lb - 1

            c3[x] += 1
            if c3[x] == m: good += 1
            if good >= k:
                # advance q while removing nums[q] still leaves good >= k
                while True:
                    v = nums[q]
                    if c3[v] == m and good <= k:
                        break
                    if c3[v] == m:
                        good -= 1
                    c3[v] -= 1
                    q += 1
                top = min(hi, q)
                if top >= lo:
                    ans += top - lo + 1
        return ans
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [992. Subarrays with K Different Integers](../../1001-1500/1034-subarrays-with-k-different-integers/)
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2394-count-subarrays-with-score-less-than-k/)
- [2962. Count Subarrays Where Max Element Appears at Least K Times](../../3001-3500/3213-count-subarrays-where-max-element-appears-at-least-k-times/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/)
