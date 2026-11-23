# LeetCode 4054: Count Shadow Pairs I

**LeetCode Problem #4054 — Count Shadow Pairs I**
Solve LeetCode Count Shadow Pairs I using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Shadow Pairs I |
| LeetCode | #4054 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n`.

A pair of indices `(i, j)` is called a **shadow pair** if all of the following conditions are satisfied:

`0 <= i < j < n` 
 `nums[i] < nums[j]` 
 There **does not exist** an index `k` such that `i < k < j` and `nums[k] < nums[i] < nums[j]`.

Return the total number of **shadow pairs**.

## Constraints
- `3 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [3,1,4,1,5]`
- **Output:** `3`
- **Explanation:** `(i, j)` 
 `nums[i]` 
 `nums[j]` 
 Shadow Pair 
 
 
 
 
 (1, 2) 
 1 
 4 
 No index `k` exists such that `1 < k < 2` 
 
 
 (1, 4) 
 1 
 5 
 `nums[2] = 4` and `nums[3] = 1` are not smaller than 1 
 
 
 (3, 4) 
 1 
 5 
 No index `k` exists such that `3 < k < 4` 
 
 
 

 Thus, the answer is 3.

### Example 2
- **Input:** `nums = [6,7,6,6,7]`
- **Output:** `4`
- **Explanation:** `(i, j)` 
 `nums[i]` 
 `nums[j]` 
 Shadow Pair 
 
 
 
 
 (0, 1) 
 6 
 7 
 No index `k` exists such that `0 < k < 1` 
 
 
 (0, 4) 
 6 
 7 
 `nums[1] = 7`, `nums[2] = 6`, and `nums[3] = 6` are not smaller than 6 
 
 
 (2, 4) 
 6 
 7 
 `nums[3] = 6` is not smaller than 6 
 
 
 (3, 4) 
 6 
 7 
 No index `k` exists such that `3 < k < 4` 
 
 
 

 Thus, the answer is 4.

### Example 3
- **Input:** `nums = [1,2,3,4]`
- **Output:** `6`
- **Explanation:** `(i, j)` 
 `nums[i]` 
 `nums[j]` 
 Shadow Pair 
 
 
 
 
 (0, 1) 
 1 
 2 
 No index `k` exists such that `0 < k < 1` 
 
 
 (0, 2) 
 1 
 3 
 `nums[1] = 2` is not smaller than 1 
 
 
 (0, 3) 
 1 
 4 
 `nums[1] = 2` and `nums[2] = 3` are not smaller than 1 
 
 
 (1, 2) 
 2 
 3 
 No index `k` exists such that `1 < k < 2` 
 
 
 (1, 3) 
 2 
 4 
 `nums[2] = 3` is not smaller than 2 
 
 
 (2, 3) 
 3 
 4 
 No index `k` exists such that `2 < k < 3` 
 
 
 

 Thus, the answer is 6.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Shadow Pairs I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,4,1,5]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** `(i, j)` 
 `nums[i]` 
 `nums[j]` 
 Shadow Pair 
 
 
 
 
 (1, 2) 
 1 
 4 
 No index `k` exists such that `1 < k < 2` 
 
 
 (1, 4) 
 1 
 5 
 `nums[2] = 4` and `nums[3] = 1` are not smaller than 1 
 
 
 (3, 4) 
 1 
 5 
 No index `k` exists such that `3 < k < 4` 
 
 
 

 Thus, the answer is 3.

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
    def shadowPairs(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []  # [value, count, ns, idx]
        ans = 0
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while stack and stack[-1][0] > x:
                stack.pop()
            if stack and stack[-1][0] == x:
                top = stack[-1]
                ns, eq = top[2], top[1]
                ans += ns - i - 1 - eq
                top[1] += 1
                top[3] = i
            else:
                ns = stack[-1][3] if stack else n
                ans += ns - i - 1
                stack.append([x, 1, ns, i])
        return ans
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
- [4055. Count Shadow Pairs II](../../4001-4500/4326-count-shadow-pairs-ii/)
- [1782. Count Pairs Of Nodes](../../1501-2000/1891-count-pairs-of-nodes/)
- [1803. Count Pairs With XOR in a Range](../../1501-2000/1907-count-pairs-with-xor-in-a-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-shadow-pairs-i/)
