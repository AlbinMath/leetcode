# LeetCode 1846: Maximum Element After Decreasing and Rearranging

**LeetCode Problem #1846 — Maximum Element After Decreasing and Rearranging**
Solve LeetCode Maximum Element After Decreasing and Rearranging using Java and Binary Search. This solution finds the optimal result using Modified Binary Search in O(log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Element After Decreasing and Rearranging |
| LeetCode | #1846 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of positive integers `arr`. Perform some operations (possibly none) on `arr` so that it satisfies these conditions:

The value of the **first** element in `arr` must be `1`. 
 The absolute difference between any 2 adjacent elements must be **less than or equal to **`1`. In other words, `abs(arr[i] - arr[i - 1]) <= 1` for each `i` where `1 <= i < arr.length` (**0-indexed**). `abs(x)` is the absolute value of `x`.

There are 2 types of operations that you can perform any number of times:

**Decrease** the value of any element of `arr` to a **smaller positive integer**. 
 **Rearrange** the elements of `arr` to be in any order.

Return *the **maximum** possible value of an element in *`arr`* after performing the operations to satisfy the conditions*.

## Constraints
- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^9`

## Examples
### Example 1
- **Input:** `arr = [2,2,1,2,1]`
- **Output:** `2`
- **Explanation:** We can satisfy the conditions by rearranging `arr` so it becomes `[1,2,2,2,1]`.
The largest element in `arr` is 2.

### Example 2
- **Input:** `arr = [100,1,1000]`
- **Output:** `3`
- **Explanation:** One possible way to satisfy the conditions is by doing the following:
1. Rearrange `arr` so it becomes `[1,100,1000]`.
2. Decrease the value of the second element to 2.
3. Decrease the value of the third element to 3.
Now `arr = [1,2,3]`, which satisfies the conditions.
The largest element in `arr is 3.`

### Example 3
- **Input:** `arr = [1,2,3,4,5]`
- **Output:** `5`
- **Explanation:** The array already satisfies the conditions, and the largest element is 5.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
1. **Sort** the array in ascending order.
2. Initialize `max = 0`. For each element, set `max = min(num, max + 1)`. This greedily builds the longest possible increasing sequence where each step increases by at most 1.
3. Return `max`.

Time complexity is $O(N \log N)$ and space complexity is $O(\log N)$ for sorting.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [2,2,1,2,1]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We can satisfy the conditions by rearranging `arr` so it becomes `[1,2,2,2,1]`.
The largest element in `arr` is 2.

## Complexity Analysis
- **Time Complexity:** O(log n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
import java.util.Arrays;

class Solution {
    public int maximumElementAfterDecrementingAndRearranging(int[] arr) {
        Arrays.sort(arr);

        int max = 0;

        for (int num : arr) {
            max = Math.min(num, max + 1);
        }

        return max;
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
- [3346. Maximum Frequency of an Element After Performing Operations I](../../3001-3500/3346-maximum-frequency-of-an-element-after-performing-operations-i/)
- [3347. Maximum Frequency of an Element After Performing Operations II](../../3001-3500/3347-maximum-frequency-of-an-element-after-performing-operations-ii/)
- [2945. Find Maximum Non-decreasing Array Length](../../2501-3000/2945-find-maximum-non-decreasing-array-length/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/)
