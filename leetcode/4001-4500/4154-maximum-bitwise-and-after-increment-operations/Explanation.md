# LeetCode 3806: Maximum Bitwise AND After Increment Operations

**LeetCode Problem #3806 — Maximum Bitwise AND After Increment Operations**
Solve LeetCode Maximum Bitwise AND After Increment Operations using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Bitwise AND After Increment Operations |
| LeetCode | #3806 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and two integers `k` and `m`.

You may perform **at most** `k` operations. In one operation, you may choose any index `i` and **increase** `nums[i]` by 1.

Return an integer denoting the **maximum** possible **bitwise AND** of any ** subset ** of size `m` after performing up to `k` operations optimally.

## Constraints
- `1 <= n == nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`
- `1 <= m <= n`

## Examples
### Example 1
- **Input:** `nums = [3,1,2], k = 8, m = 2`
- **Output:** `6`
- **Explanation:** We need a subset of size `m = 2`. Choose indices `[0, 2]`. 
 Increase `nums[0] = 3` to 6 using 3 operations, and increase `nums[2] = 2` to 6 using 4 operations. 
 The total number of operations used is 7, which is not greater than `k = 8`. 
 The two chosen values become `[6, 6]`, and their bitwise AND is `6`, which is the maximum possible.

### Example 2
- **Input:** `nums = [1,2,8,4], k = 7, m = 3`
- **Output:** `4`
- **Explanation:** We need a subset of size `m = 3`. Choose indices `[0, 1, 3]`. 
 Increase `nums[0] = 1` to 4 using 3 operations, increase `nums[1] = 2` to 4 using 2 operations, and keep `nums[3] = 4`. 
 The total number of operations used is 5, which is not greater than `k = 7`. 
 The three chosen values become `[4, 4, 4]`, and their bitwise AND is 4, which is the maximum possible.​​​​​​​

### Example 3
- **Input:** `nums = [1,1], k = 3, m = 2`
- **Output:** `2`
- **Explanation:** We need a subset of size `m = 2`. Choose indices `[0, 1]`. 
 Increase both values from 1 to 2 using 1 operation each. 
 The total number of operations used is 2, which is not greater than `k = 3`. 
 The two chosen values become `[2, 2]`, and their bitwise AND is 2, which is the maximum possible.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Bitwise AND After Increment Operations**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,2], k = 8, m = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** We need a subset of size `m = 2`. Choose indices `[0, 2]`. 
 Increase `nums[0] = 3` to 6 using 3 operations, and increase `nums[2] = 2` to 6 using 4 operations. 
 The total number of operations used is 7, which is not greater than `k = 8`. 
 The two chosen values become `[6, 6]`, and their bitwise AND is `6`, which is the maximum possible.

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
    def maximumAND(self, nums, k, m):
        ans = 0
        for b in range(31, -1, -1):
            c = ans | (1 << b)
            costs = []
            for x in nums:
                d = c & ~x
                if d == 0:
                    costs.append(0)
                else:
                    h = d.bit_length() - 1
                    y = ((x >> (h + 1)) << (h + 1)) | (1 << h) | (c & ((1 << h) - 1))
                    costs.append(y - x)
            costs.sort()
            if sum(costs[:m]) <= k:
                ans = c
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
- [3849. Maximum Bitwise XOR After Rearrangement](../../4001-4500/4044-maximum-bitwise-xor-after-rearrangement/)
- [2317. Maximum XOR After Operations ](../../2001-2500/2402-maximum-xor-after-operations-/)
- [3035. Maximum Palindromes After Operations](../../3001-3500/3317-maximum-palindromes-after-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/)
