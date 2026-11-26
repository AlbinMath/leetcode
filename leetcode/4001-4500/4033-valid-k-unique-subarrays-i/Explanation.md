# LeetCode 4033: Valid K-Unique Subarrays I

**LeetCode Problem #4033 — Valid K-Unique Subarrays I**
Solve LeetCode Valid K-Unique Subarrays I using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Valid K-Unique Subarrays I |
| LeetCode | #4033 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]` represents the **subarray** `nums[l_i..r_i]`.

For each query, the **subarray** `nums[l_i..r_i]` is considered **valid** if:

It contains **exactly** `k` **distinct** numbers, and 
 The **frequency** of every number in the **subarray** is **even**.

Return a boolean array `ans`, where `ans[i]` is `true` if `nums[l_i..r_i]` is **valid**, and `false` otherwise.

## Constraints
- `2 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= n`
- `1 <= queries.length <= 10^5`
- `queries[i] == [l_i, r_i]`
- `0 <= l_i < r_i <= n - 1`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,1], k = 2, queries = [[0,1],[0,3],[1,2]]`
- **Output:** `[false,true,false]`
- **Explanation:** `i` 
 `[l_i, r_i]` 
 Subarray 
 Unique numbers 
 Frequency 
 Validity check 
 
 
 0 
 [0, 1] 
 [1, 2] 
 {1, 2} &rarr; 2 
 {1: 1, 2: 1} 
 `false`: Element counts are not even. 
 
 
 1 
 [0, 3] 
 [1, 2, 2, 1] 
 {1, 2} &rarr; 2 
 {1: 2, 2: 2} 
 `true`: Exactly `k = 2` distinct elements, all appear an even number of times. 
 
 
 2 
 [1, 2] 
 [2, 2] 
 {2} &rarr; 1 
 {2: 2} 
 `false`: Number of distinct elements is less than `k = 2`. 
 
 
 

 Thus, `ans = [false, true, false]`.

### Example 2
- **Input:** `nums = [3,3,3], k = 1, queries = [[1,2],[0,2]]`
- **Output:** `[true,false]`
- **Explanation:** `i` 
 `[l_i, r_i]` 
 Subarray 
 Unique numbers 
 Frequency 
 Validity check 
 
 
 0 
 [1, 2] 
 [3, 3] 
 {3} &rarr; 1 
 {3: 2} 
 `true`: Exactly `k = 1` distinct element, appears an even number of times. 
 
 
 1 
 [0, 2] 
 [3, 3, 3] 
 {3} &rarr; 1 
 {3: 3} 
 `false`: 3 does not appear an even number of times. 
 
 
 

 Thus, `ans = [true, false]`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Valid K-Unique Subarrays I**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,1], k = 2, queries = [[0,1],[0,3],[1,2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[false,true,false]`.
4. **Verification:** `i` 
 `[l_i, r_i]` 
 Subarray 
 Unique numbers 
 Frequency 
 Validity check 
 
 
 0 
 [0, 1] 
 [1, 2] 
 {1, 2} &rarr; 2 
 {1: 1, 2: 1} 
 `false`: Element counts are not even. 
 
 
 1 
 [0, 3] 
 [1, 2, 2, 1] 
 {1, 2} &rarr; 2 
 {1: 2, 2: 2} 
 `true`: Exactly `k = 2` distinct elements, all appear an even number of times. 
 
 
 2 
 [1, 2] 
 [2, 2] 
 {2} &rarr; 1 
 {2: 2} 
 `false`: Number of distinct elements is less than `k = 2`. 
 
 
 

 Thus, `ans = [false, true, false]`.

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
    def validSubarrays(self, nums, k, queries):
        n = len(nums)
        q = len(queries)
        block = max(1, int(n ** 0.5))

        order = sorted(
            [(l, r, i) for i, (l, r) in enumerate(queries)],
            key=lambda x: (
                x[0] // block,
                x[1] if (x[0] // block) % 2 == 0 else -x[1]
            )
        )

        freq = [0] * (max(nums) + 1)
        distinct = 0
        odd_freq = 0
        left, right = 0, -1
        ans = [False] * q

        for l, r, idx in order:
            while left > l:
                left -= 1
                x = nums[left]
                if freq[x] == 0:
                    distinct += 1
                if freq[x] % 2 == 0:
                    odd_freq += 1
                else:
                    odd_freq -= 1
                freq[x] += 1

            while right < r:
                right += 1
                x = nums[right]
                if freq[x] == 0:
                    distinct += 1
                if freq[x] % 2 == 0:
                    odd_freq += 1
                else:
                    odd_freq -= 1
                freq[x] += 1

            while left < l:
                x = nums[left]
                odd_freq += -1 if freq[x] % 2 else 1
                freq[x] -= 1
                if freq[x] == 0:
                    distinct -= 1
                left += 1

            while right > r:
                x = nums[right]
                odd_freq += -1 if freq[x] % 2 else 1
                freq[x] -= 1
                if freq[x] == 0:
                    distinct -= 1
                right -= 1

            ans[idx] = (distinct == k and odd_freq == 0)

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
- [992. Subarrays with K Different Integers](../../0501-1000/0992-subarrays-with-k-different-integers/)
- [2261. K Divisible Elements Subarrays](../../2001-2500/2261-k-divisible-elements-subarrays/)
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2302-count-subarrays-with-score-less-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/valid-k-unique-subarrays-i/)
