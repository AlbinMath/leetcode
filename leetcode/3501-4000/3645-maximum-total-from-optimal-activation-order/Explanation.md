# LeetCode 3645: Maximum Total from Optimal Activation Order

**LeetCode Problem #3645 — Maximum Total from Optimal Activation Order**
Solve LeetCode Maximum Total from Optimal Activation Order using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Total from Optimal Activation Order |
| LeetCode | #3645 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays `value` and `limit`, both of length `n`.

Initially, all elements are **inactive**. You may activate them in any order.

To activate an inactive element at index `i`, the number of **currently** active elements must be **strictly less** than `limit[i]`. 
 When you activate the element at index `i`, it adds `value[i]` to the **total** activation value (i.e., the sum of `value[i]` for all elements that have undergone activation operations). 
 After each activation, if the number of **currently** active elements becomes `x`, then **all** elements `j` with `limit[j] <= x` become **permanently** inactive, even if they are already active.

Return the **maximum** **total** you can obtain by choosing the activation order optimally.

## Constraints
- `1 <= n == value.length == limit.length <= 10^5`
- `1 <= value[i] <= 10^5`​​​​​​​
- `1 <= limit[i] <= n`

## Examples
### Example 1
- **Input:** `value = [3,5,8], limit = [2,1,3]`
- **Output:** `16`
- **Explanation:** One optimal activation order is: 

 
 
 
 Step 
 Activated `i` 
 `value[i]` 
 Active Before `i` 
 Active After `i` 
 Becomes Inactive `j` 
 Inactive Elements 
 Total 
 
 
 
 
 1 
 1 
 5 
 0 
 1 
 `j = 1` as `limit[1] = 1` 
 [1] 
 5 
 
 
 2 
 0 
 3 
 0 
 1 
 - 
 [1] 
 8 
 
 
 3 
 2 
 8 
 1 
 2 
 `j = 0` as `limit[0] = 2` 
 [0, 1] 
 16 
 
 
 

 Thus, the maximum possible total is 16.

### Example 2
- **Input:** `value = [4,2,6], limit = [1,1,1]`
- **Output:** `6`
- **Explanation:** One optimal activation order is: 

 
 
 
 Step 
 Activated `i` 
 `value[i]` 
 Active Before `i` 
 Active After `i` 
 Becomes Inactive `j` 
 Inactive Elements 
 Total 
 
 
 
 
 1 
 2 
 6 
 0 
 1 
 `j = 0, 1, 2` as `limit[j] = 1` 
 [0, 1, 2] 
 6 
 
 
 

 Thus, the maximum possible total is 6.

### Example 3
- **Input:** `value = [4,1,5,2], limit = [3,3,2,3]`
- **Output:** `12`
- **Explanation:** One optimal activation order is:​​​​​​​

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Total from Optimal Activation Order**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `value = [3,5,8], limit = [2,1,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `16`.
4. **Verification:** One optimal activation order is: 

 
 
 
 Step 
 Activated `i` 
 `value[i]` 
 Active Before `i` 
 Active After `i` 
 Becomes Inactive `j` 
 Inactive Elements 
 Total 
 
 
 
 
 1 
 1 
 5 
 0 
 1 
 `j = 1` as `limit[1] = 1` 
 [1] 
 5 
 
 
 2 
 0 
 3 
 0 
 1 
 - 
 [1] 
 8 
 
 
 3 
 2 
 8 
 1 
 2 
 `j = 0` as `limit[0] = 2` 
 [0, 1] 
 16 
 
 
 

 Thus, the maximum possible total is 16.

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
var maxTotal = function(value, limit) {
    const groups = new Map();
    for (let i = 0; i < value.length; i++) {
        if (!groups.has(limit[i])) {
            groups.set(limit[i], []);
        }

        groups.get(limit[i]).push(value[i]);
    }

    let ans = 0;

    for (const [lim, values] of groups) {
        values.sort((a, b) => b - a);

        for (let i = 0; i < Math.min(lim, values.length); i++) {
            ans += values[i];
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
- [3530. Maximum Profit from Valid Topological Order in DAG](../../3501-4000/3530-maximum-profit-from-valid-topological-order-in-dag/)
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)
- [1423. Maximum Points You Can Obtain from Cards](../../1001-1500/1423-maximum-points-you-can-obtain-from-cards/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-total-from-optimal-activation-order/)
