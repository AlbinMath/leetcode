# LeetCode 2780: Minimum Index of a Valid Split

**LeetCode Problem #2780 — Minimum Index of a Valid Split**
Solve LeetCode Minimum Index of a Valid Split using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Index of a Valid Split |
| LeetCode | #2780 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
An element `x` of an integer array `arr` of length `m` is **dominant** if **more than half** the elements of `arr` have a value of `x`.

You are given a **0-indexed** integer array `nums` of length `n` with one **dominant** element.

You can split `nums` at an index `i` into two arrays `nums[0, ..., i]` and `nums[i + 1, ..., n - 1]`, but the split is only **valid** if:

`0 <= i < n - 1` 
 `nums[0, ..., i]`, and `nums[i + 1, ..., n - 1]` have the same dominant element.

Here, `nums[i, ..., j]` denotes the subarray of `nums` starting at index `i` and ending at index `j`, both ends being inclusive. Particularly, if `j < i` then `nums[i, ..., j]` denotes an empty subarray.

Return *the **minimum** index of a **valid split***. If no valid split exists, return `-1`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `nums` has exactly one dominant element.

## Examples
### Example 1
- **Input:** `nums = [1,2,2,2]`
- **Output:** `2`
- **Explanation:** We can split the array at index 2 to obtain arrays [1,2,2] and [2]. 
In array [1,2,2], element 2 is dominant since it occurs twice in the array and 2 * 2 > 3. 
In array [2], element 2 is dominant since it occurs once in the array and 1 * 2 > 1.
Both [1,2,2] and [2] have the same dominant element as nums, so this is a valid split. 
It can be shown that index 2 is the minimum index of a valid split.

### Example 2
- **Input:** `nums = [2,1,3,1,1,1,7,1,2,1]`
- **Output:** `4`
- **Explanation:** We can split the array at index 4 to obtain arrays [2,1,3,1,1] and [1,7,1,2,1].
In array [2,1,3,1,1], element 1 is dominant since it occurs thrice in the array and 3 * 2 > 5.
In array [1,7,1,2,1], element 1 is dominant since it occurs thrice in the array and 3 * 2 > 5.
Both [2,1,3,1,1] and [1,7,1,2,1] have the same dominant element as nums, so this is a valid split.
It can be shown that index 4 is the minimum index of a valid split.

### Example 3
- **Input:** `nums = [3,3,3,3,7,2,2]`
- **Output:** `-1`
- **Explanation:** It can be shown that there is no valid split.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Minimum Index of a Valid Split**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,2]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can split the array at index 2 to obtain arrays [1,2,2] and [2]. 
In array [1,2,2], element 2 is dominant since it occurs twice in the array and 2 * 2 > 3. 
In array [2], element 2 is dominant since it occurs once in the array and 1 * 2 > 1.
Both [1,2,2] and [2] have the same dominant element as nums, so this is a valid split. 
It can be shown that index 2 is the minimum index of a valid split.

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
var minimumIndex = function(nums) {
    const n = nums.length;
    const freq = new Map();

    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    let dominant = -1;
    let totalCount = 0;

    for (const [num, count] of freq) {
        if (count * 2 > n) {
            dominant = num;
            totalCount = count;
            break;
        }
    }

    let leftCount = 0;

    for (let i = 0; i < n - 1; i++) {
        if (nums[i] === dominant) {
            leftCount++;
        }

        const leftLength = i + 1;
        const rightLength = n - leftLength;
        const rightCount = totalCount - leftCount;

        if (
            leftCount * 2 > leftLength &&
            rightCount * 2 > rightLength
        ) {
            return i;
        }
    }

    return -1;
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
- [921. Minimum Add to Make Parentheses Valid](../../0501-1000/0921-minimum-add-to-make-parentheses-valid/)
- [1249. Minimum Remove to Make Valid Parentheses](../../1001-1500/1249-minimum-remove-to-make-valid-parentheses/)
- [1368. Minimum Cost to Make at Least One Valid Path in a Grid](../../1001-1500/1368-minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-index-of-a-valid-split/)
