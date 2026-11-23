# LeetCode 1480: Running Sum of 1d Array

**LeetCode Problem #1480 — Running Sum of 1d Array**
Solve LeetCode Running Sum of 1d Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Running Sum of 1d Array |
| LeetCode | #1480 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]&hellip;nums[i])`.

Return the running sum of `nums`.

## Constraints
- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4]`
- **Output:** `[1,3,6,10]`
- **Explanation:** Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

### Example 2
- **Input:** `nums = [1,1,1,1,1]`
- **Output:** `[1,2,3,4,5]`
- **Explanation:** Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

### Example 3
- **Input:** `nums = [3,1,2,10,1]`
- **Output:** `[3,4,6,16,17]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Running Sum of 1d Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,6,10]`.
4. **Verification:** Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

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
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0

        for num in nums:
            total += num
            result.append(total)

        return result
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
- [167. Two Sum II - Input Array Is Sorted](../../0001-0500/0167-two-sum-ii---input-array-is-sorted/)
- [410. Split Array Largest Sum](../../0001-0500/0410-split-array-largest-sum/)
- [1005. Maximize Sum Of Array After K Negations](../../1001-1500/1047-maximize-sum-of-array-after-k-negations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/)
