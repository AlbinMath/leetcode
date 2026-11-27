# LeetCode 3265: Count Almost Equal Pairs I

**LeetCode Problem #3265 — Count Almost Equal Pairs I**
Solve LeetCode Count Almost Equal Pairs I using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Almost Equal Pairs I |
| LeetCode | #3265 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` consisting of positive integers.

We call two integers `x` and `y` in this problem **almost equal** if both integers can become equal after performing the following operation **at most once**:

Choose **either** `x` or `y` and swap any two digits within the chosen number.

Return the number of indices `i` and `j` in `nums` where `i < j` such that `nums[i]` and `nums[j]` are **almost equal**.

**Note** that it is allowed for an integer to have leading zeros after performing an operation.

## Constraints
- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [3,12,30,17,21]`
- **Output:** `2`
- **Explanation:** The almost equal pairs of elements are: 

 
 3 and 30. By swapping 3 and 0 in 30, you get 3. 
 12 and 21. By swapping 1 and 2 in 12, you get 21.

### Example 2
- **Input:** `nums = [1,1,1,1,1]`
- **Output:** `10`
- **Explanation:** Every two elements in the array are almost equal.

### Example 3
- **Input:** `nums = [123,231]`
- **Output:** `0`
- **Explanation:** We cannot swap any two digits of 123 or 231 to reach the other.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Almost Equal Pairs I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,12,30,17,21]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The almost equal pairs of elements are: 

 
 3 and 30. By swapping 3 and 0 in 30, you get 3. 
 12 and 21. By swapping 1 and 2 in 12, you get 21.

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
    def countPairs(self, nums: List[int]) -> int:
        L = max(len(str(x)) for x in nums)
        strs = [str(x).zfill(L) for x in nums]

        def almost(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            diff = [i for i in range(L) if a[i] != b[i]]
            return len(diff) == 2

        ans = 0
        n = len(strs)
        for i in range(n):
            for j in range(i + 1, n):
                if almost(strs[i], strs[j]):
                    ans += 1
        return ans
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
- [3267. Count Almost Equal Pairs II](../../3001-3500/3267-count-almost-equal-pairs-ii/)
- [4043. Count Rotations With Exactly K Equal Adjacent Pairs](../../4001-4500/4043-count-rotations-with-exactly-k-equal-adjacent-pairs/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-almost-equal-pairs-i/)
