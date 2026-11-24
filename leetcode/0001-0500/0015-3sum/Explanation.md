# LeetCode 15: 3Sum

**LeetCode Problem #15 — 3Sum**
Solve LeetCode 3Sum using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | 3Sum |
| LeetCode | #15 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

## Constraints
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [-1,0,1,2,-1,-4]`
- **Output:** `[[-1,-1,2],[-1,0,1]]`
- **Explanation:** nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

### Example 2
- **Input:** `nums = [0,1,1]`
- **Output:** `[]`
- **Explanation:** The only possible triplet does not sum up to 0.

### Example 3
- **Input:** `nums = [0,0,0]`
- **Output:** `[[0,0,0]]`
- **Explanation:** The only possible triplet sums up to 0.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses **Sorting + Two Pointers** to efficiently find all unique triplets in $O(N^2)$ time.

1. **Sort the Array:** Sorting enables the two-pointer technique and makes it easy to skip duplicate values.
2. **Fix One Element:** It iterates through the array with index `i`, fixing `nums[i]` as the first element of the triplet.
   - If `nums[i] > 0`, the loop breaks early because three positive numbers can never sum to zero.
   - If `nums[i]` equals the previous element (`nums[i - 1]`), it skips to avoid duplicate triplets.
3. **Two Pointers for the Remaining Two:** For each fixed `nums[i]`, it uses two pointers: `left = i + 1` and `right = nums.length - 1`.
   - It calculates `sum = nums[i] + nums[left] + nums[right]`.
   - If `sum === 0`, the triplet is added to the result. Then both pointers are moved inward, skipping over any duplicate values.
   - If `sum < 0`, `left` is incremented to increase the sum.
   - If `sum > 0`, `right` is decremented to decrease the sum.
4. The result contains all unique triplets.

Time complexity is $O(N^2)$ and space complexity is $O(\log N)$ for sorting (ignoring output).

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [-1,0,1,2,-1,-4]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[-1,-1,2],[-1,0,1]]`.
4. **Verification:** nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var threeSum = function(nums) {
    nums.sort((a, b) => a - b);

    const result = [];
    const n = nums.length;

    for (let i = 0; i < n - 2; i++) {
        // Skip duplicate first elements
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        // Since the array is sorted, no later triplet can sum to zero
        if (nums[i] > 0) {
            break;
        }

        let left = i + 1;
        let right = n - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];

            if (sum === 0) {
                result.push([nums[i], nums[left], nums[right]]);

                left++;
                right--;

                // Skip duplicate second elements
                while (left < right && nums[left] === nums[left - 1]) {
                    left++;
                }

                // Skip duplicate third elements
                while (left < right && nums[right] === nums[right + 1]) {
                    right--;
                }
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    return result;
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
- [16. 3Sum Closest](../../0001-0500/0016-3sum-closest/)
- [923. 3Sum With Multiplicity](../../0501-1000/0923-3sum-with-multiplicity/)
- [4. Median of Two Sorted Arrays](../../0001-0500/0004-median-of-two-sorted-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/3sum/)
