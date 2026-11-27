# LeetCode 3994: Minimum Adjacent Swaps to Partition Array

**LeetCode Problem #3994 — Minimum Adjacent Swaps to Partition Array**
Solve LeetCode Minimum Adjacent Swaps to Partition Array using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Adjacent Swaps to Partition Array |
| LeetCode | #3994 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and two integers `a` and `b` such that `a < b`.

An array is called **good** if it can be split into three **contiguous** parts, in this order, such that:

Every element in the first part is **less than** `a`. 
 Every element in the second part is **in** the range `[a, b]` inclusive. 
 Every element in the third part is **greater than** `b`.

Any of the three parts **may be** empty.

In one **adjacent swap**, you may swap two **neighboring** elements of `nums`.

Return the **minimum number** of adjacent swaps required to make `nums` good. Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= nums.length <= 10^5`
- `​​​​​​​1 <= nums[i] <= 10^9`
- `1 <= a < b <= 10^9​​​​​​​`

## Examples
### Example 1
- **Input:** `nums = [1,3,2,4,5,6], a = 3, b = 4`
- **Output:** `1`
- **Explanation:** Swap `nums[1]` and `nums[2]`. The array becomes `[1, 2, 3, 4, 5, 6]`. 
 This array is good because it can be split into `[1, 2]`, `[3, 4]`, and `[5, 6]`.

### Example 2
- **Input:** `nums = [9,7,5,3], a = 4, b = 8`
- **Output:** `5`
- **Explanation:** One sequence of optimal swaps is as follows: 

 
 Swap `nums[2]` and `nums[3]`. The array becomes `[9, 7, 3, 5]`. 
 Swap `nums[1]` and `nums[2]`. The array becomes `[9, 3, 7, 5]`. 
 Swap `nums[0]` and `nums[1]`. The array becomes `[3, 9, 7, 5]`. 
 Swap `nums[1]` and `nums[2]`. The array becomes `[3, 7, 9, 5]`. 
 Swap `nums[2]` and `nums[3]`. The array becomes `[3, 7, 5, 9]`. 
 This array is good because it can be split into `[3]`, `[7, 5]`, and `[9]`.

### Example 3
- **Input:** `nums = [3,7,5,9], a = 4, b = 8`
- **Output:** `0`
- **Explanation:** The array is already good. No swaps are needed.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Adjacent Swaps to Partition Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,3,2,4,5,6], a = 3, b = 4`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Swap `nums[1]` and `nums[2]`. The array becomes `[1, 2, 3, 4, 5, 6]`. 
 This array is good because it can be split into `[1, 2]`, `[3, 4]`, and `[5, 6]`.

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
var minAdjacentSwaps = function(nums, a, b) {
    const MOD = 1000000007;

    let count1 = 0;
    let count2 = 0;
    let answer = 0;

    for (const num of nums) {
        if (num < a) {
            answer = (answer + count1 + count2) % MOD;
        } else if (num <= b) {
            answer = (answer + count2) % MOD;
            count1++;
        } else {
            count2++;
        }
    }

    return answer;
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
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1505-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](../../1501-2000/1703-minimum-adjacent-swaps-for-k-consecutive-ones/)
- [1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number](../../1501-2000/1850-minimum-adjacent-swaps-to-reach-the-kth-smallest-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/)
