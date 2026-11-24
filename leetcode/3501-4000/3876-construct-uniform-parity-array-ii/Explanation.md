# LeetCode 3876: Construct Uniform Parity Array II

**LeetCode Problem #3876 — Construct Uniform Parity Array II**
Solve LeetCode Construct Uniform Parity Array II using C++ and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Construct Uniform Parity Array II |
| LeetCode | #3876 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums1` of `n` **distinct** integers.

You want to construct another array `nums2` of length `n` such that the elements in `nums2` are either **all odd or all even**.

For each index `i`, you must choose **exactly one** of the following (in any order):

`nums2[i] = nums1[i]`​​​​​​​ 
 `nums2[i] = nums1[i] - nums1[j]`, for an index `j != i`, such that `nums1[i] - nums1[j] >= 1`

Return `true` if it is possible to construct such an array, otherwise return `false`.

## Constraints
- `1 <= n == nums1.length <= 10^5`
- `1 <= nums1[i] <= 10^9`
- `nums1` consists of distinct integers.

## Examples
### Example 1
- **Input:** `nums1 = [1,4,7]`
- **Output:** `true`
- **Explanation:** ​​​​​​​​​​​​​​ 

 
 Set `nums2[0] = nums1[0] = 1`. 
 Set `nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3`. 
 Set `nums2[2] = nums1[2] = 7`. 
 `nums2 = [1, 3, 7]`, and all elements are odd. Thus, the answer is `true`.

### Example 2
- **Input:** `nums1 = [2,3]`
- **Output:** `false`
- **Explanation:** It is not possible to construct `nums2` such that all elements have the same parity. Thus, the answer is `false`.

### Example 3
- **Input:** `nums1 = [4,6]`
- **Output:** `true`
- **Explanation:** Set `nums2[0] = nums1[0] = 4`. 
 Set `nums2[1] = nums1[1] = 6`. 
 `nums2 = [4, 6]`, and all elements are even. Thus, the answer is `true`.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Construct Uniform Parity Array II**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,4,7]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** ​​​​​​​​​​​​​​ 

 
 Set `nums2[0] = nums1[0] = 1`. 
 Set `nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3`. 
 Set `nums2[2] = nums1[2] = 7`. 
 `nums2 = [1, 3, 7]`, and all elements are odd. Thus, the answer is `true`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int minOdd = INT_MAX;

        // Find the smallest odd number
        for (int x : nums1) {
            if (x % 2 == 1) {
                minOdd = min(minOdd, x);
            }
        }

        // If all numbers are even, already uniform
        if (minOdd == INT_MAX) {
            return true;
        }

        // Every even number must be larger than the smallest odd
        for (int x : nums1) {
            if (x % 2 == 0 && x <= minOdd) {
                return false;
            }
        }

        return true;
    }
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3875. Construct Uniform Parity Array I](../../3501-4000/3875-construct-uniform-parity-array-i/)
- [905. Sort Array By Parity](../../0501-1000/0905-sort-array-by-parity/)
- [922. Sort Array By Parity II](../../0501-1000/0922-sort-array-by-parity-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/construct-uniform-parity-array-ii/)
