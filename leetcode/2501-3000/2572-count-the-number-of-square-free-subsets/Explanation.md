# LeetCode 2572: Count the Number of Square-Free Subsets

**LeetCode Problem #2572 — Count the Number of Square-Free Subsets**
Solve LeetCode Count the Number of Square-Free Subsets using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Square-Free Subsets |
| LeetCode | #2572 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a positive integer **0-indexed** array `nums`.

A subset of the array `nums` is **square-free** if the product of its elements is a **square-free integer**.

A **square-free integer** is an integer that is divisible by no square number other than `1`.

Return *the number of square-free non-empty subsets of the array* **nums**. Since the answer may be too large, return it **modulo** `10^9 + 7`.

A **non-empty** **subset** of `nums` is an array that can be obtained by deleting some (possibly none but not all) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 30`

## Examples
### Example 1
- **Input:** `nums = [3,4,4,5]`
- **Output:** `3`
- **Explanation:** There are 3 square-free subsets in this example:
- The subset consisting of the 0^th element [3]. The product of its elements is 3, which is a square-free integer.
- The subset consisting of the 3^rd element [5]. The product of its elements is 5, which is a square-free integer.
- The subset consisting of 0^th and 3^rd elements [3,5]. The product of its elements is 15, which is a square-free integer.
It can be proven that there are no more than 3 square-free subsets in the given array.

### Example 2
- **Input:** `nums = [1]`
- **Output:** `1`
- **Explanation:** There is 1 square-free subset in this example:
- The subset consisting of the 0^th element [1]. The product of its elements is 1, which is a square-free integer.
It can be proven that there is no more than 1 square-free subset in the given array.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count the Number of Square-Free Subsets**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,4,4,5]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** There are 3 square-free subsets in this example:
- The subset consisting of the 0^th element [3]. The product of its elements is 3, which is a square-free integer.
- The subset consisting of the 3^rd element [5]. The product of its elements is 5, which is a square-free integer.
- The subset consisting of 0^th and 3^rd elements [3,5]. The product of its elements is 15, which is a square-free integer.
It can be proven that there are no more than 3 square-free subsets in the given array.

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
from collections import Counter

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        def get_mask(v: int) -> int:
            m = 0
            for i, p in enumerate(primes):
                if v % p == 0:
                    v //= p
                    if v % p == 0:
                        return -1  # p squared divides it
                    m |= 1 << i
            return m

        cnt = Counter(nums)
        dp = [0] * 1024
        dp[0] = 1

        for v in range(2, 31):
            c = cnt.get(v, 0)
            if c == 0:
                continue
            m = get_mask(v)
            if m < 0:
                continue
            for mask in range(1023, -1, -1):
                if mask & m == 0 and dp[mask]:
                    dp[mask | m] = (dp[mask | m] + dp[mask] * c) % MOD

        total = sum(dp) % MOD
        total = total * pow(2, cnt.get(1, 0), MOD) % MOD
        return (total - 1) % MOD
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
- [2044. Count Number of Maximum Bitwise-OR Subsets](../../2001-2500/2044-count-number-of-maximum-bitwise-or-subsets/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1248-count-number-of-nice-subarrays/)
- [1395. Count Number of Teams](../../1001-1500/1395-count-number-of-teams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-square-free-subsets/)
