# LeetCode 2161: Partition Array According to Given Pivot

**LeetCode Problem #2161 — Partition Array According to Given Pivot**
Solve LeetCode Partition Array According to Given Pivot using Java and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Partition Array According to Given Pivot |
| LeetCode | #2161 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums` and an integer `pivot`. Rearrange `nums` such that the following conditions are satisfied:

Every element less than `pivot` appears **before** every element greater than `pivot`. 
 Every element equal to `pivot` appears **in between** the elements less than and greater than `pivot`. 
 The **relative order** of the elements less than `pivot` and the elements greater than `pivot` is maintained.
 
 More formally, consider every `p_i`, `p_j` where `p_i` is the new position of the `i^th` element and `p_j` is the new position of the `j^th` element. If `i < j` and **both** elements are smaller (*or larger*) than `pivot`, then `p_i < p_j`.

Return `nums`* after the rearrangement.*

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^6 <= nums[i] <= 10^6`
- `pivot` equals to an element of `nums`.

## Examples
### Example 1
- **Input:** `nums = [9,12,5,10,14,3,10], pivot = 10`
- **Output:** `[9,5,3,10,10,12,14]`
- **Explanation:** The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

### Example 2
- **Input:** `nums = [-3,4,3,2], pivot = 2`
- **Output:** `[-3,2,4,3]`
- **Explanation:** The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
Three-pass approach: collect elements < pivot, then == pivot, then > pivot, and concatenate them. This maintains relative order within each partition.

## Algorithm
1. Initialize state variables / data structure (**Tree / Graph / Grid**).
2. Process elements sequentially using **Depth-First Search (DFS) / Breadth-First Search (BFS)**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [9,12,5,10,14,3,10], pivot = 10`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[9,5,3,10,10,12,14]`.
4. **Verification:** The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

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
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int[] result = new int[n];
        int index = 0;

        // Elements smaller than pivot
        for (int num : nums) {
            if (num < pivot) {
                result[index++] = num;
            }
        }

        // Elements equal to pivot
        for (int num : nums) {
            if (num == pivot) {
                result[index++] = num;
            }
        }

        // Elements greater than pivot
        for (int num : nums) {
            if (num > pivot) {
                result[index++] = num;
            }
        }

        return result;
    }
}
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
- [561. Array Partition](../../0501-1000/0561-array-partition/)
- [1389. Create Target Array in the Given Order](../../1001-1500/1389-create-target-array-in-the-given-order/)
- [1802. Maximum Value at a Given Index in a Bounded Array](../../1501-2000/1802-maximum-value-at-a-given-index-in-a-bounded-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/partition-array-according-to-given-pivot/)
