# LeetCode 2598: Smallest Missing Non-negative Integer After Operations

**LeetCode Problem #2598 — Smallest Missing Non-negative Integer After Operations**
Solve LeetCode Smallest Missing Non-negative Integer After Operations using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Missing Non-negative Integer After Operations |
| LeetCode | #2598 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums` and an integer `value`.

In one operation, you can add or subtract `value` from any element of `nums`.

For example, if `nums = [1,2,3]` and `value = 2`, you can choose to subtract `value` from `nums[0]` to make `nums = [-1,2,3]`.

The MEX (minimum excluded) of an array is the smallest missing **non-negative** integer in it.

For example, the MEX of `[-1,2,3]` is `0` while the MEX of `[1,0,3]` is `2`.

Return *the maximum MEX of *`nums`* after applying the mentioned operation **any number of times***.

## Constraints
- `1 <= nums.length, value <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,-10,7,13,6,8], value = 5`
- **Output:** `4`
- **Explanation:** One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,

### Example 2
- **Input:** `nums = [1,-10,7,13,6,8], value = 7`
- **Output:** `2`
- **Explanation:** One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Missing Non-negative Integer After Operations**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,-10,7,13,6,8], value = 5`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = [0] * value
        for x in nums:
            cnt[x % value] += 1
        m = 0
        while True:
            r = m % value
            if cnt[r] == 0:
                return m
            cnt[r] -= 1
            m += 1
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../../2501-3000/2996-smallest-missing-integer-greater-than-sequential-prefix-sum/)
- [3782. Last Remaining Integer After Alternating Deletion Operations](../../3501-4000/3782-last-remaining-integer-after-alternating-deletion-operations/)
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/)
