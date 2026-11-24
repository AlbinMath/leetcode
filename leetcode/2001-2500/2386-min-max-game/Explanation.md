# LeetCode 2293: Min Max Game

**LeetCode Problem #2293 — Min Max Game**
Solve LeetCode Min Max Game using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Min Max Game |
| LeetCode | #2293 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums` whose length is a power of `2`.

Apply the following algorithm on `nums`:

Let `n` be the length of `nums`. If `n == 1`, **end** the process. Otherwise, **create** a new **0-indexed** integer array `newNums` of length `n / 2`. 
 For every **even** index `i` where `0 <= i < n / 2`, **assign** the value of `newNums[i]` as `min(nums[2 * i], nums[2 * i + 1])`. 
 For every **odd** index `i` where `0 <= i < n / 2`, **assign** the value of `newNums[i]` as `max(nums[2 * i], nums[2 * i + 1])`. 
 **Replace** the array `nums` with `newNums`. 
 **Repeat** the entire process starting from step 1.

Return *the last number that remains in *`nums`* after applying the algorithm.*

## Constraints
- `1 <= nums.length <= 1024`
- `1 <= nums[i] <= 10^9`
- `nums.length` is a power of `2`.

## Examples
### Example 1
- **Input:** `nums = [1,3,5,2,4,8,2,2]`
- **Output:** `1`
- **Explanation:** The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.

### Example 2
- **Input:** `nums = [3]`
- **Output:** `3`
- **Explanation:** 3 is already the last remaining number, so we return 3.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Min Max Game**, we observe the problem requirements and utilize the **Stack & Queue** technique. We iterate through the inputs using **Stack Push / Pop Parsing**, leveraging a **Stack** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Stack**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,5,2,4,8,2,2]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minMaxGame = function(nums) {
    let n = nums.length;
    
    while (n > 1) {
        const half = n >> 1;
        for (let i = 0; i < half; i++) {
            if (i % 2 === 0) {
                nums[i] = Math.min(nums[2 * i], nums[2 * i + 1]);
            } else {
                nums[i] = Math.max(nums[2 * i], nums[2 * i + 1]);
            }
        }
        n = half;
    }
    
    return nums[0];
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3578. Count Partitions With Max-Min Difference at Most K](../../3501-4000/3835-count-partitions-with-max-min-difference-at-most-k/)
- [149. Max Points on a Line](../../0001-0500/0149-max-points-on-a-line/)
- [363. Max Sum of Rectangle No Larger Than K](../../0001-0500/0363-max-sum-of-rectangle-no-larger-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/min-max-game/)
