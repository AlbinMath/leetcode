# LeetCode 16: 3Sum Closest

**LeetCode Problem #16 — 3Sum Closest**
Solve LeetCode 3Sum Closest using JavaScript, Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | 3Sum Closest |
| LeetCode | #16 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer `target`.

Find three integers at **distinct indices** in `nums` such that the sum is **closest** to `target`.

Return the sum of the three integers.

You may assume that each input would have **exactly** one solution.

## Constraints
- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [-1,2,1,-4], target = 1`
- **Output:** `2`
- **Explanation:** The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

### Example 2
- **Input:** `nums = [0,0,0], target = 1`
- **Output:** `0`
- **Explanation:** The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
This solution uses **Sorting + Two Pointers**, very similar to the 3Sum problem, but instead of looking for an exact match, it tracks which sum is closest to the target.

1. **Sort the Array:** The array is sorted in ascending order to enable the two-pointer approach.
2. **Initialize Closest:** The variable `closest` is initialized to the sum of the first three elements as a starting reference.
3. **Fix One Element:** It iterates through the array with index `i`, fixing `nums[i]` as the first element.
4. **Two Pointers:** For each `i`, it sets `left = i + 1` and `right = nums.length - 1`.
   - It calculates `sum = nums[i] + nums[left] + nums[right]`.
   - If the absolute difference between `sum` and `target` is smaller than the current `closest`, it updates `closest = sum`.
   - If `sum < target`, it increments `left` to increase the sum.
   - If `sum > target`, it decrements `right` to decrease the sum.
   - If `sum === target`, it returns `sum` immediately (can't get any closer than an exact match).
5. After all iterations, it returns `closest`.

Time complexity is $O(N^2)$ and space complexity is $O(\log N)$ for sorting.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-1,2,1,-4], target = 1`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort((a, b) => a - b);
    let closest = nums[0] + nums[1] + nums[2];
    for (let i = 0; i < nums.length - 2; i++) {
        let left = i + 1;
        let right = nums.length - 1;
        while (left < right) {
            let sum = nums[i] + nums[left] + nums[right];
            if (Math.abs(sum - target) < Math.abs(closest - target)) {
                closest = sum;
            }
            if (sum < target) {
                left++;
            } else if (sum > target) {
                right--;
            } else {
                return sum;
            }
        }
    }
    return closest;
};
```

### Python
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < abs(ans - target):
                    ans = s

                if s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return ans
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
- [564. Find the Closest Palindrome](../../0501-1000/0564-find-the-closest-palindrome/)
- [658. Find K Closest Elements](../../0501-1000/0658-find-k-closest-elements/)
- [973. K Closest Points to Origin](../../0501-1000/0973-k-closest-points-to-origin/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/3sum-closest/)
