# LeetCode 982: Triples with Bitwise AND Equal To Zero

**LeetCode Problem #982 — Triples with Bitwise AND Equal To Zero**
Solve LeetCode Triples with Bitwise AND Equal To Zero using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Triples with Bitwise AND Equal To Zero |
| LeetCode | #982 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array nums, return *the number of **AND triples***.

An **AND triple** is a triple of indices `(i, j, k)` such that:

`0 <= i < nums.length` 
 `0 <= j < nums.length` 
 `0 <= k < nums.length` 
 `nums[i] & nums[j] & nums[k] == 0`, where `&` represents the bitwise-AND operator.

## Constraints
- `1 <= nums.length <= 1000`
- `0 <= nums[i] < 2^16`

## Examples
### Example 1
- **Input:** `nums = [2,1,3]`
- **Output:** `12`
- **Explanation:** We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2

### Example 2
- **Input:** `nums = [0,0,0]`
- **Output:** `27`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Triples with Bitwise AND Equal To Zero**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,1,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2

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
    def countTriplets(self, nums: List[int]) -> int:
        freq = Counter(nums)
        items = list(freq.items())

        # cnt[v] = number of ordered pairs (i, j) with nums[i] & nums[j] == v
        cnt = Counter()
        for a, fa in items:
            for b, fb in items:
                cnt[a & b] += fa * fb

        ans = 0
        for v, c in cnt.items():
            for x, fx in items:
                if v & x == 0:
                    ans += c * fx
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
- [2275. Largest Combination With Bitwise AND Greater Than Zero](../../2001-2500/2275-largest-combination-with-bitwise-and-greater-than-zero/)
- [2546. Apply Bitwise Operations to Make Strings Equal](../../2501-3000/2546-apply-bitwise-operations-to-make-strings-equal/)
- [3702. Longest Subsequence With Non-Zero Bitwise XOR](../../3501-4000/3702-longest-subsequence-with-non-zero-bitwise-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/)
