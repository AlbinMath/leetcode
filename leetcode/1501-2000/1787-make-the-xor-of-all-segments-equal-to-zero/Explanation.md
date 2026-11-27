# LeetCode 1787: Make the XOR of All Segments Equal to Zero

**LeetCode Problem #1787 — Make the XOR of All Segments Equal to Zero**
Solve LeetCode Make the XOR of All Segments Equal to Zero using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make the XOR of All Segments Equal to Zero |
| LeetCode | #1787 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `nums`​​​ and an integer `k`​​​​​. The XOR of a segment `[left, right]` where `left <= right` is the `XOR` of all the elements with indices between `left` and `right`, inclusive: `nums[left] XOR nums[left+1] XOR ... XOR nums[right]`.

Return *the minimum number of elements to change in the array *such that the `XOR` of all segments of size `k`​​​​​​ is equal to zero.

## Constraints
- `1 <= k <= nums.length <= 2000`
- `​​​​​​0 <= nums[i] < 2^10`

## Examples
### Example 1
- **Input:** `nums = [1,2,0,3,0], k = 1`
- **Output:** `3`
- **Explanation:** Modify the array from [

### Example 2
- **Input:** `nums = [3,4,5,2,1,7,3,4,7], k = 3`
- **Output:** `3`
- **Explanation:** Modify the array from [3,4,

### Example 3
- **Input:** `nums = [1,2,4,1,2,5,1,2,6], k = 3`
- **Output:** `3`
- **Explanation:** Modify the array from [1,2,

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Make the XOR of All Segments Equal to Zero**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,0,3,0], k = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Modify the array from [

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
from collections import Counter

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        M = 1 << 10
        INF = float('inf')
        dp = [INF] * M
        dp[0] = 0

        for j in range(k):
            cnt = Counter(nums[j::k])
            size = sum(cnt.values())
            best = min(dp)
            new_dp = [best + size] * M   # change whole class to any value
            for x in range(M):
                if dp[x] == INF:
                    continue
                for v, f in cnt.items():
                    t = x ^ v
                    c = dp[x] + size - f
                    if c < new_dp[t]:
                        new_dp[t] = c
            dp = new_dp

        return dp[0]
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
- [2772. Apply Operations to Make All Array Elements Equal to Zero](../../2501-3000/2772-apply-operations-to-make-all-array-elements-equal-to-zero/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [1466. Reorder Routes to Make All Paths Lead to the City Zero](../../1001-1500/1466-reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/)
