# LeetCode 2657: Find the Prefix Common Array of Two Arrays

**LeetCode Problem #2657 — Find the Prefix Common Array of Two Arrays**
Solve LeetCode Find the Prefix Common Array of Two Arrays using C++ and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Prefix Common Array of Two Arrays |
| LeetCode | #2657 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two **0-indexed **integer** **permutations `A` and `B` of length `n`.

A **prefix common array** of `A` and `B` is an array `C` such that `C[i]` is equal to the count of numbers that are present at or before the index `i` in both `A` and `B`.

Return *the **prefix common array** of *`A`* and *`B`.

A sequence of `n` integers is called a **permutation** if it contains all integers from `1` to `n` exactly once.

## Constraints
- `1 <= A.length == B.length == n <= 50`
- `1 <= A[i], B[i] <= n`
- `It is guaranteed that A and B are both a permutation of n integers.`

## Examples
### Example 1
- **Input:** `A = [1,3,2,4], B = [3,1,2,4]`
- **Output:** `[0,2,3,4]`
- **Explanation:** At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

### Example 2
- **Input:** `A = [2,3,1], B = [3,1,2]`
- **Output:** `[0,1,3]`
- **Explanation:** At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Maintain a frequency counter. For each index i, increment counts for A[i] and B[i]. If a count reaches 2, that number has appeared in both arrays up to this point. Track the running count of such numbers.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `A = [1,3,2,4], B = [3,1,2,4]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,2,3,4]`.
4. **Verification:** At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size();
        vector<int> ans(n);
        vector<int> freq(n + 1, 0);

        int common = 0;

        for (int i = 0; i < n; i++) {
            freq[A[i]]++;
            if (freq[A[i]] == 2)
                common++;

            freq[B[i]]++;
            if (freq[B[i]] == 2)
                common++;

            ans[i] = common;
        }

        return ans;
    }
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1385. Find the Distance Value Between Two Arrays](../../1001-1500/1486-find-the-distance-value-between-two-arrays/)
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../../1501-2000/1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [1979. Find Greatest Common Divisor of Array](../../2001-2500/2106-find-greatest-common-divisor-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/)
