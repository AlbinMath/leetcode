# LeetCode 414: Third Maximum Number

**LeetCode Problem #414 — Third Maximum Number**
Solve LeetCode Third Maximum Number using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Third Maximum Number |
| LeetCode | #414 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Return the **third distinct maximum** number in this array. If the third **maximum** does not exist, return the **maximum** number.

## Constraints
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `nums = [3,2,1]`
- **Output:** `1`
- **Explanation:** The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

### Example 2
- **Input:** `nums = [1,2]`
- **Output:** `2`
- **Explanation:** The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

### Example 3
- **Input:** `nums = [2,2,3,1]`
- **Output:** `1`
- **Explanation:** The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Third Maximum Number**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

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
    def thirdMax(self, nums):
        first = None
        second = None
        third = None

        for num in nums:
            # Ignore duplicates
            if num == first or num == second or num == third:
                continue

            if first is None or num > first:
                third = second
                second = first
                first = num

            elif second is None or num > second:
                third = second
                second = num

            elif third is None or num > third:
                third = num

        # If there is no third maximum, return maximum
        if third is None:
            return first

        return third
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
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)
- [1072. Flip Columns For Maximum Number of Equal Rows](../../1001-1500/1072-flip-columns-for-maximum-number-of-equal-rows/)
- [1189. Maximum Number of Balloons](../../1001-1500/1189-maximum-number-of-balloons/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/third-maximum-number/)
