# LeetCode 2597: The Number of Beautiful Subsets

**LeetCode Problem #2597 — The Number of Beautiful Subsets**
Solve LeetCode The Number of Beautiful Subsets using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The Number of Beautiful Subsets |
| LeetCode | #2597 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` of positive integers and a **positive** integer `k`.

A subset of `nums` is **beautiful** if it does not contain two integers with an absolute difference equal to `k`.

Return *the number of **non-empty beautiful **subsets of the array* `nums`.

A **subset** of `nums` is an array that can be obtained by deleting some (possibly none) elements from `nums`. Two subsets are different if and only if the chosen indices to delete are different.

## Constraints
- `1 <= nums.length <= 18`
- `1 <= nums[i], k <= 1000`

## Examples
### Example 1
- **Input:** `nums = [2,4,6], k = 2`
- **Output:** `4`
- **Explanation:** The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

### Example 2
- **Input:** `nums = [1], k = 1`
- **Output:** `1`
- **Explanation:** The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **The Number of Beautiful Subsets**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,4,6], k = 2`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var beautifulSubsets = function(nums, k) {
    let count = 0;
    const freq = new Map();

    function backtrack(index) {
        if (index === nums.length) {
            count++;
            return;
        }

        // Skip the current element.
        backtrack(index + 1);

        const num = nums[index];

        // Include it only if num - k and num + k are absent.
        if (!freq.has(num - k) && !freq.has(num + k)) {
            freq.set(num, (freq.get(num) || 0) + 1);

            backtrack(index + 1);

            freq.set(num, freq.get(num) - 1);
            if (freq.get(num) === 0) {
                freq.delete(num);
            }
        }
    }

    backtrack(0);

    return count - 1; // Exclude the empty subset.
};
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2478. Number of Beautiful Partitions](../../2001-2500/2478-number-of-beautiful-partitions/)
- [2588. Count the Number of Beautiful Subarrays](../../2501-3000/2588-count-the-number-of-beautiful-subarrays/)
- [2748. Number of Beautiful Pairs](../../2501-3000/2748-number-of-beautiful-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-number-of-beautiful-subsets/)
