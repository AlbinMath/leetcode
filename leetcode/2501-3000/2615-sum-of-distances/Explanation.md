# LeetCode 2615: Sum of Distances

**LeetCode Problem #2615 — Sum of Distances**
Solve LeetCode Sum of Distances using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sum of Distances |
| LeetCode | #2615 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums`.

There exists an array `arr` of length `nums.length`, where `arr[i]` is the sum of `|i - j|` over all `j` such that `nums[j] == nums[i]` and `j != i`. If there is no such `j`, set `arr[i]` to be 0.

Return the array `arr`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,3,1,1,2]`
- **Output:** `[5,0,3,4,0]`
- **Explanation:** When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2.

### Example 2
- **Input:** `nums = [0,5,3]`
- **Output:** `[0,0,0]`
- **Explanation:** Since each element in nums is distinct, arr[i] = 0 for all i.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Sum of Distances**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,1,1,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,0,3,4,0]`.
4. **Verification:** When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2.

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
var distance = function(nums) {
    const n = nums.length;
    let map = new Map();
    for (let i = 0; i < n; i++) {
        if (!map.has(nums[i])) {
            map.set(nums[i], []);
        }
        map.get(nums[i]).push(i);
    }
    let result = new Array(n).fill(0);
    for (let indices of map.values()) {
        const m = indices.length;
        let prefix = new Array(m + 1).fill(0);

        for (let j = 0; j < m; j++) {
            prefix[j + 1] = prefix[j] + indices[j];
        }

        const totalSum = prefix[m];
        for (let j = 0; j < m; j++) {
            let pos = indices[j];
            let left = j * pos - prefix[j];
            let right =
                (totalSum - prefix[j + 1]) -
                (m - j - 1) * pos;

            result[pos] = left + right;
        }
    }
    return result;
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
- [834. Sum of Distances in Tree](../../0501-1000/0834-sum-of-distances-in-tree/)
- [1. Two Sum](../../0001-0500/0001-two-sum/)
- [39. Combination Sum](../../0001-0500/0039-combination-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sum-of-distances/)
