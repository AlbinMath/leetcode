# LeetCode 4038: Count Integers Appearing in a Single Block

**LeetCode Problem #4038 — Count Integers Appearing in a Single Block**
Solve LeetCode Count Integers Appearing in a Single Block using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Integers Appearing in a Single Block |
| LeetCode | #4038 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

An integer `x` is **special** if all occurrences of `x` in `nums` appear in a single **contiguous** block.

Return the number of **distinct** special integers in `nums`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,1]`
- **Output:** `1`
- **Explanation:** 1 appears at indices 0 and 3, forming two separate blocks, so it is not special. 
 2 appears in a single contiguous block at indices `[1, 2]`, so it is special. 
 

 Therefore, there is one special integer.

### Example 2
- **Input:** `nums = [3,3,1,2,2,1]`
- **Output:** `2`
- **Explanation:** 3 appears in a single contiguous block at indices `[0, 1]`, so it is special. 
 1 appears at indices 2 and 5, forming two separate blocks, so it is not special. 
 2 appears in a single contiguous block at indices `[3, 4]`, so it is special. 
 

 Therefore, there are two special integers.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Integers Appearing in a Single Block**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** 1 appears at indices 0 and 3, forming two separate blocks, so it is not special. 
 2 appears in a single contiguous block at indices `[1, 2]`, so it is special. 
 

 Therefore, there is one special integer.

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
var countSpecialIntegers = function(nums) {
    let blocks = new Map();

    for (let i = 0; i < nums.length; i++) {
        if (i === 0 || nums[i] !== nums[i - 1]) {
            blocks.set(nums[i], (blocks.get(nums[i]) || 0) + 1);
        }
    }

    let count = 0;

    for (let [num, freq] of blocks) {
        if (freq === 1) {
            count++;
        }
    }

    return count;
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
- [2180. Count Integers With Even Digit Sum](../../2001-2500/2298-count-integers-with-even-digit-sum/)
- [2276. Count Integers in Intervals](../../2001-2500/2357-count-integers-in-intervals/)
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2501-3000/2525-count-number-of-distinct-integers-after-reverse-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-integers-appearing-in-a-single-block/)
