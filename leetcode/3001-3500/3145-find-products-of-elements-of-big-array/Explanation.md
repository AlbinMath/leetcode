# LeetCode 3145: Find Products of Elements of Big Array

**LeetCode Problem #3145 — Find Products of Elements of Big Array**
Solve LeetCode Find Products of Elements of Big Array using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Products of Elements of Big Array |
| LeetCode | #3145 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **powerful array** of a non-negative integer `x` is defined as the shortest sorted array of powers of two that sum up to `x`. The table below illustrates examples of how the **powerful array** is determined. It can be proven that the powerful array of `x` is unique.

num 
 Binary Representation 
 powerful array 
 
 
 1 
 0000 1 
 [1] 
 
 
 8 
 0 1 000 
 [8] 
 
 
 10 
 0 1 0 1 0 
 [2, 8] 
 
 
 13 
 0 11 0 1 
 [1, 4, 8] 
 
 
 23 
 1 0 111 
 [1, 2, 4, 16]

The array `big_nums` is created by concatenating the **powerful arrays** for every positive integer `i` in ascending order: 1, 2, 3, and so on. Thus, `big_nums` begins as `[ 1 , 2 , 1, 2 , 4 , 1, 4 , 2, 4 , 1, 2, 4 , 8 , ...]`.

You are given a 2D integer matrix `queries`, where for `queries[i] = [from_i, to_i, mod_i]` you should calculate `(big_nums[from_i] * big_nums[from_i + 1] * ... * big_nums[to_i]) % mod_i` .

Return an integer array `answer` such that `answer[i]` is the answer to the `i^th` query.

## Constraints
- `1 <= queries.length <= 500`
- `queries[i].length == 3`
- `0 <= queries[i][0] <= queries[i][1] <= 10^15`
- `1 <= queries[i][2] <= 10^5`

## Examples
### Example 1
- **Input:** `queries = [[1,3,7]]`
- **Output:** `[4]`
- **Explanation:** There is one query. 

 `big_nums[1..3] = [2,1,2]`. The product of them is 4. The result is `4 % 7 = 4.`

### Example 2
- **Input:** `queries = [[2,5,3],[7,7,4]]`
- **Output:** `[2,2]`
- **Explanation:** There are two queries. 

 First query: `big_nums[2..5] = [1,2,4,1]`. The product of them is 8. The result is `8 % 3 = 2`. 

 Second query: `big_nums[7] = 2`. The result is `2 % 4 = 2`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Products of Elements of Big Array**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `queries = [[1,3,7]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4]`.
4. **Verification:** There is one query. 

 `big_nums[1..3] = [2,1,2]`. The product of them is 4. The result is `4 % 7 = 4.`

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
class Solution(object):
    def findProductsOfElements(self, queries):
        def bit_counts(x):
            # (total set bits in 1..x, total sum of bit positions in 1..x)
            total = 0
            exps = 0
            n = x + 1
            for b in range(60):
                full = (n >> (b + 1)) << b
                rem = n & ((1 << (b + 1)) - 1)
                c = full + max(0, rem - (1 << b))
                total += c
                exps += b * c
            return total, exps

        def S(N):
            # sum of exponents of the first N elements of big_nums
            if N <= 0:
                return 0
            lo, hi = 0, 1 << 51
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if bit_counts(mid)[0] <= N:
                    lo = mid
                else:
                    hi = mid - 1
            x = lo
            c, e = bit_counts(x)
            r = N - c
            y = x + 1
            b = 0
            while r > 0:
                if (y >> b) & 1:
                    e += b
                    r -= 1
                b += 1
            return e

        res = []
        for f, t, m in queries:
            res.append(pow(2, S(t + 1) - S(f), m))
        return res
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
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2593-find-score-of-an-array-after-marking-all-elements/)
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)
- [462. Minimum Moves to Equal Array Elements II](../../0001-0500/0462-minimum-moves-to-equal-array-elements-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-products-of-elements-of-big-array/)
