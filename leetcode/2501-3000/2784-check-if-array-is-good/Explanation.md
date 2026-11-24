# LeetCode 2784: Check if Array is Good

**LeetCode Problem #2784 — Check if Array is Good**
Solve LeetCode Check if Array is Good using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Array is Good |
| LeetCode | #2784 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`. We consider an array **good **if it is a permutation of an array `base[n]`.

`base[n] = [1, 2, ..., n - 1, n, n] `(in other words, it is an array of length `n + 1` which contains `1` to `n - 1 `exactly once, plus two occurrences of `n`). For example, `base[1] = [1, 1]` and` base[3] = [1, 2, 3, 3]`.

Return `true` *if the given array is good, otherwise return** *`false`.

**Note: **A permutation of integers represents an arrangement of these numbers.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= num[i] <= 200`

## Examples
### Example 1
- **Input:** `nums = [2, 1, 3]`
- **Output:** `false`
- **Explanation:** Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

### Example 2
- **Input:** `nums = [1, 3, 3, 2]`
- **Output:** `true`
- **Explanation:** Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. It can be seen that nums is a permutation of base[3] = [1, 2, 3, 3] (by swapping the second and fourth elements in nums, we reach base[3]). Therefore, the answer is true.

### Example 3
- **Input:** `nums = [1, 1]`
- **Output:** `true`
- **Explanation:** Since the maximum element of the array is 1, the only candidate n for which this array could be a permutation of base[n], is n = 1. It can be seen that nums is a permutation of base[1] = [1, 1]. Therefore, the answer is true.

### Example 4
- **Input:** `nums = [3, 4, 4, 1, 2, 1]`
- **Output:** `false`
- **Explanation:** Since the maximum element of the array is 4, the only candidate n for which this array could be a permutation of base[n], is n = 4. However, base[4] has five elements but array nums has six. Therefore, it can not be a permutation of base[4] = [1, 2, 3, 4, 4]. So the answer is false.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Sort the array. The maximum value should be `n = arr.length - 1`. Check that the last two elements equal `n` and elements 0 through n-2 equal 1 through n-1 respectively.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2, 1, 3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** Since the maximum element of the array is 3, the only candidate n for which this array could be a permutation of base[n], is n = 3. However, base[3] has four elements but array nums has three. Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

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
    bool isGood(vector<int>& nums) {
        int n = *max_element(nums.begin(), nums.end());

        // A good array must have n + 1 elements
        if (nums.size() != n + 1)
            return false;

        vector<int> freq(n + 1, 0);

        for (int x : nums) {
            freq[x]++;
        }

        // 1 to n-1 must appear once,
        // n must appear twice.
        for (int i = 1; i < n; i++) {
            if (freq[i] != 1)
                return false;
        }

        return freq[n] == 2;
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
- [1250. Check If It Is a Good Array](../../1001-1500/1250-check-if-it-is-a-good-array/)
- [1497. Check If Array Pairs Are Divisible by k](../../1001-1500/1497-check-if-array-pairs-are-divisible-by-k/)
- [1752. Check if Array Is Sorted and Rotated](../../1501-2000/1752-check-if-array-is-sorted-and-rotated/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-array-is-good/)
