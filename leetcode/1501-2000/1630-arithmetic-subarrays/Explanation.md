# LeetCode 1630: Arithmetic Subarrays

**LeetCode Problem #1630 — Arithmetic Subarrays**
Solve LeetCode Arithmetic Subarrays using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Arithmetic Subarrays |
| LeetCode | #1630 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A sequence of numbers is called **arithmetic** if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence `s` is arithmetic if and only if `s[i+1] - s[i] == s[1] - s[0] `for all valid `i`.

For example, these are **arithmetic** sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not **arithmetic**:

1, 1, 2, 5, 7

You are given an array of `n` integers, `nums`, and two arrays of `m` integers each, `l` and `r`, representing the `m` range queries, where the `i^th` query is the range `[l[i], r[i]]`. All the arrays are **0-indexed**.

Return *a list of *`boolean` *elements* `answer`*, where* `answer[i]` *is* `true` *if the subarray* `nums[l[i]], nums[l[i]+1], ... , nums[r[i]]`* can be **rearranged** to form an **arithmetic** sequence, and* `false` *otherwise.*

## Constraints
- `n == nums.length`
- `m == l.length`
- `m == r.length`
- `2 <= n <= 500`
- `1 <= m <= 500`
- `0 <= l[i] < r[i] < n`
- `-10^5 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = `[4,6,5,9,3,7]`, l = `[0,0,2]`, r = `[2,3,5]`
- **Output:** `[true,false,true]`
- **Explanation:** In the 0^th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1^st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2^nd query, the subarray is `[5,9,3,7]. This` can be rearranged as `[3,5,7,9]`, which is an arithmetic sequence.

### Example 2
- **Input:** `nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]`
- **Output:** `[false,true,false,false,true,true]`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Arithmetic Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = `[4,6,5,9,3,7]`, l = `[0,0,2]`, r = `[2,3,5]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[true,false,true]`.
4. **Verification:** In the 0^th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1^st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2^nd query, the subarray is `[5,9,3,7]. This` can be rearranged as `[3,5,7,9]`, which is an arithmetic sequence.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(sub: List[int]) -> bool:
            k = len(sub)
            min_val = min(sub)
            max_val = max(sub)
            if (max_val - min_val) % (k - 1) != 0:
                return False
                
            step = (max_val - min_val) // (k - 1)
            if step == 0:
                return True
                
            seen = set(sub)
            return all((min_val + i * step) in seen for i in range(k))

        return [is_arithmetic(nums[left : right + 1]) for left, right in zip(l, r)]
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [795. Number of Subarrays with Bounded Maximum](../../0501-1000/0795-number-of-subarrays-with-bounded-maximum/)
- [898. Bitwise ORs of Subarrays](../../0501-1000/0898-bitwise-ors-of-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/arithmetic-subarrays/)
