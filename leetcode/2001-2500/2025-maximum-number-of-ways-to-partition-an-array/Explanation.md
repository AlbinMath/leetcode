# LeetCode 2025: Maximum Number of Ways to Partition an Array

**LeetCode Problem #2025 — Maximum Number of Ways to Partition an Array**
Solve LeetCode Maximum Number of Ways to Partition an Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Ways to Partition an Array |
| LeetCode | #2025 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums` of length `n`. The number of ways to **partition** `nums` is the number of `pivot` indices that satisfy both conditions:

`1 <= pivot < n` 
 `nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]`

You are also given an integer `k`. You can choose to change the value of **one** element of `nums` to `k`, or to leave the array **unchanged**.

Return *the **maximum** possible number of ways to **partition** *`nums`* to satisfy both conditions after changing **at most** one element*.

## Constraints
- `n == nums.length`
- `2 <= n <= 10^5`
- `-10^5 <= k, nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [2,-1,2], k = 3`
- **Output:** `1`
- **Explanation:** One optimal approach is to change nums[0] to k. The array becomes [

### Example 2
- **Input:** `nums = [0,0,0], k = 1`
- **Output:** `2`
- **Explanation:** The optimal approach is to leave the array unchanged.
There are two ways to partition the array:
- For pivot = 1, we have the partition [0 | 0,0]: 0 == 0 + 0.
- For pivot = 2, we have the partition [0,0 | 0]: 0 + 0 == 0.

### Example 3
- **Input:** `nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33`
- **Output:** `4`
- **Explanation:** One optimal approach is to change nums[2] to k. The array becomes [22,4,

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Number of Ways to Partition an Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,-1,2], k = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** One optimal approach is to change nums[0] to k. The array becomes [

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

class Solution(object):
    def waysToPartition(self, nums, k):
        n = len(nums)
        total = sum(nums)
        
        left = Counter()
        right = Counter()
        
        pref = 0
        for i in range(n - 1):
            pref += nums[i]
            right[total - 2 * pref] += 1
            
        ans = right[0]
        
        pref = 0
        for i in range(n):
            d = k - nums[i]
            ans = max(ans, left[-d] + right[d])
            
            if i < n - 1:
                pref += nums[i]
                diff = total - 2 * pref
                right[diff] -= 1
                left[diff] += 1
                
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
- [1569. Number of Ways to Reorder Array to Get Same BST](../../1501-2000/1569-number-of-ways-to-reorder-array-to-get-same-bst/)
- [3630. Partition Array for Maximum XOR and AND](../../3501-4000/3630-partition-array-for-maximum-xor-and-and/)
- [2341. Maximum Number of Pairs in Array](../../2001-2500/2341-maximum-number-of-pairs-in-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/)
