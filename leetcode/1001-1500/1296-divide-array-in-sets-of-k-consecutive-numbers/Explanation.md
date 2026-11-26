# LeetCode 1296: Divide Array in Sets of K Consecutive Numbers

**LeetCode Problem #1296 — Divide Array in Sets of K Consecutive Numbers**
Solve LeetCode Divide Array in Sets of K Consecutive Numbers using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Divide Array in Sets of K Consecutive Numbers |
| LeetCode | #1296 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `nums` and a positive integer `k`, check whether it is possible to divide this array into sets of `k` consecutive numbers.

Return `true` *if it is possible*.** **Otherwise, return `false`.

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,3,4,4,5,6], k = 4`
- **Output:** `true`
- **Explanation:** Array can be divided into [1,2,3,4] and [3,4,5,6].

### Example 2
- **Input:** `nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3`
- **Output:** `true`
- **Explanation:** Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].

### Example 3
- **Input:** `nums = [1,2,3,4], k = 3`
- **Output:** `false`
- **Explanation:** Each array should be divided in subarrays of size 3.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Divide Array in Sets of K Consecutive Numbers**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,3,4,4,5,6], k = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Array can be divided into [1,2,3,4] and [3,4,5,6].

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
from collections import Counter
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
            
        counts = Counter(nums)
        
        for start in sorted(counts):
            needed = counts[start]
            if needed > 0:
                for num in range(start, start + k):
                    if counts[num] < needed:
                        return False
                    counts[num] -= needed
                    
        return True
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
- [532. K-diff Pairs in an Array](../../0501-1000/0532-k-diff-pairs-in-an-array/)
- [629. K Inverse Pairs Array](../../0501-1000/0629-k-inverse-pairs-array/)
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/)
