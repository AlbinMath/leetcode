# LeetCode 3852: Smallest Pair With Different Frequencies

**LeetCode Problem #3852 — Smallest Pair With Different Frequencies**
Solve LeetCode Smallest Pair With Different Frequencies using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Pair With Different Frequencies |
| LeetCode | #3852 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

Consider all pairs of **distinct** values `x` and `y` from `nums` such that:

`x < y` 
 `x` and `y` have different frequencies in `nums`.

Among all such pairs:

Choose the pair with the smallest possible value of `x`. 
 If multiple pairs have the same `x`, choose the one with the smallest possible value of `y`.

Return an integer array `[x, y]`. If no valid pair exists, return `[-1, -1]`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,1,2,2,3,4]`
- **Output:** `[1,3]`
- **Explanation:** The smallest value is 1 with a frequency of 2, and the smallest value greater than 1 that has a different frequency from 1 is 3 with a frequency of 1. Thus, the answer is `[1, 3]`.

### Example 2
- **Input:** `nums = [1,5]`
- **Output:** `[-1,-1]`
- **Explanation:** Both values have the same frequency, so no valid pair exists. Return `[-1, -1]`.

### Example 3
- **Input:** `nums = [7]`
- **Output:** `[-1,-1]`
- **Explanation:** There is only one value in the array, so no valid pair exists. Return `[-1, -1]`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Smallest Pair With Different Frequencies**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,2,2,3,4]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3]`.
4. **Verification:** The smallest value is 1 with a frequency of 2, and the smallest value greater than 1 that has a different frequency from 1 is 3 with a frequency of 1. Thus, the answer is `[1, 3]`.

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
var minDistinctFreqPair = function(nums) {
    const freq = new Array(101).fill(0);

    // Step 1: Count frequencies
    for (let num of nums) {
        freq[num]++;
    }

    // Step 2: Find the smallest number
    let x = -1;

    for (let i = 1; i <= 100; i++) {
        if (freq[i] > 0) {
            x = i;
            break;
        }
    }

    // Step 3: Find the smallest valid y
    for (let y = x + 1; y <= 100; y++) {
        if (freq[y] > 0 && freq[y] !== freq[x]) {
            return [x, y];
        }
    }

    return [-1, -1];
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
- [719. Find K-th Smallest Pair Distance](../../0501-1000/0719-find-k-th-smallest-pair-distance/)
- [646. Maximum Length of Pair Chain](../../0501-1000/0646-maximum-length-of-pair-chain/)
- [1190. Reverse Substrings Between Each Pair of Parentheses](../../1001-1500/1190-reverse-substrings-between-each-pair-of-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-pair-with-different-frequencies/)
