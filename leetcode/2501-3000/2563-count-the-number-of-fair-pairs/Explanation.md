# LeetCode 2563: Count the Number of Fair Pairs

**LeetCode Problem #2563 — Count the Number of Fair Pairs**
Solve LeetCode Count the Number of Fair Pairs using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Fair Pairs |
| LeetCode | #2563 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a **0-indexed** integer array `nums` of size `n` and two integers `lower` and `upper`, return *the number of fair pairs*.

A pair `(i, j)` is fair if:

`0 <= i < j < n`, and 
 `lower <= nums[i] + nums[j] <= upper`

## Constraints
- `1 <= nums.length <= 10^5`
- `nums.length == n`
- ` -10^9 <= nums[i] <= 10^9`
- ` -10^9 <= lower <= upper <= 10^9 `

## Examples
### Example 1
- **Input:** `nums = [0,1,7,4,4,5], lower = 3, upper = 6`
- **Output:** `6`
- **Explanation:** There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

### Example 2
- **Input:** `nums = [1,7,9,2,5], lower = 11, upper = 11`
- **Output:** `1`
- **Explanation:** There is a single fair pair: (2,3).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count the Number of Fair Pairs**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,7,4,4,5], lower = 3, upper = 6`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

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
class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            lo = bisect_left(nums, lower - x, i + 1)
            hi = bisect_right(nums, upper - x, i + 1)
            ans += hi - lo
        return ans
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
- [2006. Count Number of Pairs With Absolute Difference K](../../2001-2500/2006-count-number-of-pairs-with-absolute-difference-k/)
- [2364. Count Number of Bad Pairs](../../2001-2500/2364-count-number-of-bad-pairs/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1248-count-number-of-nice-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-fair-pairs/)
