# LeetCode 2453: Destroy Sequential Targets

**LeetCode Problem #2453 — Destroy Sequential Targets**
Solve LeetCode Destroy Sequential Targets using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Destroy Sequential Targets |
| LeetCode | #2453 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array `nums` consisting of positive integers, representing targets on a number line. You are also given an integer `space`.

You have a machine which can destroy targets. **Seeding** the machine with some `nums[i]` allows it to destroy all targets with values that can be represented as `nums[i] + c * space`, where `c` is any non-negative integer. You want to destroy the **maximum** number of targets in `nums`.

Return* the **minimum value** of *`nums[i]`* you can seed the machine with to destroy the maximum number of targets.*

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= space <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [3,7,8,1,1,5], space = 2`
- **Output:** `1`
- **Explanation:** If we seed the machine with nums[3], then we destroy all targets equal to 1,3,5,7,9,... 
In this case, we would destroy 5 total targets (all except for nums[2]). 
It is impossible to destroy more than 5 targets, so we return nums[3].

### Example 2
- **Input:** `nums = [1,3,5,2,4,6], space = 2`
- **Output:** `1`
- **Explanation:** Seeding the machine with nums[0], or nums[3] destroys 3 targets. 
It is not possible to destroy more than 3 targets.
Since nums[0] is the minimal integer that can destroy 3 targets, we return 1.

### Example 3
- **Input:** `nums = [6,2,5], space = 100`
- **Output:** `2`
- **Explanation:** Whatever initial seed we select, we can only destroy 1 target. The minimal seed is nums[1].

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Destroy Sequential Targets**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,7,8,1,1,5], space = 2`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** If we seed the machine with nums[3], then we destroy all targets equal to 1,3,5,7,9,... 
In this case, we would destroy 5 total targets (all except for nums[2]). 
It is impossible to destroy more than 5 targets, so we return nums[3].

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
from collections import Counter

class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        rem_counts = Counter(num % space for num in nums)
        max_targets = max(rem_counts.values())
        
        return min(num for num in nums if rem_counts[num % space] == max_targets)
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
- [1291. Sequential Digits](../../1001-1500/1212-sequential-digits/)
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../../3001-3500/3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)
- [13. Roman to Integer](../../0001-0500/0013-roman-to-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/destroy-sequential-targets/)
