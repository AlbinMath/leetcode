# LeetCode 3659: Partition Array Into K-Distinct Groups

**LeetCode Problem #3659 — Partition Array Into K-Distinct Groups**
Solve LeetCode Partition Array Into K-Distinct Groups using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array Into K-Distinct Groups |
| LeetCode | #3659 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

Your task is to determine whether it is possible to partition all elements of `nums` into one or more groups such that:

Each group contains **exactly** `k` elements. 
 All elements in each group are **distinct**. 
 Each element in `nums` must be assigned to **exactly** one group.

Return `true` if such a partition is possible, otherwise return `false`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `^​​​​​​​1 <= k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4], k = 2`
- **Output:** `true`
- **Explanation:** One possible partition is to have 2 groups: 

 
 Group 1: `[1, 2]` 
 Group 2: `[3, 4]` 
 

 Each group contains `k = 2` distinct elements, and all elements are used exactly once.

### Example 2
- **Input:** `nums = [3,5,2,2], k = 2`
- **Output:** `true`
- **Explanation:** One possible partition is to have 2 groups: 

 
 Group 1: `[2, 3]` 
 Group 2: `[2, 5]` 
 

 Each group contains `k = 2` distinct elements, and all elements are used exactly once.

### Example 3
- **Input:** `nums = [1,5,2,3], k = 3`
- **Output:** `false`
- **Explanation:** We cannot form groups of `k = 3` distinct elements using all values exactly once.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Partition Array Into K-Distinct Groups**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** One possible partition is to have 2 groups: 

 
 Group 1: `[1, 2]` 
 Group 2: `[3, 4]` 
 

 Each group contains `k = 2` distinct elements, and all elements are used exactly once.

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
var partitionArray = function(nums, k) {
    let n = nums.length;

    // Check if array can be divided into equal groups
    if (n % k !== 0) {
        return false;
    }

    let freq = new Map();
    let maxFreq = 0;

    // Count frequency of each number
    for (const num of nums) {
        let count = (freq.get(num) || 0) + 1;

        freq.set(num, count);

        maxFreq = Math.max(maxFreq, count);
    }

    // Number of groups
    let groups = n / k;

    return maxFreq <= groups;
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
- [2138. Divide a String Into Groups of Size k](../../2001-2500/2260-divide-a-string-into-groups-of-size-k/)
- [2035. Partition Array Into Two Arrays to Minimize Sum Difference](../../2001-2500/2162-partition-array-into-two-arrays-to-minimize-sum-difference/)
- [3566. Partition Array into Two Equal Product Subsets](../../3501-4000/3843-partition-array-into-two-equal-product-subsets/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-into-k-distinct-groups/)
