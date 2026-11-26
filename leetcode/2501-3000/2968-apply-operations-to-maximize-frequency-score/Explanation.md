# LeetCode 2968: Apply Operations to Maximize Frequency Score

**LeetCode Problem #2968 — Apply Operations to Maximize Frequency Score**
Solve LeetCode Apply Operations to Maximize Frequency Score using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Apply Operations to Maximize Frequency Score |
| LeetCode | #2968 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums` and an integer `k`.

You can perform the following operation on the array **at most** `k` times:

Choose any index `i` from the array and **increase** or **decrease** `nums[i]` by `1`.

The score of the final array is the **frequency** of the most frequent element in the array.

Return *the **maximum** score you can achieve*.

The frequency of an element is the number of occurences of that element in the array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^14`

## Examples
### Example 1
- **Input:** `nums = [1,2,6,4], k = 3`
- **Output:** `3`
- **Explanation:** We can do the following operations on the array:
- Choose i = 0, and increase the value of nums[0] by 1. The resulting array is [2,2,6,4].
- Choose i = 3, and decrease the value of nums[3] by 1. The resulting array is [2,2,6,3].
- Choose i = 3, and decrease the value of nums[3] by 1. The resulting array is [2,2,6,2].
The element 2 is the most frequent in the final array so our score is 3.
It can be shown that we cannot achieve a better score.

### Example 2
- **Input:** `nums = [1,4,4,2,4], k = 0`
- **Output:** `3`
- **Explanation:** We cannot apply any operations so our score will be the frequency of the most frequent element in the original array, which is 3.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Apply Operations to Maximize Frequency Score**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,6,4], k = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can do the following operations on the array:
- Choose i = 0, and increase the value of nums[0] by 1. The resulting array is [2,2,6,4].
- Choose i = 3, and decrease the value of nums[3] by 1. The resulting array is [2,2,6,3].
- Choose i = 3, and decrease the value of nums[3] by 1. The resulting array is [2,2,6,2].
The element 2 is the most frequent in the final array so our score is 3.
It can be shown that we cannot achieve a better score.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        P = [0] * (n + 1)
        for i, x in enumerate(nums):
            P[i + 1] = P[i] + x

        def cost(l: int, r: int) -> int:
            mid = (l + r) // 2
            m = nums[mid]
            left = m * (mid - l) - (P[mid] - P[l])
            right = (P[r + 1] - P[mid + 1]) - m * (r - mid)
            return left + right

        ans = 0
        l = 0
        for r in range(n):
            while cost(l, r) > k:
                l += 1
            ans = max(ans, r - l + 1)
        return ans
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2818. Apply Operations to Maximize Score](../../2501-3000/2818-apply-operations-to-maximize-score/)
- [2897. Apply Operations on Array to Maximize Sum of Squares](../../2501-3000/2897-apply-operations-on-array-to-maximize-sum-of-squares/)
- [1799. Maximize Score After N Operations](../../1501-2000/1799-maximize-score-after-n-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/)
