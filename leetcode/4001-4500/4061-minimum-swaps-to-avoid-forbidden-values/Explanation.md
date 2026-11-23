# LeetCode 3785: Minimum Swaps to Avoid Forbidden Values

**LeetCode Problem #3785 — Minimum Swaps to Avoid Forbidden Values**
Solve LeetCode Minimum Swaps to Avoid Forbidden Values using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Swaps to Avoid Forbidden Values |
| LeetCode | #3785 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integer arrays, `nums` and `forbidden`, each of length `n`.

You may perform the following operation any number of times (including zero):

Choose two **distinct** indices `i` and `j`, and swap `nums[i]` with `nums[j]`.

Return the **minimum** number of swaps required such that, for every index `i`, the value of `nums[i]` is **not equal** to `forbidden[i]`. If no amount of swaps can ensure that every index avoids its forbidden value, return -1.

## Constraints
- `1 <= n == nums.length == forbidden.length <= 10^5`
- `1 <= nums[i], forbidden[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3], forbidden = [3,2,1]`
- **Output:** `1`
- **Explanation:** One optimal set of swaps: 

 
 Select indices `i = 0` and `j = 1` in `nums` and swap them, resulting in `nums = [2, 1, 3]`. 
 After this swap, for every index `i`, `nums[i]` is not equal to `forbidden[i]`.

### Example 2
- **Input:** `nums = [4,6,6,5], forbidden = [4,6,5,5]`
- **Output:** `2`
- **Explanation:** One optimal set of swaps:

 
 Select indices `i = 0` and `j = 2` in `nums` and swap them, resulting in `nums = [6, 6, 4, 5]`. 
 Select indices `i = 1` and `j = 3` in `nums` and swap them, resulting in `nums = [6, 5, 4, 6]`. 
 After these swaps, for every index `i`, `nums[i]` is not equal to `forbidden[i]`.

### Example 3
- **Input:** `nums = [7,7], forbidden = [8,7]`
- **Output:** `-1`
- **Explanation:** It is not possible to make `nums[i]` different from `forbidden[i]` for all indices.

### Example 4
- **Input:** `nums = [1,2], forbidden = [2,1]`
- **Output:** `0`
- **Explanation:** No swaps are required because `nums[i]` is already different from `forbidden[i]` for all indices, so the answer is 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Swaps to Avoid Forbidden Values**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], forbidden = [3,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** One optimal set of swaps: 

 
 Select indices `i = 0` and `j = 1` in `nums` and swap them, resulting in `nums = [2, 1, 3]`. 
 After this swap, for every index `i`, `nums[i]` is not equal to `forbidden[i]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minSwaps = function(nums, forbidden) {
    const n = nums.length;

    const numsFreq = new Map();
    const forbiddenFreq = new Map();
    const badFreq = new Map();

    let badCount = 0;
    let maxFreq = 0;

    // Step 1: Count frequencies
    for (let i = 0; i < n; i++) {
        numsFreq.set(nums[i], (numsFreq.get(nums[i]) || 0) + 1);

        forbiddenFreq.set(
            forbidden[i],
            (forbiddenFreq.get(forbidden[i]) || 0) + 1
        );
    }

    // Step 2: Check if a valid arrangement is possible
    for (let [num, count] of numsFreq) {
        const forbiddenCount = forbiddenFreq.get(num) || 0;

        if (count + forbiddenCount > n) {
            return -1;
        }
    }

    // Step 3: Count conflicting positions
    for (let i = 0; i < n; i++) {
        if (nums[i] === forbidden[i]) {
            badCount++;

            const count = (badFreq.get(nums[i]) || 0) + 1;

            badFreq.set(nums[i], count);

            maxFreq = Math.max(maxFreq, count);
        }
    }

    // Step 4: Calculate minimum swaps
    return Math.max(maxFreq, Math.ceil(badCount / 2));
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
- [1130. Minimum Cost Tree From Leaf Values](../../1001-1500/1228-minimum-cost-tree-from-leaf-values/)
- [1247. Minimum Swaps to Make Strings Equal](../../1001-1500/1369-minimum-swaps-to-make-strings-equal/)
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/)
