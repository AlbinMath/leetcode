# LeetCode 3624: Number of Integers With Popcount-Depth Equal to K II

**LeetCode Problem #3624 — Number of Integers With Popcount-Depth Equal to K II**
Solve LeetCode Number of Integers With Popcount-Depth Equal to K II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Integers With Popcount-Depth Equal to K II |
| LeetCode | #3624 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

For any positive integer `x`, define the following sequence:

`p_0 = x` 
 `p_i+1 = popcount(p_i)` for all `i >= 0`, where `popcount(y)` is the number of set bits (1's) in the binary representation of `y`.

This sequence will eventually reach the value 1.

The **popcount-depth** of `x` is defined as the **smallest** integer `d >= 0` such that `p_d = 1`.

For example, if `x = 7` (binary representation `"111"`). Then, the sequence is: `7 &rarr; 3 &rarr; 2 &rarr; 1`, so the popcount-depth of 7 is 3.

You are also given a 2D integer array `queries`, where each `queries[i]` is either:

`[1, l, r, k]` - **Determine** the number of indices `j` such that `l <= j <= r` and the **popcount-depth** of `nums[j]` is equal to `k`. 
 `[2, idx, val]` - **Update** `nums[idx]` to `val`.

Return an integer array `answer`, where `answer[i]` is the number of indices for the `i^th` query of type `[1, l, r, k]`.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^15`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 3` or `4`
 
 `queries[i] == [1, l, r, k]` or,
- `queries[i] == [2, idx, val]`
- `0 <= l <= r <= n - 1`
- `0 <= k <= 5`
- `0 <= idx <= n - 1`
- `1 <= val <= 10^15`

## Examples
### Example 1
- **Input:** `nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]]`
- **Output:** `[2,1]`
- **Explanation:** `i` 
 `queries[i]` 
 `nums` 
 binary(`nums`) 
 popcount- 
 depth 
 `[l, r]` 
 `k` 
 Valid 
 `nums[j]` 
 updated 
 `nums` 
 Answer 
 
 
 
 
 0 
 [1,0,1,1] 
 [2,4] 
 [10, 100] 
 [1, 1] 
 [0, 1] 
 1 
 [0, 1] 
 &mdash; 
 2 
 
 
 1 
 [2,1,1] 
 [2,4] 
 [10, 100] 
 [1, 1] 
 &mdash; 
 &mdash; 
 &mdash; 
 [2,1] 
 &mdash; 
 
 
 2 
 [1,0,1,0] 
 [2,1] 
 [10, 1] 
 [1, 0] 
 [0, 1] 
 0 
 [1] 
 &mdash; 
 1 
 
 
 

 Thus, the final `answer` is `[2, 1]`.

### Example 2
- **Input:** `nums = [3,5,6], queries = [[1,0,2,2],[2,1,4],[1,1,2,1],[1,0,1,0]]`
- **Output:** `[3,1,0]`
- **Explanation:** `i` 
 `queries[i]` 
 `nums` 
 binary(`nums`) 
 popcount- 
 depth 
 `[l, r]` 
 `k` 
 Valid 
 `nums[j]` 
 updated 
 `nums` 
 Answer 
 
 
 
 
 0 
 [1,0,2,2] 
 [3, 5, 6] 
 [11, 101, 110] 
 [2, 2, 2] 
 [0, 2] 
 2 
 [0, 1, 2] 
 &mdash; 
 3 
 
 
 1 
 [2,1,4] 
 [3, 5, 6] 
 [11, 101, 110] 
 [2, 2, 2] 
 &mdash; 
 &mdash; 
 &mdash; 
 [3, 4, 6] 
 &mdash; 
 
 
 2 
 [1,1,2,1] 
 [3, 4, 6] 
 [11, 100, 110] 
 [2, 1, 2] 
 [1, 2] 
 1 
 [1] 
 &mdash; 
 1 
 
 
 3 
 [1,0,1,0] 
 [3, 4, 6] 
 [11, 100, 110] 
 [2, 1, 2] 
 [0, 1] 
 0 
 [] 
 &mdash; 
 0 
 
 
 

 Thus, the final `answer` is `[3, 1, 0]`.

### Example 3
- **Input:** `nums = [1,2], queries = [[1,0,1,1],[2,0,3],[1,0,0,1],[1,0,0,2]]`
- **Output:** `[1,0,1]`
- **Explanation:** `i` 
 `queries[i]` 
 `nums` 
 binary(`nums`) 
 popcount- 
 depth 
 `[l, r]` 
 `k` 
 Valid 
 `nums[j]` 
 updated 
 `nums` 
 Answer 
 
 
 
 
 0 
 [1,0,1,1] 
 [1, 2] 
 [1, 10] 
 [0, 1] 
 [0, 1] 
 1 
 [1] 
 &mdash; 
 1 
 
 
 1 
 [2,0,3] 
 [1, 2] 
 [1, 10] 
 [0, 1] 
 &mdash; 
 &mdash; 
 &mdash; 
 [3, 2] 
 
 
 
 2 
 [1,0,0,1] 
 [3, 2] 
 [11, 10] 
 [2, 1] 
 [0, 0] 
 1 
 [] 
 &mdash; 
 0 
 
 
 3 
 [1,0,0,2] 
 [3, 2] 
 [11, 10] 
 [2, 1] 
 [0, 0] 
 2 
 [0] 
 &mdash; 
 1 
 
 
 

 Thus, the final `answer` is `[1, 0, 1]`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Integers With Popcount-Depth Equal to K II**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,4], queries = [[1,0,1,1],[2,1,1],[1,0,1,0]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1]`.
4. **Verification:** `i` 
 `queries[i]` 
 `nums` 
 binary(`nums`) 
 popcount- 
 depth 
 `[l, r]` 
 `k` 
 Valid 
 `nums[j]` 
 updated 
 `nums` 
 Answer 
 
 
 
 
 0 
 [1,0,1,1] 
 [2,4] 
 [10, 100] 
 [1, 1] 
 [0, 1] 
 1 
 [0, 1] 
 &mdash; 
 2 
 
 
 1 
 [2,1,1] 
 [2,4] 
 [10, 100] 
 [1, 1] 
 &mdash; 
 &mdash; 
 &mdash; 
 [2,1] 
 &mdash; 
 
 
 2 
 [1,0,1,0] 
 [2,1] 
 [10, 1] 
 [1, 0] 
 [0, 1] 
 0 
 [1] 
 &mdash; 
 1 
 
 
 

 Thus, the final `answer` is `[2, 1]`.

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
class Solution:
    def popcountDepth(self, nums, queries):
        n = len(nums)
        bit = [[0] * (n + 1) for _ in range(6)]

        def depth(x):
            d = 0
            while x > 1:
                x = bin(x).count('1')
                d += 1
            return d

        def update(k, i, delta):
            i += 1
            while i <= n:
                bit[k][i] += delta
                i += i & -i

        def prefix(k, i):
            if i < 0:
                return 0
            i += 1
            res = 0
            while i > 0:
                res += bit[k][i]
                i -= i & -i
            return res

        depths = [depth(x) for x in nums]

        for i, d in enumerate(depths):
            update(d, i, 1)

        ans = []

        for q in queries:
            if q[0] == 1:
                _, l, r, k = q
                ans.append(prefix(k, r) - prefix(k, l - 1))
            else:
                _, idx, val = q
                old = depths[idx]
                new = depth(val)

                if old != new:
                    update(old, idx, -1)
                    update(new, idx, 1)
                    depths[idx] = new

                nums[idx] = val

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
- [3621. Number of Integers With Popcount-Depth Equal to K I](../../3501-4000/3937-number-of-integers-with-popcount-depth-equal-to-k-i/)
- [3226. Number of Bit Changes to Make Two Integers Equal](../../3501-4000/3508-number-of-bit-changes-to-make-two-integers-equal/)
- [1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](../../1001-1500/1445-number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/)
