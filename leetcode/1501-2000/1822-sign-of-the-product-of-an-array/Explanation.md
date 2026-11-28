# LeetCode 1822: Sign of the Product of an Array

**LeetCode Problem #1822 — Sign of the Product of an Array**
Solve LeetCode Sign of the Product of an Array using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sign of the Product of an Array |
| LeetCode | #1822 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Implement a function `signFunc(x)` that returns:

`1` if `x` is positive. 
 `-1` if `x` is negative. 
 `0` if `x` is equal to `0`.

You are given an integer array `nums`. Let `product` be the product of all values in the array `nums`.

Return `signFunc(product)`.

## Constraints
- `1 <= nums.length <= 1000`
- `-100 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [-1,-2,-3,-4,3,2,1]`
- **Output:** `1`
- **Explanation:** The product of all values in the array is 144, and signFunc(144) = 1

### Example 2
- **Input:** `nums = [1,5,0,2,-3]`
- **Output:** `0`
- **Explanation:** The product of all values in the array is 0, and signFunc(0) = 0

### Example 3
- **Input:** `nums = [-1,1,-1,1,-1]`
- **Output:** `-1`
- **Explanation:** The product of all values in the array is -1, and signFunc(-1) = -1

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sign of the Product of an Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-1,-2,-3,-4,3,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The product of all values in the array is 144, and signFunc(144) = 1

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
    int arraySign(vector<int>& nums) {
        int negativeCount = 0;

        for (int num : nums) {
            if (num == 0) {
                return 0;
            }

            if (num < 0) {
                negativeCount++;
            }
        }

        if (negativeCount % 2 == 0) {
            return 1;
        }

        return -1;
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
- [238. Product of Array Except Self](../../0001-0500/0238-product-of-array-except-self/)
- [1464. Maximum Product of Two Elements in an Array](../../1001-1500/1464-maximum-product-of-two-elements-in-an-array/)
- [1735. Count Ways to Make Array With Product](../../1501-2000/1735-count-ways-to-make-array-with-product/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sign-of-the-product-of-an-array/)
