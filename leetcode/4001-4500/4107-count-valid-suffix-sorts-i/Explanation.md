# LeetCode 4107: Count Valid Suffix Sorts I

**LeetCode Problem #4107 — Count Valid Suffix Sorts I**
Solve LeetCode Count Valid Suffix Sorts I using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Valid Suffix Sorts I |
| LeetCode | #4107 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays `nums` and `target`, both of length `n`.

For each index `i`, consider sorting the **suffix** `nums[i..n - 1]` of the original array in **non-increasing order**.

Return the number of indices `i` for which the resulting array is equal to `target`.

A **suffix** of an array is a subarray that begins at any index and extends to the end of the array.

## Constraints
- `1 <= n == nums.length == target.length <= 10^5`
- `1 <= nums[i], target[i] <= 10^​​​​​​​5`​​​​​​​​​​​​​​

## Examples
### Example 1
- **Input:** `nums = [1,2,3], target = [3,2,1]`
- **Output:** `1`
- **Explanation:** `i = 0`: The resulting array is `[3, 2, 1]`, which equals `target`. 
 `i = 1`: The resulting array is `[1, 3, 2]`. 
 `i = 2`: The resulting array is `[1, 2, 3]`. 
 

 Only `i = 0` is valid, so the answer is 1.

### Example 2
- **Input:** `nums = [1,5,6,4,6], target = [1,5,6,6,4]`
- **Output:** `2`
- **Explanation:** Choosing either `i = 2` or `i = 3` results in `[1, 5, 6, 6, 4]`. No other index produces `target`. Therefore, the answer is 2.

### Example 3
- **Input:** `nums = [7,6,8], target = [8,6,7]`
- **Output:** `0`
- **Explanation:** Sorting the suffix starting at indices 0, 1, and 2 produces `[8, 7, 6]`, `[7, 8, 6]`, and `[7, 6, 8]`, respectively. None equals `target`, so the answer is 0.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Valid Suffix Sorts I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3], target = [3,2,1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** `i = 0`: The resulting array is `[3, 2, 1]`, which equals `target`. 
 `i = 1`: The resulting array is `[1, 3, 2]`. 
 `i = 2`: The resulting array is `[1, 2, 3]`. 
 

 Only `i = 0` is valid, so the answer is 1.

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
var countSuffix = function(nums, target) {
    let n = nums.length;

    let freq = new Int32Array(100001);
    let nonZero = 0;

    // Calculate frequency differences
    for (let i = 0; i < n; i++) {
        freq[nums[i]]++;
        freq[target[i]]--;
    }

    for (let i = 1; i <= 100000; i++) {
        if (freq[i] !== 0) {
            nonZero++;
        }
    }

    // Check non-increasing target suffixes
    let sorted = new Array(n).fill(true);

    for (let i = n - 2; i >= 0; i--) {
        sorted[i] = sorted[i + 1] &&
                    target[i] >= target[i + 1];
    }

    let ans = 0;
    let prefixMatch = true;

    for (let i = 0; i < n; i++) {

        if (prefixMatch && nonZero === 0 && sorted[i]) {
            ans++;
        }

        let a = nums[i];
        let b = target[i];

        if (freq[a] !== 0) nonZero--;
        freq[a]--;
        if (freq[a] !== 0) nonZero++;

        if (freq[b] !== 0) nonZero--;
        freq[b]++;
        if (freq[b] !== 0) nonZero++;

        if (nums[i] !== target[i]) {
            prefixMatch = false;
        }
    }

    return ans;
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
- [4109. Count Valid Suffix Sorts II](../../4001-4500/4109-count-valid-suffix-sorts-ii/)
- [3042. Count Prefix and Suffix Pairs I](../../3001-3500/3042-count-prefix-and-suffix-pairs-i/)
- [3045. Count Prefix and Suffix Pairs II](../../3001-3500/3045-count-prefix-and-suffix-pairs-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-valid-suffix-sorts-i/)
