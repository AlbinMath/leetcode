# LeetCode 1424: Diagonal Traverse II

**LeetCode Problem #1424 — Diagonal Traverse II**
Solve LeetCode Diagonal Traverse II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Diagonal Traverse II |
| LeetCode | #1424 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a 2D integer array `nums`, return *all elements of *`nums`* in diagonal order as shown in the below images*.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i].length <= 10^5`
- `1 <= sum(nums[i].length) <= 10^5`
- `1 <= nums[i][j] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [[1,2,3],[4,5,6],[7,8,9]]`
- **Output:** `[1,4,2,7,5,3,8,6,9]`

### Example 2
- **Input:** `nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]`
- **Output:** `[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Diagonal Traverse II**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [[1,2,3],[4,5,6],[7,8,9]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,4,2,7,5,3,8,6,9]`.

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
var findDiagonalOrder = function(nums) {
    const map = new Map();
    let maxKey = 0;

    // Group elements by diagonal
    for (let r = 0; r < nums.length; r++) {
        for (let c = 0; c < nums[r].length; c++) {
            const key = r + c;

            if (!map.has(key)) {
                map.set(key, []);
            }

            map.get(key).push(nums[r][c]);
            maxKey = Math.max(maxKey, key);
        }
    }

    const result = [];

    for (let key = 0; key <= maxKey; key++) {
        const diagonal = map.get(key);

        for (let i = diagonal.length - 1; i >= 0; i--) {
            result.push(diagonal[i]);
        }
    }

    return result;
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
- [498. Diagonal Traverse](../../0001-0500/0498-diagonal-traverse/)
- [1572. Matrix Diagonal Sum](../../1501-2000/1572-matrix-diagonal-sum/)
- [2614. Prime In Diagonal](../../2501-3000/2614-prime-in-diagonal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/diagonal-traverse-ii/)
