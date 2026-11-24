# LeetCode 446: Arithmetic Slices II - Subsequence

**LeetCode Problem #446 — Arithmetic Slices II - Subsequence**
Solve LeetCode Arithmetic Slices II - Subsequence using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Arithmetic Slices II - Subsequence |
| LeetCode | #446 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `nums`, return *the number of all the **arithmetic subsequences** of* `nums`.

A sequence of numbers is called arithmetic if it consists of **at least three elements** and if the difference between any two consecutive elements is the same.

For example, `[1, 3, 5, 7, 9]`, `[7, 7, 7, 7]`, and `[3, -1, -5, -9]` are arithmetic sequences. 
 For example, `[1, 1, 2, 5, 7]` is not an arithmetic sequence.

A **subsequence** of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, `[2,5,10]` is a subsequence of `[1,2,1,** 2 **,4,1, **5** , **10** ]`.

The test cases are generated so that the answer fits in **32-bit** integer.

## Constraints
- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `nums = [2,4,6,8,10]`
- **Output:** `7`
- **Explanation:** All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

### Example 2
- **Input:** `nums = [7,7,7,7,7]`
- **Output:** `16`
- **Explanation:** Any subsequence of this array is arithmetic.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Arithmetic Slices II - Subsequence**, we observe the problem requirements and utilize the **Dynamic Programming** technique. By maintaining a **DP Table / Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **DP Table / Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,4,6,8,10]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

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
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for j in range(n):
            for i in range(j):
                d = nums[j] - nums[i]
                c = dp[i].get(d, 0)
                ans += c
                dp[j][d] += c + 1
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
- [413. Arithmetic Slices](../../0001-0500/0413-arithmetic-slices/)
- [1307. Verbal Arithmetic Puzzle](../../1001-1500/1307-verbal-arithmetic-puzzle/)
- [1502. Can Make Arithmetic Progression From Sequence](../../1501-2000/1502-can-make-arithmetic-progression-from-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/)
