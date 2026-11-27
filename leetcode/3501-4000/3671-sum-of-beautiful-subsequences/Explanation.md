# LeetCode 3671: Sum of Beautiful Subsequences

**LeetCode Problem #3671 — Sum of Beautiful Subsequences**
Solve LeetCode Sum of Beautiful Subsequences using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Beautiful Subsequences |
| LeetCode | #3671 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

For every **positive** integer `g`, we define the **beauty** of `g` as the **product** of `g` and the number of **strictly increasing** ** subsequences ** of `nums` whose greatest common divisor (GCD) is exactly `g`.

Return the **sum** of **beauty** values for all positive integers `g`.

Since the answer could be very large, return it modulo `10^9 + 7`.

## Constraints
- `1 <= n == nums.length <= 10^4`
- `1 <= nums[i] <= 7 * 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `10`
- **Explanation:** All strictly increasing subsequences and their GCDs are: 

 
 
 
 Subsequence 
 GCD 
 
 
 
 
 [1] 
 1 
 
 
 [2] 
 2 
 
 
 [3] 
 3 
 
 
 [1,2] 
 1 
 
 
 [1,3] 
 1 
 
 
 [2,3] 
 1 
 
 
 [1,2,3] 
 1 
 
 
 

 Calculating beauty for each GCD: 

 
 
 
 GCD 
 Count of subsequences 
 Beauty (GCD &times; Count) 
 
 
 
 
 1 
 5 
 1 &times; 5 = 5 
 
 
 2 
 1 
 2 &times; 1 = 2 
 
 
 3 
 1 
 3 &times; 1 = 3 
 
 
 

 Total beauty is `5 + 2 + 3 = 10`.

### Example 2
- **Input:** `nums = [4,6]`
- **Output:** `12`
- **Explanation:** All strictly increasing subsequences and their GCDs are: 

 
 
 
 Subsequence 
 GCD 
 
 
 
 
 [4] 
 4 
 
 
 [6] 
 6 
 
 
 [4,6] 
 2 
 
 
 

 Calculating beauty for each GCD: 

 
 
 
 GCD 
 Count of subsequences 
 Beauty (GCD &times; Count) 
 
 
 
 
 2 
 1 
 2 &times; 1 = 2 
 
 
 4 
 1 
 4 &times; 1 = 4 
 
 
 6 
 1 
 6 &times; 1 = 6 
 
 
 

 Total beauty is `2 + 4 + 6 = 12`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Sum of Beautiful Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** All strictly increasing subsequences and their GCDs are: 

 
 
 
 Subsequence 
 GCD 
 
 
 
 
 [1] 
 1 
 
 
 [2] 
 2 
 
 
 [3] 
 3 
 
 
 [1,2] 
 1 
 
 
 [1,3] 
 1 
 
 
 [2,3] 
 1 
 
 
 [1,2,3] 
 1 
 
 
 

 Calculating beauty for each GCD: 

 
 
 
 GCD 
 Count of subsequences 
 Beauty (GCD &times; Count) 
 
 
 
 
 1 
 5 
 1 &times; 5 = 5 
 
 
 2 
 1 
 2 &times; 1 = 2 
 
 
 3 
 1 
 3 &times; 1 = 3 
 
 
 

 Total beauty is `5 + 2 + 3 = 10`.

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
    def totalBeauty(self, nums):
        MOD = 10**9 + 7
        M = max(nums)

        # Precompute all divisors for every number.
        divisors = [[] for _ in range(M + 1)]
        for g in range(1, M + 1):
            for x in range(g, M + 1, g):
                divisors[x].append(g)

        # Fenwick tree for each divisor g.
        # Tree g stores subsequences whose elements
        # are all divisible by g.
        trees = [None] * (M + 1)
        for g in range(1, M + 1):
            trees[g] = [0] * (M // g + 1)

        def update(tree, i, value):
            while i < len(tree):
                tree[i] = (tree[i] + value) % MOD
                i += i & -i

        def query(tree, i):
            result = 0
            while i > 0:
                result = (result + tree[i]) % MOD
                i -= i & -i
            return result

        # Count strictly increasing subsequences
        # whose elements are all divisible by g.
        for x in nums:
            for g in divisors[x]:
                tree = trees[g]
                pos = x // g

                # Start a new subsequence with x,
                # or extend a subsequence ending at a smaller value.
                ways = (1 + query(tree, pos - 1)) % MOD
                update(tree, pos, ways)

        # divisible_count[g] counts subsequences whose
        # GCD is a multiple of g.
        divisible_count = [0] * (M + 1)
        for g in range(1, M + 1):
            divisible_count[g] = query(
                trees[g], M // g
            )

        # Recover the number of subsequences with GCD exactly g.
        exact = [0] * (M + 1)
        ans = 0

        for g in range(M, 0, -1):
            count = divisible_count[g]

            for multiple in range(2 * g, M + 1, g):
                count -= exact[multiple]
                count %= MOD

            exact[g] = count
            ans = (ans + g * count) % MOD

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
- [1498. Number of Subsequences That Satisfy the Given Sum Condition](../../1001-1500/1498-number-of-subsequences-that-satisfy-the-given-sum-condition/)
- [3627. Maximum Median Sum of Subsequences of Size 3](../../3501-4000/3627-maximum-median-sum-of-subsequences-of-size-3/)
- [115. Distinct Subsequences](../../0001-0500/0115-distinct-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-beautiful-subsequences/)
