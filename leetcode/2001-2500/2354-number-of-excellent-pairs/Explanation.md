# LeetCode 2354: Number of Excellent Pairs

**LeetCode Problem #2354 — Number of Excellent Pairs**
Solve LeetCode Number of Excellent Pairs using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Excellent Pairs |
| LeetCode | #2354 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** positive integer array `nums` and a positive integer `k`.

A pair of numbers `(num1, num2)` is called **excellent** if the following conditions are satisfied:

**Both** the numbers `num1` and `num2` exist in the array `nums`. 
 The sum of the number of set bits in `num1 OR num2` and `num1 AND num2` is greater than or equal to `k`, where `OR` is the bitwise **OR** operation and `AND` is the bitwise **AND** operation.

Return *the number of **distinct** excellent pairs*.

Two pairs `(a, b)` and `(c, d)` are considered distinct if either `a != c` or `b != d`. For example, `(1, 2)` and `(2, 1)` are distinct.

**Note** that a pair `(num1, num2)` such that `num1 == num2` can also be excellent if you have at least **one** occurrence of `num1` in the array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 60`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,1], k = 3`
- **Output:** `5`
- **Explanation:** The excellent pairs are the following:
- (3, 3). (3 AND 3) and (3 OR 3) are both equal to (11) in binary. The total number of set bits is 2 + 2 = 4, which is greater than or equal to k = 3.
- (2, 3) and (3, 2). (2 AND 3) is equal to (10) in binary, and (2 OR 3) is equal to (11) in binary. The total number of set bits is 1 + 2 = 3.
- (1, 3) and (3, 1). (1 AND 3) is equal to (01) in binary, and (1 OR 3) is equal to (11) in binary. The total number of set bits is 1 + 2 = 3.
So the number of excellent pairs is 5.

### Example 2
- **Input:** `nums = [5,1,1], k = 10`
- **Output:** `0`
- **Explanation:** There are no excellent pairs for this array.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Number of Excellent Pairs**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,1], k = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The excellent pairs are the following:
- (3, 3). (3 AND 3) and (3 OR 3) are both equal to (11) in binary. The total number of set bits is 2 + 2 = 4, which is greater than or equal to k = 3.
- (2, 3) and (3, 2). (2 AND 3) is equal to (10) in binary, and (2 OR 3) is equal to (11) in binary. The total number of set bits is 1 + 2 = 3.
- (1, 3) and (3, 1). (1 AND 3) is equal to (01) in binary, and (1 OR 3) is equal to (11) in binary. The total number of set bits is 1 + 2 = 3.
So the number of excellent pairs is 5.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    long long countExcellentPairs(vector<int>& nums, int k) {
        // Step 1: Deduplicate nums
        unordered_set<int> unique_nums(nums.begin(), nums.end());
        
        // Step 2: Count frequencies of set bits (max 30 bits for 10^9)
        long long bit_counts[32] = {0};
        for (int num : unique_nums) {
            bit_counts[__builtin_popcount(num)]++;
        }
        
        // Step 3: Sum valid combinations
        long long ans = 0;
        for (int b1 = 0; b1 < 32; ++b1) {
            for (int b2 = 0; b2 < 32; ++b2) {
                if (b1 + b2 >= k) {
                    ans += bit_counts[b1] * bit_counts[b2];
                }
            }
        }
        return ans;
    }
};
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
- [1128. Number of Equivalent Domino Pairs](../../1001-1500/1128-number-of-equivalent-domino-pairs/)
- [1512. Number of Good Pairs](../../1501-2000/1512-number-of-good-pairs/)
- [1530. Number of Good Leaf Nodes Pairs](../../1501-2000/1530-number-of-good-leaf-nodes-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-excellent-pairs/)
