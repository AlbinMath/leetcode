# LeetCode 4063: Longest Subarray Divisible by K with At Most One Negation I

**LeetCode Problem #4063 — Longest Subarray Divisible by K with At Most One Negation I**
Solve LeetCode Longest Subarray Divisible by K with At Most One Negation I using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Subarray Divisible by K with At Most One Negation I |
| LeetCode | #4063 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

A subarray is **valid** if its sum is divisible by `k`, or can become divisible by `k` by **negating one element within that subarray**.

Negating an element means replacing its value `x` with `-x`.

Return the **length of the longest valid subarray**. If no valid subarray exists, return 0.

## Constraints
- `1 <= nums.length <= 1000`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [4,1,2], k = 3`
- **Output:** `3`
- **Explanation:** The sum of the entire array is 7, and `7 % 3 = 1`, so it is not divisible by `k = 3`. 
 Negating `nums[2] = 2` changes the sum to `4 + 1 &minus; 2 = 3`, which is divisible by `k`. 
 Therefore, the entire array is a valid subarray, giving a length of 3.

### Example 2
- **Input:** `nums = [5,3,4], k = 7`
- **Output:** `2`
- **Explanation:** The sum of the entire array is 12, and negating any one of its elements does not make its sum divisible by 7. 
 However, the subarray `[3, 4]` has a sum of 7, which is divisible by `k = 7` without any negation. 
 Therefore, the longest valid subarray has a length of 2.

### Example 3
- **Input:** `nums = [2,2,5], k = 6`
- **Output:** `2`
- **Explanation:** The sum of the entire array is 9, and negating any one of its elements does not make its sum divisible by 6. 
 The subarray `[2, 2]` has a sum of 4. Negating either element changes it to `[-2, 2]` or `[2, -2]`, both of which have a sum of 0. 
 Therefore, the longest valid subarray has a length of 2.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Longest Subarray Divisible by K with At Most One Negation I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,1,2], k = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The sum of the entire array is 7, and `7 % 3 = 1`, so it is not divisible by `k = 3`. 
 Negating `nums[2] = 2` changes the sum to `4 + 1 &minus; 2 = 3`, which is divisible by `k`. 
 Therefore, the entire array is a valid subarray, giving a length of 3.

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
    def longestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        best = 0
        for l in range(n):
            S = 0
            seen = set()
            for r in range(l, n):
                x = nums[r]
                S += x
                seen.add((2 * x) % k)
                rem = S % k
                if rem == 0 or rem in seen:
                    best = max(best, r - l + 1)
        return best
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
- [4064. Longest Subarray Divisible by K with At Most One Negation II](../../4001-4500/4064-longest-subarray-divisible-by-k-with-at-most-one-negation-ii/)
- [2958. Length of Longest Subarray With at Most K Frequency](../../2501-3000/2958-length-of-longest-subarray-with-at-most-k-frequency/)
- [4032. Longest Subarray With at Most K Distinct Prime Factors](../../4001-4500/4032-longest-subarray-with-at-most-k-distinct-prime-factors/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-i/)
