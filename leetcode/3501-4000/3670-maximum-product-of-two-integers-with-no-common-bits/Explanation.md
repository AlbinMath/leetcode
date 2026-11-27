# LeetCode 3670: Maximum Product of Two Integers With No Common Bits

**LeetCode Problem #3670 — Maximum Product of Two Integers With No Common Bits**
Solve LeetCode Maximum Product of Two Integers With No Common Bits using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Product of Two Integers With No Common Bits |
| LeetCode | #3670 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Your task is to find two **distinct** indices `i` and `j` such that the product `nums[i] * nums[j]` is **maximized,** and the binary representations of `nums[i]` and `nums[j]` do not share any common set bits.

Return the **maximum** possible product of such a pair. If no such pair exists, return 0.

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5,6,7]`
- **Output:** `12`
- **Explanation:** The best pair is 3 (011) and 4 (100). They share no set bits and `3 * 4 = 12`.

### Example 2
- **Input:** `nums = [5,6,4]`
- **Output:** `0`
- **Explanation:** Every pair of numbers has at least one common set bit. Hence, the answer is 0.

### Example 3
- **Input:** `nums = [64,8,32]`
- **Output:** `2048`
- **Explanation:** No pair of numbers share a common bit, so the answer is the product of the two maximum elements, 64 and 32 (`64 * 32 = 2048`).

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Product of Two Integers With No Common Bits**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5,6,7]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** The best pair is 3 (011) and 4 (100). They share no set bits and `3 * 4 = 12`.

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
    def maxProduct(self, nums):
        bits = max(nums).bit_length()
        size = 1 << bits
        full = size - 1

        arr = np.array(nums, dtype=np.int64)
        best = np.zeros(size, dtype=np.int64)
        best[arr] = arr  # best[m] = largest element that is a submask of m

        for b in range(bits):
            v = best.reshape(-1, 2, 1 << b)
            np.maximum(v[:, 1, :], v[:, 0, :], out=v[:, 1, :])

        partner = best[full ^ arr]   # largest element fitting inside the complement
        return int((arr * partner).max())
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
- [1464. Maximum Product of Two Elements in an Array](../../1001-1500/1464-maximum-product-of-two-elements-in-an-array/)
- [1913. Maximum Product Difference Between Two Pairs](../../1501-2000/1913-maximum-product-difference-between-two-pairs/)
- [1960. Maximum Product of the Length of Two Palindromic Substrings](../../1501-2000/1960-maximum-product-of-the-length-of-two-palindromic-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/)
