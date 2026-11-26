# LeetCode 2121: Intervals Between Identical Elements

**LeetCode Problem #2121 — Intervals Between Identical Elements**
Solve LeetCode Intervals Between Identical Elements using JavaScript and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Intervals Between Identical Elements |
| LeetCode | #2121 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array of `n` integers `arr`.

The **interval** between two elements in `arr` is defined as the **absolute difference** between their indices. More formally, the **interval** between `arr[i]` and `arr[j]` is `|i - j|`.

Return *an array* `intervals` *of length* `n` *where* `intervals[i]` *is **the sum of intervals** between *`arr[i]`* and each element in *`arr`* with the same value as *`arr[i]`*.*

**Note:** `|x|` is the absolute value of `x`.

## Constraints
- `n == arr.length`
- `1 <= n <= 10^5`
- `1 <= arr[i] <= 10^5`

## Examples
### Example 1
- **Input:** `arr = [2,1,3,1,2,3,3]`
- **Output:** `[4,2,7,2,4,4,5]`
- **Explanation:** - Index 0: Another 2 is found at index 4. |0 - 4| = 4
- Index 1: Another 1 is found at index 3. |1 - 3| = 2
- Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
- Index 3: Another 1 is found at index 1. |3 - 1| = 2
- Index 4: Another 2 is found at index 0. |4 - 0| = 4
- Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
- Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5

### Example 2
- **Input:** `arr = [10,5,10,10]`
- **Output:** `[5,0,3,4]`
- **Explanation:** - Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5
- Index 1: There is only one 5 in the array, so its sum of intervals to identical elements is 0.
- Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3
- Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Intervals Between Identical Elements**, we observe the problem requirements and utilize the **Greedy** technique. By maintaining a **Array / Priority Queue**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array / Priority Queue** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [2,1,3,1,2,3,3]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,2,7,2,4,4,5]`.
4. **Verification:** - Index 0: Another 2 is found at index 4. |0 - 4| = 4
- Index 1: Another 1 is found at index 3. |1 - 3| = 2
- Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
- Index 3: Another 1 is found at index 1. |3 - 1| = 2
- Index 4: Another 2 is found at index 0. |4 - 0| = 4
- Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
- Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var getDistances = function(arr) {
    const map = new Map();
    const result = new Array(arr.length).fill(0);
    for (let i = 0; i < arr.length; i++) {
        if (!map.has(arr[i])) {
            map.set(arr[i], []);
        }
        map.get(arr[i]).push(i);
    }
    for (const indices of map.values()) {
        const m = indices.length;
        let totalSum = indices.reduce((sum, x) => sum + x, 0);
        let prefixSum = 0;
        for (let j = 0; j < m; j++) {
            const index = indices[j];
            const leftCount = j;
            const rightCount = m - j - 1;
            const leftDistance =
                index * leftCount - prefixSum;
            const rightSum = totalSum - prefixSum - index;
            const rightDistance =
                rightSum - index * rightCount;
            result[index] = leftDistance + rightDistance;
            prefixSum += index;
        }
    }
    return result;
};
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1981. Minimize the Difference Between Target and Chosen Elements](../../1501-2000/1981-minimize-the-difference-between-target-and-chosen-elements/)
- [2817. Minimum Absolute Difference Between Elements With Constraint](../../2501-3000/2817-minimum-absolute-difference-between-elements-with-constraint/)
- [3398. Smallest Substring With Identical Characters I](../../3001-3500/3398-smallest-substring-with-identical-characters-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/intervals-between-identical-elements/)
