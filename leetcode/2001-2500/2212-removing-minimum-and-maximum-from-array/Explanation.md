# LeetCode 2091: Removing Minimum and Maximum From Array

**LeetCode Problem #2091 — Removing Minimum and Maximum From Array**
Solve LeetCode Removing Minimum and Maximum From Array using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Removing Minimum and Maximum From Array |
| LeetCode | #2091 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array of **distinct** integers `nums`.

There is an element in `nums` that has the **lowest** value and an element that has the **highest** value. We call them the **minimum** and **maximum** respectively. Your goal is to remove **both** these elements from the array.

A **deletion** is defined as either removing an element from the **front** of the array or removing an element from the **back** of the array.

Return the **minimum** number of deletions it would take to remove **both** the **minimum** and **maximum** element from the array.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
- The integers in `nums` are **distinct**.

## Examples
### Example 1
- **Input:** `nums = [2,`
- **Output:** `5`
- **Explanation:** The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.

### Example 2
- **Input:** `nums = [0,`
- **Output:** `3`
- **Explanation:** The minimum element in the array is nums[1], which is -4.
The maximum element in the array is nums[2], which is 19.
We can remove both the minimum and maximum by removing 3 elements from the front.
This results in only 3 deletions, which is the minimum number possible.

### Example 3
- **Input:** `nums = [`
- **Output:** `1`
- **Explanation:** There is only one element in the array, which makes it both the minimum and maximum element.
We can remove it with 1 deletion.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Find indices of the min and max. Consider three strategies: remove both from the front, both from the back, or one from each end. Return the minimum deletions among all strategies.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **In-Place Array Traversal & Index Mapping**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.

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
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();

        int minIndex = 0;
        int maxIndex = 0;

        // Find indices of minimum and maximum
        for (int i = 0; i < n; i++) {
            if (nums[i] < nums[minIndex])
                minIndex = i;

            if (nums[i] > nums[maxIndex])
                maxIndex = i;
        }

        // Make minIndex the smaller index
        if (minIndex > maxIndex)
            swap(minIndex, maxIndex);

        // 1. Remove both from the front
        int fromFront = maxIndex + 1;

        // 2. Remove both from the back
        int fromBack = n - minIndex;

        // 3. Remove min from front and max from back
        int bothSides = (minIndex + 1) + (n - maxIndex);

        return min({fromFront, fromBack, bothSides});
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
- [1717. Maximum Score From Removing Substrings](../../1501-2000/1818-maximum-score-from-removing-substrings/)
- [2975. Maximum Square Area by Removing Fences From a Field](../../3001-3500/3250-maximum-square-area-by-removing-fences-from-a-field/)
- [1707. Maximum XOR With an Element From Array](../../1501-2000/1826-maximum-xor-with-an-element-from-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/)
