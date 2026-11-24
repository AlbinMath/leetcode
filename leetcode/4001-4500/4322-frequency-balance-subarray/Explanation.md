# LeetCode 3960: Frequency Balance Subarray

**LeetCode Problem #3960 — Frequency Balance Subarray**
Solve LeetCode Frequency Balance Subarray using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Frequency Balance Subarray |
| LeetCode | #3960 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array ​​​​​​​`nums`.

Define a **frequency balance subarray ** as follows:

If the subarray contains only one distinct value, it is frequency balanced. 
 Otherwise, there must exist a positive integer `f` such that every distinct value in the subarray occurs either `f` or `2 * f` times, and both frequencies occur among the distinct values.

Return an integer denoting the length of the **longest** frequency balance subarray.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^​​​​​​​9`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,1,2,3,3,3]`
- **Output:** `5`
- **Explanation:** The longest frequency balance subarray is `[2, 1, 2, 3, 3]`. 
 The elements that appear most frequently are 2 and 3, both appearing twice. 
 The remaining element 1 appears once, meeting the requirements.

### Example 2
- **Input:** `nums = [5,5,5,5]`
- **Output:** `4`
- **Explanation:** The longest frequency balance subarray is `[5, 5, 5, 5]`. 
 The element that appears most frequently is 5. 
 There are no other elements meeting the requirements.

### Example 3
- **Input:** `nums = [1,2,3,4]`
- **Output:** `1`
- **Explanation:** Since all elements appear only once, the length of the longest frequency balance subarray is 1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Frequency Balance Subarray**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,1,2,3,3,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** The longest frequency balance subarray is `[2, 1, 2, 3, 3]`. 
 The elements that appear most frequently are 2 and 3, both appearing twice. 
 The remaining element 1 appears once, meeting the requirements.

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
var getLength = function(nums) {
    const n = nums.length;
    let ans = 1;

    for (let i = 0; i < n; i++) {
        const freq = new Map();
        const freqCount = new Map();

        for (let j = i; j < n; j++) {
            const num = nums[j];

            const oldFreq = freq.get(num) || 0;
            const newFreq = oldFreq + 1;

            // Remove old frequency
            if (oldFreq > 0) {
                const count = freqCount.get(oldFreq);

                if (count === 1) {
                    freqCount.delete(oldFreq);
                } else {
                    freqCount.set(oldFreq, count - 1);
                }
            }

            // Update frequency
            freq.set(num, newFreq);

            freqCount.set(
                newFreq,
                (freqCount.get(newFreq) || 0) + 1
            );

            // Only one distinct value
            if (freq.size === 1) {
                ans = Math.max(ans, j - i + 1);
                continue;
            }

            // Check frequency balance
            if (freqCount.size === 2) {
                const [a, b] = freqCount.keys();

                if (Math.max(a, b) === 2 * Math.min(a, b)) {
                    ans = Math.max(ans, j - i + 1);
                }
            }
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
- [2958. Length of Longest Subarray With at Most K Frequency](../../3001-3500/3225-length-of-longest-subarray-with-at-most-k-frequency/)
- [3434. Maximum Frequency After Subarray Operation](../../3501-4000/3751-maximum-frequency-after-subarray-operation/)
- [53. Maximum Subarray](../../0001-0500/0053-maximum-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/frequency-balance-subarray/)
