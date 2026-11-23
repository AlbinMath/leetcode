# LeetCode 2963: Count the Number of Good Partitions

**LeetCode Problem #2963 — Count the Number of Good Partitions**
Solve LeetCode Count the Number of Good Partitions using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Number of Good Partitions |
| LeetCode | #2963 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array `nums` consisting of **positive** integers.

A partition of an array into one or more **contiguous** subarrays is called **good** if no two subarrays contain the same number.

Return *the **total number** of good partitions of *`nums`.

Since the answer may be large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4]`
- **Output:** `8`
- **Explanation:** The 8 possible good partitions are: ([1], [2], [3], [4]), ([1], [2], [3,4]), ([1], [2,3], [4]), ([1], [2,3,4]), ([1,2], [3], [4]), ([1,2], [3,4]), ([1,2,3], [4]), and ([1,2,3,4]).

### Example 2
- **Input:** `nums = [1,1,1,1]`
- **Output:** `1`
- **Explanation:** The only possible good partition is: ([1,1,1,1]).

### Example 3
- **Input:** `nums = [1,2,1,3]`
- **Output:** `2`
- **Explanation:** The 2 possible good partitions are: ([1,2,1], [3]) and ([1,2,1,3]).

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count the Number of Good Partitions**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The 8 possible good partitions are: ([1], [2], [3], [4]), ([1], [2], [3,4]), ([1], [2,3], [4]), ([1], [2,3,4]), ([1,2], [3], [4]), ([1,2], [3,4]), ([1,2,3], [4]), and ([1,2,3,4]).

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
var numberOfGoodPartitions = function(nums) {
    const MOD = 1000000007;
    const last = new Map();

    for (let i = 0; i < nums.length; i++) {
        last.set(nums[i], i);
    }

    let partitions = 0;
    let end = 0;

    for (let i = 0; i < nums.length; i++) {
        end = Math.max(end, last.get(nums[i]));

        if (i === end && i < nums.length - 1) {
            partitions++;
        }
    }

    return Number(2n ** BigInt(partitions) % BigInt(MOD));
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
- [2537. Count the Number of Good Subarrays](../../2501-3000/2626-count-the-number-of-good-subarrays/)
- [1248. Count Number of Nice Subarrays](../../1001-1500/1370-count-number-of-nice-subarrays/)
- [1395. Count Number of Teams](../../1501-2000/1511-count-number-of-teams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-number-of-good-partitions/)
