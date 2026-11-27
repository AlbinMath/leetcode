# LeetCode 2656: Maximum Sum With Exactly K Elements 

**LeetCode Problem #2656 — Maximum Sum With Exactly K Elements **
Solve LeetCode Maximum Sum With Exactly K Elements  using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Sum With Exactly K Elements  |
| LeetCode | #2656 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `nums` and an integer `k`. Your task is to perform the following operation **exactly** `k` times in order to maximize your score:

Select an element `m` from `nums`. 
 Remove the selected element `m` from the array. 
 Add a new element with a value of `m + 1` to the array. 
 Increase your score by `m`.

Return *the maximum score you can achieve after performing the operation exactly* `k` *times.*

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= k <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5], k = 3`
- **Output:** `18`
- **Explanation:** We need to choose exactly 3 elements from nums to maximize the sum.
For the first iteration, we choose 5. Then sum is 5 and nums = [1,2,3,4,6]
For the second iteration, we choose 6. Then sum is 5 + 6 and nums = [1,2,3,4,7]
For the third iteration, we choose 7. Then sum is 5 + 6 + 7 = 18 and nums = [1,2,3,4,8]
So, we will return 18.
It can be proven, that 18 is the maximum answer that we can achieve.

### Example 2
- **Input:** `nums = [5,5,5], k = 2`
- **Output:** `11`
- **Explanation:** We need to choose exactly 2 elements from nums to maximize the sum.
For the first iteration, we choose 5. Then sum is 5 and nums = [5,5,6]
For the second iteration, we choose 6. Then sum is 5 + 6 = 11 and nums = [5,5,7]
So, we will return 11.
It can be proven, that 11 is the maximum answer that we can achieve.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Sum With Exactly K Elements **, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5], k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `18`.
4. **Verification:** We need to choose exactly 3 elements from nums to maximize the sum.
For the first iteration, we choose 5. Then sum is 5 and nums = [1,2,3,4,6]
For the second iteration, we choose 6. Then sum is 5 + 6 and nums = [1,2,3,4,7]
For the third iteration, we choose 7. Then sum is 5 + 6 + 7 = 18 and nums = [1,2,3,4,8]
So, we will return 18.
It can be proven, that 18 is the maximum answer that we can achieve.

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
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        return k * m + k * (k - 1) // 2
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
- [3462. Maximum Sum With at Most K Elements](../../3001-3500/3462-maximum-sum-with-at-most-k-elements/)
- [3974. Maximum Total Sum of K Selected Elements](../../3501-4000/3974-maximum-total-sum-of-k-selected-elements/)
- [1191. K-Concatenation Maximum Sum](../../1001-1500/1191-k-concatenation-maximum-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/)
