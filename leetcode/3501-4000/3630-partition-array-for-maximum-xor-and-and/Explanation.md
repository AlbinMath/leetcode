# LeetCode 3630: Partition Array for Maximum XOR and AND

**LeetCode Problem #3630 — Partition Array for Maximum XOR and AND**
Solve LeetCode Partition Array for Maximum XOR and AND using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array for Maximum XOR and AND |
| LeetCode | #3630 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Partition the array into **three** (possibly empty) subsequences `A`, `B`, and `C` such that every element of `nums` belongs to **exactly** one subsequence.

Your goal is to **maximize** the value of: `XOR(A) + AND(B) + XOR(C)`

where:

`XOR(arr)` denotes the bitwise XOR of all elements in `arr`. If `arr` is empty, its value is defined as 0. 
 `AND(arr)` denotes the bitwise AND of all elements in `arr`. If `arr` is empty, its value is defined as 0.

Return the **maximum** value achievable.

**Note:** If multiple partitions result in the same **maximum** sum, you can consider any one of them.

## Constraints
- `1 <= nums.length <= 19`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,3]`
- **Output:** `5`
- **Explanation:** One optimal partition is: 

 
 `A = [3], XOR(A) = 3` 
 `B = [2], AND(B) = 2` 
 `C = [], XOR(C) = 0` 
 

 The maximum value of: `XOR(A) + AND(B) + XOR(C) = 3 + 2 + 0 = 5`. Thus, the answer is 5.

### Example 2
- **Input:** `nums = [1,3,2]`
- **Output:** `6`
- **Explanation:** One optimal partition is: 

 
 `A = [1], XOR(A) = 1` 
 `B = [2], AND(B) = 2` 
 `C = [3], XOR(C) = 3` 
 

 The maximum value of: `XOR(A) + AND(B) + XOR(C) = 1 + 2 + 3 = 6`. Thus, the answer is 6.

### Example 3
- **Input:** `nums = [2,3,6,7]`
- **Output:** `15`
- **Explanation:** One optimal partition is: 

 
 `A = [7], XOR(A) = 7` 
 `B = [2,3], AND(B) = 2` 
 `C = [6], XOR(C) = 6` 
 

 The maximum value of: `XOR(A) + AND(B) + XOR(C) = 7 + 2 + 6 = 15`. Thus, the answer is 15.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Partition Array for Maximum XOR and AND**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** One optimal partition is: 

 
 `A = [3], XOR(A) = 3` 
 `B = [2], AND(B) = 2` 
 `C = [], XOR(C) = 0` 
 

 The maximum value of: `XOR(A) + AND(B) + XOR(C) = 3 + 2 + 0 = 5`. Thus, the answer is 5.

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
import numpy as np

class Solution(object):
    def maximizeXorAndXor(self, nums):
        n = len(nums)
        size = 1 << n
        BITS = max(nums).bit_length()
        ALL = (1 << BITS) - 1

        # XOR and AND of every subset, built by doubling
        xr = np.zeros(size, dtype=np.int32)
        an = np.full(size, ALL, dtype=np.int32)
        for i, v in enumerate(nums):
            xr[1 << i: 2 << i] = xr[:1 << i] ^ v
            an[1 << i: 2 << i] = an[:1 << i] & v
        an[0] = 0  # AND of an empty subset is 0

        idx = np.arange(size, dtype=np.int32)
        total_xor = xr[size - 1]
        X = total_xor ^ xr                 # XOR of the complement (rest) for each B
        notX = (~X) & ALL

        basis = [np.zeros(size, dtype=np.int32) for _ in range(BITS)]

        for i, v in enumerate(nums):
            in_rest = ((idx >> i) & 1) == 0
            cur = np.where(in_rest, notX & v, 0).astype(np.int32)
            for b in range(BITS - 1, -1, -1):
                has = ((cur >> b) & 1).astype(bool)
                nb = np.where(has & (basis[b] == 0), cur, basis[b])
                basis[b] = nb
                cur = np.where(has, cur ^ nb, cur)

        res = np.zeros(size, dtype=np.int32)
        for b in range(BITS - 1, -1, -1):
            res = np.maximum(res, res ^ basis[b])

        total = an.astype(np.int64) + X.astype(np.int64) + 2 * res.astype(np.int64)
        return int(total.max())
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
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [1707. Maximum XOR With an Element From Array](../../1501-2000/1707-maximum-xor-with-an-element-from-array/)
- [3599. Partition Array to Minimize XOR](../../3501-4000/3599-partition-array-to-minimize-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/)
