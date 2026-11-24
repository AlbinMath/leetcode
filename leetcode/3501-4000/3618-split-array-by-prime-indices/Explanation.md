# LeetCode 3618: Split Array by Prime Indices

**LeetCode Problem #3618 — Split Array by Prime Indices**
Solve LeetCode Split Array by Prime Indices using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split Array by Prime Indices |
| LeetCode | #3618 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums`.

Split `nums` into two arrays `A` and `B` using the following rule:

Elements at ** prime ** indices in `nums` must go into array `A`. 
 All other elements must go into array `B`.

Return the **absolute** difference between the sums of the two arrays: `|sum(A) - sum(B)|`.

**Note:** An empty array has a sum of 0.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [2,3,4]`
- **Output:** `1`
- **Explanation:** The only prime index in the array is 2, so `nums[2] = 4` is placed in array `A`. 
 The remaining elements, `nums[0] = 2` and `nums[1] = 3` are placed in array `B`. 
 `sum(A) = 4`, `sum(B) = 2 + 3 = 5`. 
 The absolute difference is `|4 - 5| = 1`.

### Example 2
- **Input:** `nums = [-1,5,7,0]`
- **Output:** `3`
- **Explanation:** The prime indices in the array are 2 and 3, so `nums[2] = 7` and `nums[3] = 0` are placed in array `A`. 
 The remaining elements, `nums[0] = -1` and `nums[1] = 5` are placed in array `B`. 
 `sum(A) = 7 + 0 = 7`, `sum(B) = -1 + 5 = 4`. 
 The absolute difference is `|7 - 4| = 3`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Split Array by Prime Indices**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,4]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The only prime index in the array is 2, so `nums[2] = 4` is placed in array `A`. 
 The remaining elements, `nums[0] = 2` and `nums[1] = 3` are placed in array `B`. 
 `sum(A) = 4`, `sum(B) = 2 + 3 = 5`. 
 The absolute difference is `|4 - 5| = 1`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var splitArray = function(nums) {
    const n = nums.length;

    // 1. Sieve of Eratosthenes to mark prime indices up to n - 1
    const isPrime = new Uint8Array(n).fill(1);
    isPrime[0] = 0;
    if (n > 1) isPrime[1] = 0;

    for (let i = 2; i * i < n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j < n; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // 2. Accumulate sum(A) - sum(B)
    let diff = 0;
    for (let i = 0; i < n; i++) {
        if (isPrime[i]) {
            diff += nums[i];
        } else {
            diff -= nums[i];
        }
    }

    return Math.abs(diff);
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2089. Find Target Indices After Sorting Array](../../2001-2500/2089-find-target-indices-after-sorting-array/)
- [3006. Find Beautiful Indices in the Given Array I](../../3001-3500/3006-find-beautiful-indices-in-the-given-array-i/)
- [3008. Find Beautiful Indices in the Given Array II](../../3001-3500/3008-find-beautiful-indices-in-the-given-array-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-array-by-prime-indices/)
