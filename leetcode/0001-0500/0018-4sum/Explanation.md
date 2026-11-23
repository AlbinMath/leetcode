# LeetCode 18: 4Sum

**LeetCode Problem #18 — 4Sum**
Solve LeetCode 4Sum using C++ and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | 4Sum |
| LeetCode | #18 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array `nums` of `n` integers, return *an array of all the **unique** quadruplets* `[nums[a], nums[b], nums[c], nums[d]]` such that:

`0 <= a, b, c, d < n` 
 `a`, `b`, `c`, and `d` are **distinct**. 
 `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in **any order**.

## Constraints
- `1 <= nums.length <= 200`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,0,-1,0,-2,2], target = 0`
- **Output:** `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

### Example 2
- **Input:** `nums = [2,2,2,2,2], target = 8`
- **Output:** `[[2,2,2,2]]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code extends the 3Sum approach by adding one more loop, using **Sorting + Two Nested Loops + Two Pointers** for an $O(N^3)$ solution.

1. **Sort the Array:** The array is sorted to enable the two-pointer technique and duplicate skipping.
2. **First Loop (`i`):** Fixes the first element. Skips duplicates by checking `nums[i] == nums[i - 1]`.
3. **Second Loop (`j`):** Fixes the second element starting from `i + 1`. Also skips duplicates.
4. **Two Pointers (`left`, `right`):** For each pair `(i, j)`, two pointers search for the remaining two elements.
   - The sum is computed using `long long` to avoid integer overflow.
   - If `sum == target`, the quadruplet is added and both pointers move inward, skipping duplicates.
   - If `sum < target`, `left` is incremented.
   - If `sum > target`, `right` is decremented.

The time complexity is $O(N^3)$ and space complexity is $O(\log N)$ for sorting.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,0,-1,0,-2,2], target = 0`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`.

## Complexity Analysis
- **Time Complexity:** O(log n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;
                int left = j + 1;
                int right = n - 1;
                while (left < right) {
                    long long sum = (long long)nums[i] +
                                    nums[j] +
                                    nums[left] +
                                    nums[right];
                    if (sum == target) {
                        ans.push_back({
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        });
                        while (left < right && nums[left] == nums[left + 1])
                            left++;

                        while (left < right && nums[right] == nums[right - 1])
                            right--;
                        left++;
                        right--;
                    }
                    else if (sum < target) {
                        left++;
                    }
                    else {
                        right--;
                    }
                }
            }
        }
        return ans;
    }
};
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [4. Median of Two Sorted Arrays](../../0001-0500/0004-median-of-two-sorted-arrays/)
- [15. 3Sum](../../0001-0500/0015-3sum/)
- [16. 3Sum Closest](../../0001-0500/0016-3sum-closest/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/4sum/)
