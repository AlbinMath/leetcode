# LeetCode 2295: Replace Elements in an Array

**LeetCode Problem #2295 — Replace Elements in an Array**
Solve LeetCode Replace Elements in an Array using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Replace Elements in an Array |
| LeetCode | #2295 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array `nums` that consists of `n` **distinct** positive integers. Apply `m` operations to this array, where in the `i^th` operation you replace the number `operations[i][0]` with `operations[i][1]`.

It is guaranteed that in the `i^th` operation:

`operations[i][0]` **exists** in `nums`. 
 `operations[i][1]` does **not** exist in `nums`.

Return *the array obtained after applying all the operations*.

## Constraints
- `n == nums.length`
- `m == operations.length`
- `1 <= n, m <= 10^5`
- All the values of `nums` are **distinct**.
- `operations[i].length == 2`
- `1 <= nums[i], operations[i][0], operations[i][1] <= 10^6`
- `operations[i][0]` will exist in `nums` when applying the `i^th` operation.
- `operations[i][1]` will not exist in `nums` when applying the `i^th` operation.

## Examples
### Example 1
- **Input:** `nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]`
- **Output:** `[3,2,7,1]`
- **Explanation:** We perform the following operations on nums:
- Replace the number 1 with 3. nums becomes [

### Example 2
- **Input:** `nums = [1,2], operations = [[1,3],[2,1],[3,2]]`
- **Output:** `[2,1]`
- **Explanation:** We perform the following operations to nums:
- Replace the number 1 with 3. nums becomes [

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Replace Elements in an Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,2,7,1]`.
4. **Verification:** We perform the following operations on nums:
- Replace the number 1 with 3. nums becomes [

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
var arrayChange = function(nums, operations) {
    // Map each distinct value to its current index in nums
    const pos = new Map();
    for (let i = 0; i < nums.length; i++) {
        pos.set(nums[i], i);
    }

    for (const [oldVal, newVal] of operations) {
        const idx = pos.get(oldVal);
        pos.delete(oldVal);
        nums[idx] = newVal;
        pos.set(newVal, idx);
    }

    return nums;
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
- [1299. Replace Elements with Greatest Element on Right Side](../../1001-1500/1231-replace-elements-with-greatest-element-on-right-side/)
- [2197. Replace Non-Coprime Numbers in Array](../../2001-2500/2307-replace-non-coprime-numbers-in-array/)
- [453. Minimum Moves to Equal Array Elements](../../0001-0500/0453-minimum-moves-to-equal-array-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/replace-elements-in-an-array/)
