# LeetCode 1863: Sum of All Subset XOR Totals

**LeetCode Problem #1863 — Sum of All Subset XOR Totals**
Solve LeetCode Sum of All Subset XOR Totals using C++ and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of All Subset XOR Totals |
| LeetCode | #1863 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **XOR total** of an array is defined as the bitwise `XOR` of** all its elements**, or `0` if the array is** empty**.

For example, the **XOR total** of the array `[2,5,6]` is `2 XOR 5 XOR 6 = 1`.

Given an array `nums`, return *the **sum** of all **XOR totals** for every **subset** of *`nums`.

**Note:** Subsets with the **same** elements should be counted **multiple** times.

An array `a` is a **subset** of an array `b` if `a` can be obtained from `b` by deleting some (possibly zero) elements of `b`.

## Constraints
- `1 <= nums.length <= 12`
- `1 <= nums[i] <= 20`

## Examples
### Example 1
- **Input:** `nums = [1,3]`
- **Output:** `6`
- **Explanation:** The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6

### Example 2
- **Input:** `nums = [5,1,6]`
- **Output:** `28`
- **Explanation:** The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

### Example 3
- **Input:** `nums = [3,4,5,6,7,8]`
- **Output:** `480`
- **Explanation:** The sum of all XOR totals for every subset is 480.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sum of All Subset XOR Totals**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3]`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int total = 0;

    void backtrack(vector<int>& nums, int index, int currentXOR) {
        if (index == nums.size()) {
            total += currentXOR;
            return;
        }

        // Include the current element
        backtrack(nums, index + 1, currentXOR ^ nums[index]);

        // Exclude the current element
        backtrack(nums, index + 1, currentXOR);
    }

    int subsetXORSum(vector<int>& nums) {
        total = 0;
        backtrack(nums, 0, 0);
        return total;
    }
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1835. Find XOR Sum of All Pairs Bitwise AND](../../1501-2000/1835-find-xor-sum-of-all-pairs-bitwise-and/)
- [1588. Sum of All Odd Length Subarrays](../../1501-2000/1588-sum-of-all-odd-length-subarrays/)
- [1781. Sum of Beauty of All Substrings](../../1501-2000/1781-sum-of-beauty-of-all-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)
