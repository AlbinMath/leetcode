# LeetCode 347: Top K Frequent Elements

**LeetCode Problem #347 — Top K Frequent Elements**
Solve LeetCode Top K Frequent Elements using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n log n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Top K Frequent Elements |
| LeetCode | #347 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n log n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

## Examples
### Example 1
- **Input:** `nums = [1,1,1,2,2,3], k = 2`
- **Output:** `[1,2]`

### Example 2
- **Input:** `nums = [1], k = 1`
- **Output:** `[1]`

### Example 3
- **Input:** `nums = [1,2,1,2,1,2,3,1,3,2], k = 2`
- **Output:** `[1,2]`

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Top K Frequent Elements**, we observe the problem requirements and utilize the **Binary Search** technique. By maintaining a **Sorted Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Sorted Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,1,1,2,2,3], k = 2`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.

## Complexity Analysis
- **Time Complexity:** O(n log n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result

        return result
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
- [692. Top K Frequent Words](../../0501-1000/0692-top-k-frequent-words/)
- [2512. Reward Top K Students](../../2501-3000/2512-reward-top-k-students/)
- [3070. Count Submatrices with Top-Left Element and Sum Less Than k](../../3001-3500/3070-count-submatrices-with-top-left-element-and-sum-less-than-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)
