# LeetCode 646: Maximum Length of Pair Chain

**LeetCode Problem #646 — Maximum Length of Pair Chain**
Solve LeetCode Maximum Length of Pair Chain using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Length of Pair Chain |
| LeetCode | #646 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of `n` pairs `pairs` where `pairs[i] = [left_i, right_i]` and `left_i < right_i`.

A pair `p2 = [c, d]` **follows** a pair `p1 = [a, b]` if `b < c`. A **chain** of pairs can be formed in this fashion.

Return *the length longest chain which can be formed*.

You do not need to use up all the given intervals. You can select pairs in any order.

## Constraints
- `n == pairs.length`
- `1 <= n <= 1000`
- `-1000 <= left_i < right_i <= 1000`

## Examples
### Example 1
- **Input:** `pairs = [[1,2],[2,3],[3,4]]`
- **Output:** `2`
- **Explanation:** The longest chain is [1,2] -> [3,4].

### Example 2
- **Input:** `pairs = [[1,2],[7,8],[4,5]]`
- **Output:** `3`
- **Explanation:** The longest chain is [1,2] -> [4,5] -> [7,8].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Length of Pair Chain**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `pairs = [[1,2],[2,3],[3,4]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The longest chain is [1,2] -> [3,4].

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
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])
        cur_end = float('-inf')
        count = 0
        for left, right in pairs:
            if left > cur_end:
                count += 1
                cur_end = right
        return count
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
- [718. Maximum Length of Repeated Subarray](../../0501-1000/0718-maximum-length-of-repeated-subarray/)
- [1239. Maximum Length of a Concatenated String with Unique Characters](../../1001-1500/1239-maximum-length-of-a-concatenated-string-with-unique-characters/)
- [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](../../1001-1500/1292-maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-length-of-pair-chain/)
