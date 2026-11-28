# LeetCode 350: Intersection of Two Arrays II

**LeetCode Problem #350 — Intersection of Two Arrays II**
Solve LeetCode Intersection of Two Arrays II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Intersection of Two Arrays II |
| LeetCode | #350 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

## Constraints
- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`
- What if the given array is already sorted? How would you optimize your algorithm?
- What if `nums1`'s size is small compared to `nums2`'s size? Which algorithm is better?
- What if elements of `nums2` are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

## Examples
### Example 1
- **Input:** `nums1 = [1,2,2,1], nums2 = [2,2]`
- **Output:** `[2,2]`

### Example 2
- **Input:** `nums1 = [4,9,5], nums2 = [9,4,9,8,4]`
- **Output:** `[4,9]`
- **Explanation:** [9,4] is also accepted.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Intersection of Two Arrays II**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [1,2,2,1], nums2 = [2,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,2]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def intersect(self, nums1, nums2):
        count = {}
        result = []

        # Count occurrences in nums1
        for num in nums1:
            count[num] = count.get(num, 0) + 1

        # Find matching elements in nums2
        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [349. Intersection of Two Arrays](../../0001-0500/0349-intersection-of-two-arrays/)
- [160. Intersection of Two Linked Lists](../../0001-0500/0160-intersection-of-two-linked-lists/)
- [757. Set Intersection Size At Least Two](../../0501-1000/0757-set-intersection-size-at-least-two/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
