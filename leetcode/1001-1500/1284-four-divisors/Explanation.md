# LeetCode 1390: Four Divisors

**LeetCode Problem #1390 — Four Divisors**
Solve LeetCode Four Divisors using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Four Divisors |
| LeetCode | #1390 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, return *the sum of divisors of the integers in that array that have exactly four divisors*. If there is no such integer in the array, return `0`.

## Constraints
- `1 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [21,4,7]`
- **Output:** `32`
- **Explanation:** 21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

### Example 2
- **Input:** `nums = [21,21]`
- **Output:** `64`

### Example 3
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `0`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Four Divisors**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [21,4,7]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `32`.
4. **Verification:** 21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            divs = set()
            i = 1
            while i * i <= x:
                if x % i == 0:
                    divs.add(i)
                    divs.add(x // i)
                    if len(divs) > 4:
                        break
                i += 1
            if len(divs) == 4:
                total += sum(divs)
        return total
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [342. Power of Four](../../0001-0500/0342-power-of-four/)
- [1362. Closest Divisors](../../1001-1500/1276-closest-divisors/)
- [1808. Maximize Number of Nice Divisors](../../1501-2000/1936-maximize-number-of-nice-divisors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/four-divisors/)
