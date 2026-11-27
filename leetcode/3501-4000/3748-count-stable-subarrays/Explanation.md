# LeetCode 3748: Count Stable Subarrays

**LeetCode Problem #3748 — Count Stable Subarrays**
Solve LeetCode Count Stable Subarrays using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Stable Subarrays |
| LeetCode | #3748 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

A ** subarray ** of `nums` is called **stable** if it contains **no inversions**, i.e., there is no pair of indices `i < j` such that `nums[i] > nums[j]`.

You are also given a **2D integer array** `queries` of length `q`, where each `queries[i] = [l_i, r_i]` represents a query. For each query `[l_i, r_i]`, compute the number of **stable subarrays** that lie entirely within the segment `nums[l_i..r_i]`.

Return an integer array `ans` of length `q`, where `ans[i]` is the answer to the `i^th` query.​​​​​​​​​​​​​​

**Note**:

A single element subarray is considered stable.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i] = [l_i, r_i]`
- `0 <= l_i <= r_i <= nums.length - 1`

## Examples
### Example 1
- **Input:** `nums = [3,1,2], queries = [[0,1],[1,2],[0,2]]`
- **Output:** `[2,3,4]`
- **Explanation:** ​​​​​ 

 
 For `queries[0] = [0, 1]`, the subarray is `[nums[0], nums[1]] = [3, 1]`.

 
 The stable subarrays are `[3]` and `[1]`. The total number of stable subarrays is 2. 
 
 
 For `queries[1] = [1, 2]`, the subarray is `[nums[1], nums[2]] = [1, 2]`.
 
 The stable subarrays are `[1]`, `[2]`, and `[1, 2]`. The total number of stable subarrays is 3. 
 
 
 For `queries[2] = [0, 2]`, the subarray is `[nums[0], nums[1], nums[2]] = [3, 1, 2]`.
 
 The stable subarrays are `[3]`, `[1]`, `[2]`, and `[1, 2]`. The total number of stable subarrays is 4. 
 
 
 

 Thus, `ans = [2, 3, 4]`.

### Example 2
- **Input:** `nums = [2,2], queries = [[0,1],[0,0]]`
- **Output:** `[3,1]`
- **Explanation:** For `queries[0] = [0, 1]`, the subarray is `[nums[0], nums[1]] = [2, 2]`.

 
 The stable subarrays are `[2]`, `[2]`, and `[2, 2]`. The total number of stable subarrays is 3. 
 
 
 For `queries[1] = [0, 0]`, the subarray is `[nums[0]] = [2]`.
 
 The stable subarray is `[2]`. The total number of stable subarrays is 1. 
 
 
 

 Thus, `ans = [3, 1]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Stable Subarrays**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,1,2], queries = [[0,1],[1,2],[0,2]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3,4]`.
4. **Verification:** ​​​​​ 

 
 For `queries[0] = [0, 1]`, the subarray is `[nums[0], nums[1]] = [3, 1]`.

 
 The stable subarrays are `[3]` and `[1]`. The total number of stable subarrays is 2. 
 
 
 For `queries[1] = [1, 2]`, the subarray is `[nums[1], nums[2]] = [1, 2]`.
 
 The stable subarrays are `[1]`, `[2]`, and `[1, 2]`. The total number of stable subarrays is 3. 
 
 
 For `queries[2] = [0, 2]`, the subarray is `[nums[0], nums[1], nums[2]] = [3, 1, 2]`.
 
 The stable subarrays are `[3]`, `[1]`, `[2]`, and `[1, 2]`. The total number of stable subarrays is 4. 
 
 
 

 Thus, `ans = [2, 3, 4]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        run_id = [0] * n
        starts, ends = [0], []
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                ends.append(i - 1)
                starts.append(i)
            run_id[i] = len(starts) - 1
        ends.append(n - 1)

        k = len(starts)
        pre = [0] * (k + 1)
        for j in range(k):
            L = ends[j] - starts[j] + 1
            pre[j + 1] = pre[j] + L * (L + 1) // 2

        ans = []
        for l, r in queries:
            a, b = run_id[l], run_id[r]
            if a == b:
                L = r - l + 1
                ans.append(L * (L + 1) // 2)
            else:
                l1 = ends[a] - l + 1
                l2 = r - starts[b] + 1
                ans.append(l1 * (l1 + 1) // 2 + pre[b] - pre[a + 1] + l2 * (l2 + 1) // 2)
        return ans
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3728. Stable Subarrays With Equal Boundary and Interior Sum](../../3501-4000/3728-stable-subarrays-with-equal-boundary-and-interior-sum/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1248-count-number-of-nice-subarrays/)
- [2302. Count Subarrays With Score Less Than K](../../2001-2500/2302-count-subarrays-with-score-less-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-stable-subarrays/)
