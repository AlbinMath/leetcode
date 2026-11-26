# LeetCode 1477: Find Two Non-overlapping Sub-arrays Each With Target Sum

**LeetCode Problem #1477 — Find Two Non-overlapping Sub-arrays Each With Target Sum**
Solve LeetCode Find Two Non-overlapping Sub-arrays Each With Target Sum using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Two Non-overlapping Sub-arrays Each With Target Sum |
| LeetCode | #1477 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of integers `arr` and an integer `target`.

You have to find **two non-overlapping sub-arrays** of `arr` each with a sum equal `target`. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is **minimum**.

Return *the minimum sum of the lengths* of the two required sub-arrays, or return `-1` if you cannot find such two sub-arrays.

## Constraints
- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 1000`
- `1 <= target <= 10^8`

## Examples
### Example 1
- **Input:** `arr = [3,2,2,4,3], target = 3`
- **Output:** `2`
- **Explanation:** Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

### Example 2
- **Input:** `arr = [7,3,4,7], target = 7`
- **Output:** `2`
- **Explanation:** Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.

### Example 3
- **Input:** `arr = [4,3,2,6,2,3,4], target = 6`
- **Output:** `-1`
- **Explanation:** We have only one sub-array of sum = 6.

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
The code uses a **Sliding Window** to find all subarrays with the target sum, combined with a DP approach to track the shortest valid subarray ending at or before each index. It then considers all valid pairs of non-overlapping subarrays and finds the minimum combined length.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Array / Hash Set**).
2. Process elements sequentially using **Dynamic Sliding Window Traversal**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [3,2,2,4,3], target = 3`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minSumOfLengths = function(arr, target) {
    const n = arr.length;
    const best = new Array(n).fill(Infinity);

    let left = 0;
    let sum = 0;
    let minLen = Infinity;
    let answer = Infinity;

    for (let right = 0; right < n; right++) {
        sum += arr[right];

        while (sum > target && left <= right) {
            sum -= arr[left];
            left++;
        }

        // Subarray [left ... right] has sum = target
        if (sum === target) {
            const len = right - left + 1;

            // Combine with a previous non-overlapping subarray
            if (left > 0 && best[left - 1] !== Infinity) {
                answer = Math.min(answer, len + best[left - 1]);
            }

            minLen = Math.min(minLen, len);
        }

        // Best subarray ending at or before right
        best[right] = minLen;
    }

    return answer === Infinity ? -1 : answer;
};
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1031-maximum-sum-of-two-non-overlapping-subarrays/)
- [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](../../1501-2000/1546-maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)
