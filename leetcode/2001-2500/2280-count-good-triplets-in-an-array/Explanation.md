# LeetCode 2179: Count Good Triplets in an Array

**LeetCode Problem #2179 — Count Good Triplets in an Array**
Solve LeetCode Count Good Triplets in an Array using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Good Triplets in an Array |
| LeetCode | #2179 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two **0-indexed** arrays `nums1` and `nums2` of length `n`, both of which are **permutations** of `[0, 1, ..., n - 1]`.

A **good triplet** is a set of `3` **distinct** values which are present in **increasing order** by position both in `nums1` and `nums2`. In other words, if we consider `pos1_v` as the index of the value `v` in `nums1` and `pos2_v` as the index of the value `v` in `nums2`, then a good triplet will be a set `(x, y, z)` where `0 <= x, y, z <= n - 1`, such that `pos1_x < pos1_y < pos1_z` and `pos2_x < pos2_y < pos2_z`.

Return *the **total number** of good triplets*.

## Constraints
- `n == nums1.length == nums2.length`
- `3 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= n - 1`
- `nums1` and `nums2` are permutations of `[0, 1, ..., n - 1]`.

## Examples
### Example 1
- **Input:** `nums1 = [2,0,1,3], nums2 = [0,1,2,3]`
- **Output:** `1`
- **Explanation:** There are 4 triplets (x,y,z) such that pos1_x < pos1_y < pos1_z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
Out of those triplets, only the triplet (0,1,3) satisfies pos2_x < pos2_y < pos2_z. Hence, there is only 1 good triplet.

### Example 2
- **Input:** `nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]`
- **Output:** `4`
- **Explanation:** The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Good Triplets in an Array**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [2,0,1,3], nums2 = [0,1,2,3]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There are 4 triplets (x,y,z) such that pos1_x < pos1_y < pos1_z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
Out of those triplets, only the triplet (0,1,3) satisfies pos2_x < pos2_y < pos2_z. Hence, there is only 1 good triplet.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var goodTriplets = function(nums1, nums2) {
    const n = nums1.length;

    // Map each value to its position in nums2
    const pos = new Array(n);

    for (let i = 0; i < n; i++) {
        pos[nums2[i]] = i;
    }

    // Convert nums1 into positions in nums2
    const arr = nums1.map(value => pos[value]);

    // Fenwick Tree
    const bit = new Array(n + 1).fill(0);

    function update(index, value) {
        index++; // Convert to 1-based indexing

        while (index <= n) {
            bit[index] += value;
            index += index & -index;
        }
    }

    function query(index) {
        let sum = 0;
        index++; // Inclusive prefix sum

        while (index > 0) {
            sum += bit[index];
            index -= index & -index;
        }

        return sum;
    }

    let result = 0;

    for (let j = 0; j < n; j++) {
        // Number of earlier positions smaller than arr[j]
        const left = query(arr[j] - 1);

        // Number of later positions greater than arr[j]
        const right = (n - 1 - arr[j]) -
                      (j - left);

        result += left * right;

        // Insert current position for future elements
        update(arr[j], 1);
    }

    return result;
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1534. Count Good Triplets](../../1501-2000/1656-count-good-triplets/)
- [1250. Check If It Is a Good Array](../../1001-1500/1372-check-if-it-is-a-good-array/)
- [1735. Count Ways to Make Array With Product](../../1501-2000/1836-count-ways-to-make-array-with-product/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-good-triplets-in-an-array/)
