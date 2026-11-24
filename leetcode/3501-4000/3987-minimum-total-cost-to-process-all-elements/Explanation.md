# LeetCode 3987: Minimum Total Cost to Process All Elements

**LeetCode Problem #3987 — Minimum Total Cost to Process All Elements**
Solve LeetCode Minimum Total Cost to Process All Elements using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Total Cost to Process All Elements |
| LeetCode | #3987 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

Initially, you have `k` units of resources.

You must process the elements of `nums` from left to right. To process the `i^th` element, you need `nums[i]` resources.

If your available resources are less than `nums[i]`, you may perform an operation that increases your available resources by `k`. The value of `k` is fixed and does not change throughout the process. The first such operation incurs a cost of 1, the second incurs a cost of 2, and so on.

After processing the `i^th` element, your available resources decrease by `nums[i]`.

Return an integer denoting the **minimum total cost** required to process all elements. Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4], k = 4`
- **Output:** `3`
- **Explanation:** After processing `nums[0]`, we have `4 - 1 = 3` units of resources left. 
 After processing `nums[1]`, we have `3 - 2 = 1` unit of resources left. 
 Since `nums[2] = 3` and only 1 unit of resources is available, we perform the first operation costing 1. After processing `nums[2]`, we have `1 + 4 - 3 = 2` units of resources left. 
 Since `nums[3] = 4` and only 2 units of resources are available, we perform the second operation costing 2, to have `2 + 4 = 6` units of resources, which is enough to process `nums[3]`. 
 Thus, the total cost is `1 + 2 = 3`.

### Example 2
- **Input:** `nums = [1,1,7,14], k = 4`
- **Output:** `15`
- **Explanation:** After processing `nums[0]`, we have `4 - 1 = 3` units of resources left. 
 After processing `nums[1]`, we have `3 - 1 = 2` units of resources left. 
 Since `nums[2] = 7` and only 2 units of resources are available, we perform two operations costing `1 + 2 = 3`. After processing `nums[2]`, we have `2 + 4 + 4 - 7 = 3` units of resources left. 
 Since `nums[3] = 14` and only 3 units of resources are available, we perform three operations costing `3 + 4 + 5 = 12`, to have `3 + 4 + 4 + 4 = 15` units of resources, which is enough to process `nums[3]`. 
 Thus, the total cost is `3 + 12 = 15`.

### Example 3
- **Input:** `nums = [1,2,3,4], k = 10`
- **Output:** `0`
- **Explanation:** To process all elements, we can use the initial 10 units of resources without performing any operations. Thus, the total cost required is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Total Cost to Process All Elements**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4], k = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** After processing `nums[0]`, we have `4 - 1 = 3` units of resources left. 
 After processing `nums[1]`, we have `3 - 2 = 1` unit of resources left. 
 Since `nums[2] = 3` and only 1 unit of resources is available, we perform the first operation costing 1. After processing `nums[2]`, we have `1 + 4 - 3 = 2` units of resources left. 
 Since `nums[3] = 4` and only 2 units of resources are available, we perform the second operation costing 2, to have `2 + 4 = 6` units of resources, which is enough to process `nums[3]`. 
 Thus, the total cost is `1 + 2 = 3`.

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
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        total = sum(nums)
        T = max(0, (total - k + k - 1) // k)   # ceil((total - k) / k)
        return (T * (T + 1) // 2) % MOD
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
- [2499. Minimum Total Cost to Make Arrays Unequal](../../2001-2500/2499-minimum-total-cost-to-make-arrays-unequal/)
- [3784. Minimum Deletion Cost to Make All Characters Equal](../../3501-4000/3784-minimum-deletion-cost-to-make-all-characters-equal/)
- [2602. Minimum Operations to Make All Array Elements Equal](../../2501-3000/2602-minimum-operations-to-make-all-array-elements-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/)
