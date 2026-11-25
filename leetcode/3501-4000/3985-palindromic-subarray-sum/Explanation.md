# LeetCode 3985: Palindromic Subarray Sum

**LeetCode Problem #3985 — Palindromic Subarray Sum**
Solve LeetCode Palindromic Subarray Sum using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Palindromic Subarray Sum |
| LeetCode | #3985 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Return the maximum possible sum of a subarray of `nums` that is a palindrome .

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^​​​​​​​9`

## Examples
### Example 1
- **Input:** `nums = [10,10]`
- **Output:** `20`
- **Explanation:** The whole array `[10,10]` is a palindrome. Therefore, the maximum sum is `10 + 10 = 20`.

### Example 2
- **Input:** `nums = [1,2,3,2,1,5,6]`
- **Output:** `9`
- **Explanation:** The contiguous subarray `[1,2,3,2,1]` is a palindrome. Its sum is `1 + 2 + 3 + 2 + 1 = 9` and it is the maximum sum.

### Example 3
- **Input:** `nums = [7,1,2,1,7,3,4,3,4]`
- **Output:** `18`
- **Explanation:** The contiguous subarray `[7,1,2,1,7]` is a palindrome. Its sum is `7 + 1 + 2 + 1 + 7 = 18` and it is the maximum sum.

### Example 4
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `5`
- **Explanation:** No subarray with length greater than 1 is a palindrome. The largest element in the array is 5. Therefore, the answer is 5.

### Example 5
- **Input:** `nums = [1000]`
- **Output:** `1000`
- **Explanation:** The subarray with only one element is a palindrome. Therefore, the answer is 1000.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Palindromic Subarray Sum**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [10,10]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `20`.
4. **Verification:** The whole array `[10,10]` is a palindrome. Therefore, the maximum sum is `10 + 10 = 20`.

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
    def getSum(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, v in enumerate(nums):
            pre[i + 1] = pre[i] + v

        # odd palindromes: d1[i] = number of palindromes centered at i
        d1 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and nums[i - k] == nums[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        # even palindromes: d2[i] = number centered between i-1 and i
        d2 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < n and nums[i - k - 1] == nums[i + k]:
                k += 1
            d2[i] = k
            if i + k - 1 > r:
                l, r = i - k, i + k - 1

        best = 0
        for i in range(n):
            k = d1[i]
            best = max(best, pre[i + k] - pre[i - k + 1])
            k = d2[i]
            if k:
                best = max(best, pre[i + k] - pre[i - k])
        return best
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
- [209. Minimum Size Subarray Sum](../../0001-0500/0209-minimum-size-subarray-sum/)
- [523. Continuous Subarray Sum](../../0501-1000/0523-continuous-subarray-sum/)
- [560. Subarray Sum Equals K](../../0501-1000/0560-subarray-sum-equals-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/palindromic-subarray-sum/)
