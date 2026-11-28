# LeetCode 3002: Maximum Size of a Set After Removals

**LeetCode Problem #3002 — Maximum Size of a Set After Removals**
Solve LeetCode Maximum Size of a Set After Removals using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Size of a Set After Removals |
| LeetCode | #3002 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two **0-indexed** integer arrays `nums1` and `nums2` of even length `n`.

You must remove `n / 2` elements from `nums1` and `n / 2` elements from `nums2`. After the removals, you insert the remaining elements of `nums1` and `nums2` into a set `s`.

Return *the **maximum** possible size of the set* `s`.

## Constraints
- `n == nums1.length == nums2.length`
- `1 <= n <= 2 * 10^4`
- `n` is even.
- `1 <= nums1[i], nums2[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums1 = [1,2,1,2], nums2 = [1,1,1,1]`
- **Output:** `2`
- **Explanation:** We remove two occurences of 1 from nums1 and nums2. After the removals, the arrays become equal to nums1 = [2,2] and nums2 = [1,1]. Therefore, s = {1,2}.
It can be shown that 2 is the maximum possible size of the set s after the removals.

### Example 2
- **Input:** `nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]`
- **Output:** `5`
- **Explanation:** We remove 2, 3, and 6 from nums1, as well as 2 and two occurrences of 3 from nums2. After the removals, the arrays become equal to nums1 = [1,4,5] and nums2 = [2,3,2]. Therefore, s = {1,2,3,4,5}.
It can be shown that 5 is the maximum possible size of the set s after the removals.

### Example 3
- **Input:** `nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]`
- **Output:** `6`
- **Explanation:** We remove 1, 2, and 3 from nums1, as well as 4, 5, and 6 from nums2. After the removals, the arrays become equal to nums1 = [1,2,3] and nums2 = [4,5,6]. Therefore, s = {1,2,3,4,5,6}.
It can be shown that 6 is the maximum possible size of the set s after the removals.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Size of a Set After Removals**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2,1,2], nums2 = [1,1,1,1]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We remove two occurences of 1 from nums1 and nums2. After the removals, the arrays become equal to nums1 = [2,2] and nums2 = [1,1]. Therefore, s = {1,2}.
It can be shown that 2 is the maximum possible size of the set s after the removals.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maximumSetSize = function(nums1, nums2) {
    const n = nums1.length;
    const limit = n / 2;

    const set1 = new Set(nums1);
    const set2 = new Set(nums2);
    const count1 = Math.min(limit, set1.size);
    const count2 = Math.min(limit, set2.size);
    const union = new Set([...set1, ...set2]).size;

    return Math.min(union, count1 + count2);
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [2382. Maximum Segment Sum After Removals](../../2001-2500/2382-maximum-segment-sum-after-removals/)
- [757. Set Intersection Size At Least Two](../../0501-1000/0757-set-intersection-size-at-least-two/)
- [1422. Maximum Score After Splitting a String](../../1001-1500/1422-maximum-score-after-splitting-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-size-of-a-set-after-removals/)
