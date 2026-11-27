# LeetCode 2363: Merge Similar Items

**LeetCode Problem #2363 — Merge Similar Items**
Solve LeetCode Merge Similar Items using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Merge Similar Items |
| LeetCode | #2363 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two 2D integer arrays, `items1` and `items2`, representing two sets of items. Each array `items` has the following properties:

`items[i] = [value_i, weight_i]` where `value_i` represents the **value** and `weight_i` represents the **weight **of the `i^th` item. 
 The value of each item in `items` is **unique**.

Return *a 2D integer array* `ret` *where* `ret[i] = [value_i, weight_i]`*,* *with* `weight_i` *being the **sum of weights** of all items with value* `value_i`.

**Note:** `ret` should be returned in **ascending** order by value.

## Constraints
- `1 <= items1.length, items2.length <= 1000`
- `items1[i].length == items2[i].length == 2`
- `1 <= value_i, weight_i <= 1000`
- Each `value_i` in `items1` is **unique**.
- Each `value_i` in `items2` is **unique**.

## Examples
### Example 1
- **Input:** `items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]`
- **Output:** `[[1,6],[3,9],[4,5]]`
- **Explanation:** The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
The item with value = 4 occurs in items1 with weight = 5, total weight = 5. 
Therefore, we return [[1,6],[3,9],[4,5]].

### Example 2
- **Input:** `items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]`
- **Output:** `[[1,4],[2,4],[3,4]]`
- **Explanation:** The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 3, total weight = 1 + 3 = 4.
The item with value = 2 occurs in items1 with weight = 3 and in items2 with weight = 1, total weight = 3 + 1 = 4.
The item with value = 3 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
Therefore, we return [[1,4],[2,4],[3,4]].

### Example 3
- **Input:** `items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]`
- **Output:** `[[1,7],[2,4],[7,1]]`
- **Explanation:** The item with value = 1 occurs in items1 with weight = 3 and in items2 with weight = 4, total weight = 3 + 4 = 7. 
The item with value = 2 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4. 
The item with value = 7 occurs in items2 with weight = 1, total weight = 1.
Therefore, we return [[1,7],[2,4],[7,1]].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Merge Similar Items**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,6],[3,9],[4,5]]`.
4. **Verification:** The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
The item with value = 4 occurs in items1 with weight = 5, total weight = 5. 
Therefore, we return [[1,6],[3,9],[4,5]].

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
var mergeSimilarItems = function(items1, items2) {
    const map = new Map();
    for (const [value, weight] of items1) {
        map.set(value, (map.get(value) || 0) + weight);
    }
    for (const [value, weight] of items2) {
        map.set(value, (map.get(value) || 0) + weight);
    }
    const result = Array.from(map.entries());

    result.sort((a, b) => a[0] - b[0]);

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
- [21. Merge Two Sorted Lists](../../0001-0500/0021-merge-two-sorted-lists/)
- [23. Merge k Sorted Lists](../../0001-0500/0023-merge-k-sorted-lists/)
- [56. Merge Intervals](../../0001-0500/0056-merge-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/merge-similar-items/)
