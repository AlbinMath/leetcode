# LeetCode 852: Peak Index in a Mountain Array

**LeetCode Problem #852 — Peak Index in a Mountain Array**
Solve LeetCode Peak Index in a Mountain Array using JavaScript, Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Peak Index in a Mountain Array |
| LeetCode | #852 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer **mountain** array `arr` of length `n` where the values increase to a **peak element** and then decrease.

Return the index of the peak element.

Your task is to solve it in `O(log(n))` time complexity.

## Constraints
- `3 <= arr.length <= 10^5`
- `0 <= arr[i] <= 10^6`
- `arr` is **guaranteed** to be a mountain array.

## Examples
### Example 1
- **Input:** `arr = [0,1,0]`
- **Output:** `1`

### Example 2
- **Input:** `arr = [0,2,1,0]`
- **Output:** `1`

### Example 3
- **Input:** `arr = [0,10,5,2]`
- **Output:** `1`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Peak Index in a Mountain Array**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [0,1,0]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var peakIndexInMountainArray = function(arr) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (arr[mid] < arr[mid + 1]) {
            // Still climbing; peak is to the right
            left = mid + 1;
        } else {
            // Descending or at the peak
            right = mid;
        }
    }

    return left;
};
```

### Python
```python
class Solution:
    def peakIndexInMountainArray(self, arr):
        l, r = 0, len(arr)-1
        while l < r:
            m = (l+r)//2
            if arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m
        return l
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
- [845. Longest Mountain in Array](../../0501-1000/0875-longest-mountain-in-array/)
- [941. Valid Mountain Array](../../0501-1000/0978-valid-mountain-array/)
- [1095. Find in Mountain Array](../../1001-1500/1185-find-in-mountain-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/)
