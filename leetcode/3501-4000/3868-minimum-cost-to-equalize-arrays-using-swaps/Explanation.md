# LeetCode 3868: Minimum Cost to Equalize Arrays Using Swaps

**LeetCode Problem #3868 — Minimum Cost to Equalize Arrays Using Swaps**
Solve LeetCode Minimum Cost to Equalize Arrays Using Swaps using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Equalize Arrays Using Swaps |
| LeetCode | #3868 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays `nums1` and `nums2` of size `n`.

You can perform the following two operations any number of times on these two arrays:

**Swap within the same array**: Choose two indices `i` and `j`. Then, choose either to swap `nums1[i]` and `nums1[j]`, or `nums2[i]` and `nums2[j]`. This operation is **free of charge**. 
 **Swap between two arrays**: Choose an index `i`. Then, swap `nums1[i]` and `nums2[i]`. This operation **incurs a cost of 1**.

Return an integer denoting the **minimum cost** to make `nums1` and `nums2` **identical**. If this is not possible, return -1.

## Constraints
- `2 <= n == nums1.length == nums2.length <= 8 * 10^4`
- `1 <= nums1[i], nums2[i] <= 8 * 10^4`

## Examples
### Example 1
- **Input:** `nums1 = [10,20], nums2 = [20,10]`
- **Output:** `0`
- **Explanation:** Swap `nums2[0] = 20` and `nums2[1] = 10`.

 
 `nums2` becomes `[10, 20]`. 
 This operation is free of charge. 
 
 
 `nums1` and `nums2` are now identical. The cost is 0.

### Example 2
- **Input:** `nums1 = [10,10], nums2 = [20,20]`
- **Output:** `1`
- **Explanation:** Swap `nums1[0] = 10` and `nums2[0] = 20`.

 
 `nums1` becomes `[20, 10]`. 
 `nums2` becomes `[10, 20]`. 
 This operation costs 1. 
 
 
 Swap `nums2[0] = 10` and `nums2[1] = 20`.
 
 `nums2` becomes `[20, 10]`. 
 This operation is free of charge. 
 
 
 `nums1` and `nums2` are now identical. The cost is 1.

### Example 3
- **Input:** `nums1 = [10,20], nums2 = [30,40]`
- **Output:** `-1`
- **Explanation:** It is impossible to make the two arrays identical. Therefore, the answer is -1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Cost to Equalize Arrays Using Swaps**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [10,20], nums2 = [20,10]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `0`.
4. **Verification:** Swap `nums2[0] = 20` and `nums2[1] = 10`.

 
 `nums2` becomes `[10, 20]`. 
 This operation is free of charge. 
 
 
 `nums1` and `nums2` are now identical. The cost is 0.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minCost = function(nums1, nums2) {
    const MAX = 80000;
    const count1 = new Array(MAX + 1).fill(0);
    const count2 = new Array(MAX + 1).fill(0);

    // Count frequencies in both arrays
    for (let x of nums1) {
        count1[x]++;
    }

    for (let x of nums2) {
        count2[x]++;
    }

    let answer = 0;

    for (let x = 1; x <= MAX; x++) {
        const total = count1[x] + count2[x];

        // Every number must have an even total frequency
        if (total % 2 !== 0) {
            return -1;
        }

        // Count excess elements in nums1
        const target = total / 2;

        if (count1[x] > target) {
            answer += count1[x] - target;
        }
    }

    return answer;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [2499. Minimum Total Cost to Make Arrays Unequal](../../2001-2500/2499-minimum-total-cost-to-make-arrays-unequal/)
- [3139. Minimum Cost to Equalize Array](../../3001-3500/3139-minimum-cost-to-equalize-array/)
- [1320. Minimum Distance to Type a Word Using Two Fingers](../../1001-1500/1320-minimum-distance-to-type-a-word-using-two-fingers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/)
