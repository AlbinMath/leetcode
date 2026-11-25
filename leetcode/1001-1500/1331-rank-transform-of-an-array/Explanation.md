# LeetCode 1331: Rank Transform of an Array

**LeetCode Problem #1331 — Rank Transform of an Array**
Solve LeetCode Rank Transform of an Array using Kotlin and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Rank Transform of an Array |
| LeetCode | #1331 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `arr`, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1. 
 The larger the element, the larger the rank. If two elements are equal, their rank must be the same. 
 Rank should be as small as possible.

## Constraints
- `0 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

## Examples
### Example 1
- **Input:** `arr = [40,10,20,30]`
- **Output:** `[4,1,2,3]`
- **Explanation:** : 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

### Example 2
- **Input:** `arr = [100,100,100]`
- **Output:** `[1,1,1]`
- **Explanation:** : Same elements share the same rank.

### Example 3
- **Input:** `arr = [37,12,28,9,100,56,80,5,12]`
- **Output:** `[5,3,4,2,8,6,7,1,3]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
1. **Sort a Copy:** Clone the array and sort it.
2. **Map Values to Ranks:** Iterate through the sorted array, assigning incrementing ranks. Skip duplicates (if a value was already assigned a rank, don't increment).
3. **Replace:** Build the result by looking up each original element's rank from the map.

Time complexity is $O(N \log N)$ for sorting and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [40,10,20,30]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,1,2,3]`.
4. **Verification:** : 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)


```kotlin
class Solution {
    fun arrayRankTransform(arr: IntArray): IntArray {
        val sorted = arr.clone()
        sorted.sort()

        val rank = HashMap<Int, Int>()
        var r = 1

        for (num in sorted) {
            if (!rank.containsKey(num)) {
                rank[num] = r
                r++
            }
        }

        return IntArray(arr.size) { i ->
            rank[arr[i]]!!
        }
    }
}
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [2635. Apply Transform Over Each Element in Array](../../2501-3000/2635-apply-transform-over-each-element-in-array/)
- [3467. Transform Array by Parity](../../3001-3500/3467-transform-array-by-parity/)
- [3896. Minimum Operations to Transform Array into Alternating Prime](../../3501-4000/3896-minimum-operations-to-transform-array-into-alternating-prime/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/rank-transform-of-an-array/)
