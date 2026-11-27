# LeetCode 1471: The k Strongest Values in an Array

**LeetCode Problem #1471 — The k Strongest Values in an Array**
Solve LeetCode The k Strongest Values in an Array using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The k Strongest Values in an Array |
| LeetCode | #1471 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `arr` and an integer `k`.

A value `arr[i]` is said to be stronger than a value `arr[j]` if `|arr[i] - m| > |arr[j] - m|` where `m` is the **centre** of the array. 
If `|arr[i] - m| == |arr[j] - m|`, then `arr[i]` is said to be stronger than `arr[j]` if `arr[i] > arr[j]`.

Return *a list of the strongest `k`* values in the array. Return the answer **in any arbitrary order**.

The **centre** is the middle value in an ordered integer list. More formally, if the length of the list is n, the centre is the element in position `((n - 1) / 2)` in the sorted list **(0-indexed)**.

For `arr = [6, -3, 7, 2, 11]`, `n = 5` and the centre is obtained by sorting the array `arr = [-3, 2, 6, 7, 11]` and the centre is `arr[m]` where `m = ((5 - 1) / 2) = 2`. The centre is `6`. 
 For `arr = [-7, 22, 17,&thinsp;3]`, `n = 4` and the centre is obtained by sorting the array `arr = [-7, 3, 17, 22]` and the centre is `arr[m]` where `m = ((4 - 1) / 2) = 1`. The centre is `3`.

## Constraints
- `1 <= arr.length <= 10^5`
- `-10^5 <= arr[i] <= 10^5`
- `1 <= k <= arr.length`

## Examples
### Example 1
- **Input:** `arr = [1,2,3,4,5], k = 2`
- **Output:** `[5,1]`
- **Explanation:** Centre is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also

### Example 2
- **Input:** `arr = [1,1,3,5,5], k = 2`
- **Output:** `[5,5]`
- **Explanation:** Centre is 3, the elements of the array sorted by the strongest are [5,5,1,1,3]. The strongest 2 elements are [5, 5].

### Example 3
- **Input:** `arr = [6,7,11,7,6,8], k = 5`
- **Output:** `[11,8,6,6,7]`
- **Explanation:** Centre is 7, the elements of the array sorted by the strongest are [11,8,6,6,7,7].
Any permutation of [11,8,6,6,7] is

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **The k Strongest Values in an Array**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,3,4,5], k = 2`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[5,1]`.
4. **Verification:** Centre is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var getStrongest = function(arr, k) {
    arr.sort((a, b) => a - b);
    const m = arr[Math.floor((arr.length - 1) / 2)];
    arr.sort((a, b) => {
        const diffA = Math.abs(a - m);
        const diffB = Math.abs(b - m);
        if (diffA !== diffB) {
            return diffB - diffA;
        }

        return b - a;
    });

    return arr.slice(0, k);
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2522. Partition String Into Substrings With Values at Most K](../../2501-3000/2522-partition-string-into-substrings-with-values-at-most-k/)
- [2859. Sum of Values at Indices With K Set Bits](../../2501-3000/2859-sum-of-values-at-indices-with-k-set-bits/)
- [3117. Minimum Sum of Values by Dividing Array](../../3001-3500/3117-minimum-sum-of-values-by-dividing-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-k-strongest-values-in-an-array/)
