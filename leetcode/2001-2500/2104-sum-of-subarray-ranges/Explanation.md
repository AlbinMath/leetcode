# LeetCode 2104: Sum of Subarray Ranges

**LeetCode Problem #2104 — Sum of Subarray Ranges**
Solve LeetCode Sum of Subarray Ranges using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Subarray Ranges |
| LeetCode | #2104 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`. The **range** of a subarray of `nums` is the difference between the largest and smallest element in the subarray.

Return *the **sum of all** subarray ranges of *`nums`*.*

A subarray is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 1000`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `4`
- **Explanation:** The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

### Example 2
- **Input:** `nums = [1,3,3]`
- **Output:** `4`
- **Explanation:** The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.

### Example 3
- **Input:** `nums = [4,-2,-3,4,1]`
- **Output:** `59`
- **Explanation:** The sum of all subarray ranges of nums is 59.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of Subarray Ranges**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def sum_mins(arr: List[int]) -> int:
            n = len(arr)
            stack = []
            total = 0
            for j in range(n + 1):
                while stack and (j == n or arr[stack[-1]] >= arr[j]):
                    i = stack.pop()
                    prev = stack[-1] if stack else -1
                    total += arr[i] * (i - prev) * (j - i)
                stack.append(j)
            return total

        return -sum_mins([-x for x in nums]) - sum_mins(nums)
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [209. Minimum Size Subarray Sum](../../0001-0500/0209-minimum-size-subarray-sum/)
- [560. Subarray Sum Equals K](../../0501-1000/0560-subarray-sum-equals-k/)
- [862. Shortest Subarray with Sum at Least K](../../0501-1000/0862-shortest-subarray-with-sum-at-least-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-subarray-ranges/)
