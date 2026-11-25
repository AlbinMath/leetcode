# LeetCode 1994: The Number of Good Subsets

**LeetCode Problem #1994 — The Number of Good Subsets**
Solve LeetCode The Number of Good Subsets using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Number of Good Subsets |
| LeetCode | #1994 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. We call a subset of `nums` **good** if its product can be represented as a product of one or more **distinct prime** numbers.

For example, if `nums = [1, 2, 3, 4]`:

`[2, 3]`, `[1, 2, 3]`, and `[1, 3]` are **good** subsets with products `6 = 2*3`, `6 = 2*3`, and `3 = 3` respectively. 
 `[1, 4]` and `[4]` are not **good** subsets with products `4 = 2*2` and `4 = 2*2` respectively.

Return *the number of different **good** subsets in *`nums`* **modulo** *`10^9 + 7`.

A **subset** of `nums` is any array that can be obtained by deleting some (possibly none or all) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 30`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4]`
- **Output:** `6`
- **Explanation:** The good subsets are:
- [1,2]: product is 2, which is the product of distinct prime 2.
- [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [1,3]: product is 3, which is the product of distinct prime 3.
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [3]: product is 3, which is the product of distinct prime 3.

### Example 2
- **Input:** `nums = [4,2,3,15]`
- **Output:** `5`
- **Explanation:** The good subsets are:
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5.
- [3]: product is 3, which is the product of distinct prime 3.
- [15]: product is 15, which is the product of distinct primes 3 and 5.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **The Number of Good Subsets**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The good subsets are:
- [1,2]: product is 2, which is the product of distinct prime 2.
- [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [1,3]: product is 3, which is the product of distinct prime 3.
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [3]: product is 3, which is the product of distinct prime 3.

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
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        freq = [0] * 31

        for num in nums:
            freq[num] += 1

        # dp[mask] = number of subsets with this prime-factor mask
        dp = [0] * (1 << 10)
        dp[0] = 1

        for num in range(2, 31):
            if freq[num] == 0:
                continue

            mask = 0
            valid = True

            for i, prime in enumerate(primes):
                if num % (prime * prime) == 0:
                    valid = False
                    break

                if num % prime == 0:
                    mask |= 1 << i

            if not valid:
                continue

            # Descending masks prevent using the same number twice
            for state in range((1 << 10) - 1, -1, -1):
                if state & mask == 0:
                    new_state = state | mask
                    dp[new_state] = (
                        dp[new_state] + dp[state] * freq[num]
                    ) % MOD

        # Exclude the empty subset (mask = 0)
        answer = sum(dp[1:]) % MOD

        # Each good subset can include any subset of the 1s
        answer = answer * pow(2, freq[1], MOD) % MOD

        return answer
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
- [2044. Count Number of Maximum Bitwise-OR Subsets](../../2001-2500/2044-count-number-of-maximum-bitwise-or-subsets/)
- [2572. Count the Number of Square-Free Subsets](../../2501-3000/2572-count-the-number-of-square-free-subsets/)
- [2597. The Number of Beautiful Subsets](../../2501-3000/2597-the-number-of-beautiful-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-number-of-good-subsets/)
