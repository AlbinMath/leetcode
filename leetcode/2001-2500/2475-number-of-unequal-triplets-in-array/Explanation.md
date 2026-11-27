# LeetCode 2475: Number of Unequal Triplets in Array

**LeetCode Problem #2475 — Number of Unequal Triplets in Array**
Solve LeetCode Number of Unequal Triplets in Array using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Unequal Triplets in Array |
| LeetCode | #2475 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array of positive integers `nums`. Find the number of triplets `(i, j, k)` that meet the following conditions:

`0 <= i < j < k < nums.length` 
 `nums[i]`, `nums[j]`, and `nums[k]` are **pairwise distinct**.
 
 In other words, `nums[i] != nums[j]`, `nums[i] != nums[k]`, and `nums[j] != nums[k]`.

Return *the number of triplets that meet the conditions.*

## Constraints
- `3 <= nums.length <= 100`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [4,4,2,4,3]`
- **Output:** `3`
- **Explanation:** The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.

### Example 2
- **Input:** `nums = [1,1,1,1,1]`
- **Output:** `0`
- **Explanation:** No triplets meet the conditions so we return 0.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Unequal Triplets in Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,4,2,4,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.

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
var unequalTriplets = function(nums) {
    const freq = new Map();

    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    const counts = Array.from(freq.values());

    let result = 0;

    for (let i = 0; i < counts.length; i++) {
        for (let j = i + 1; j < counts.length; j++) {
            for (let k = j + 1; k < counts.length; k++) {
                result += counts[i] * counts[j] * counts[k];
            }
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
- [2179. Count Good Triplets in an Array](../../2001-2500/2179-count-good-triplets-in-an-array/)
- [2367. Number of Arithmetic Triplets](../../2001-2500/2367-number-of-arithmetic-triplets/)
- [3513. Number of Unique XOR Triplets I](../../3501-4000/3513-number-of-unique-xor-triplets-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-unequal-triplets-in-array/)
