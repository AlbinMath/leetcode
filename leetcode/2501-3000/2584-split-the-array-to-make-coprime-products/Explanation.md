# LeetCode 2584: Split the Array to Make Coprime Products

**LeetCode Problem #2584 — Split the Array to Make Coprime Products**
Solve LeetCode Split the Array to Make Coprime Products using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split the Array to Make Coprime Products |
| LeetCode | #2584 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums` of length `n`.

A **split** at an index `i` where `0 <= i <= n - 2` is called **valid** if the product of the first `i + 1` elements and the product of the remaining elements are coprime.

For example, if `nums = [2, 3, 3]`, then a split at the index `i = 0` is valid because `2` and `9` are coprime, while a split at the index `i = 1` is not valid because `6` and `3` are not coprime. A split at the index `i = 2` is not valid because `i == n - 1`.

Return *the smallest index *`i`* at which the array can be split validly or *`-1`* if there is no such split*.

Two values `val1` and `val2` are coprime if `gcd(val1, val2) == 1` where `gcd(val1, val2)` is the greatest common divisor of `val1` and `val2`.

## Constraints
- `n == nums.length`
- `1 <= n <= 10^4`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [4,7,8,15,3,5]`
- **Output:** `2`
- **Explanation:** The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
The only valid split is at index 2.

### Example 2
- **Input:** `nums = [4,7,15,8,3,5]`
- **Output:** `-1`
- **Explanation:** The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
There is no valid split.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Split the Array to Make Coprime Products**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,7,8,15,3,5]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
The only valid split is at index 2.

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
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)
        M = max(nums)

        # smallest prime factor sieve
        spf = list(range(M + 1))
        i = 2
        while i * i <= M:
            if spf[i] == i:
                for j in range(i * i, M + 1, i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1

        first, last = {}, {}
        for idx, v in enumerate(nums):
            while v > 1:
                p = spf[v]
                while v % p == 0:
                    v //= p
                if p not in first:
                    first[p] = idx
                last[p] = idx

        diff = [0] * (n + 1)
        for p, f in first.items():
            l = last[p]
            if l > f:
                diff[f] += 1          # splits f .. l-1 are blocked
                diff[l] -= 1

        cover = 0
        for i in range(n - 1):
            cover += diff[i]
            if cover == 0:
                return i
        return -1
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
- [3145. Find Products of Elements of Big Array](../../3001-3500/3145-find-products-of-elements-of-big-array/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)
- [805. Split Array With Same Average](../../0501-1000/0805-split-array-with-same-average/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-the-array-to-make-coprime-products/)
