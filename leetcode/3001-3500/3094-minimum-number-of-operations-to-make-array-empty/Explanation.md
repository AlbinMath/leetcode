# LeetCode 2870: Minimum Number of Operations to Make Array Empty

**LeetCode Problem #2870 — Minimum Number of Operations to Make Array Empty**
Solve LeetCode Minimum Number of Operations to Make Array Empty using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Operations to Make Array Empty |
| LeetCode | #2870 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array `nums` consisting of positive integers.

There are two types of operations that you can apply on the array **any** number of times:

Choose **two** elements with **equal** values and **delete** them from the array. 
 Choose **three** elements with **equal** values and **delete** them from the array.

Return *the **minimum** number of operations required to make the array empty, or *`-1`* if it is not possible*.

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [2,3,3,2,2,4,2,3,4]`
- **Output:** `4`
- **Explanation:** We can apply the following operations to make the array empty:
- Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
- Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
- Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
- Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
It can be shown that we cannot make the array empty in less than 4 operations.

### Example 2
- **Input:** `nums = [2,1,2,2,3,3]`
- **Output:** `-1`
- **Explanation:** It is impossible to empty the array.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Operations to Make Array Empty**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,3,2,2,4,2,3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can apply the following operations to make the array empty:
- Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
- Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
- Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
- Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
It can be shown that we cannot make the array empty in less than 4 operations.

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

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        freq = Counter(nums)
        total_ops = 0
        
        for count in freq.values():
            if count == 1:
                return -1
            total_ops += (count + 2) // 3
            
        return total_ops
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
- [2009. Minimum Number of Operations to Make Array Continuous](../../2001-2500/2119-minimum-number-of-operations-to-make-array-continuous/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2753-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../3001-3500/3249-minimum-number-of-operations-to-make-array-xor-equal-to-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/)
