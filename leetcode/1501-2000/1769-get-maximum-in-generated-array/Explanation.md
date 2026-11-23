# LeetCode 1646: Get Maximum in Generated Array

**LeetCode Problem #1646 — Get Maximum in Generated Array**
Solve LeetCode Get Maximum in Generated Array using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Get Maximum in Generated Array |
| LeetCode | #1646 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`. A **0-indexed** integer array `nums` of length `n + 1` is generated in the following way:

`nums[0] = 0` 
 `nums[1] = 1` 
 `nums[2 * i] = nums[i]` when `2 <= 2 * i <= n` 
 `nums[2 * i + 1] = nums[i] + nums[i + 1]` when `2 <= 2 * i + 1 <= n`

Return** ***the **maximum** integer in the array *`nums`​​​.

## Constraints
- `0 <= n <= 100`

## Examples
### Example 1
- **Input:** `n = 7`
- **Output:** `3`
- **Explanation:** According to the given rules:
 nums[0] = 0
 nums[1] = 1
 nums[(1 * 2) = 2] = nums[1] = 1
 nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
 nums[(2 * 2) = 4] = nums[2] = 1
 nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
 nums[(3 * 2) = 6] = nums[3] = 2
 nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.

### Example 2
- **Input:** `n = 2`
- **Output:** `1`
- **Explanation:** According to the given rules, nums = [0,1,1]. The maximum is max(0,1,1) = 1.

### Example 3
- **Input:** `n = 3`
- **Output:** `2`
- **Explanation:** According to the given rules, nums = [0,1,1,2]. The maximum is max(0,1,1,2) = 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Get Maximum in Generated Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 7`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** According to the given rules:
 nums[0] = 0
 nums[1] = 1
 nums[(1 * 2) = 2] = nums[1] = 1
 nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
 nums[(2 * 2) = 4] = nums[2] = 1
 nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
 nums[(3 * 2) = 6] = nums[3] = 2
 nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n == 0) {
            return 0;
        }

        vector<int> nums(n + 1, 0);
        nums[1] = 1;

        int maxi = 1;

        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                nums[i] = nums[i / 2];
            } else {
                nums[i] = nums[i / 2] + nums[i / 2 + 1];
            }

            maxi = max(maxi, nums[i]);
        }

        return maxi;
    }
};
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
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [1464. Maximum Product of Two Elements in an Array](../../1501-2000/1574-maximum-product-of-two-elements-in-an-array/)
- [1569. Number of Ways to Reorder Array to Get Same BST](../../1501-2000/1692-number-of-ways-to-reorder-array-to-get-same-bst/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/get-maximum-in-generated-array/)
