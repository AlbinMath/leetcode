# LeetCode 1577: Number of Ways Where Square of Number Is Equal to Product of Two Numbers

**LeetCode Problem #1577 — Number of Ways Where Square of Number Is Equal to Product of Two Numbers**
Solve LeetCode Number of Ways Where Square of Number Is Equal to Product of Two Numbers using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Ways Where Square of Number Is Equal to Product of Two Numbers |
| LeetCode | #1577 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two arrays of integers `nums1` and `nums2`, return the number of triplets formed (type 1 and type 2) under the following rules:

Type 1: Triplet (i, j, k) if `nums1[i]^2 == nums2[j] * nums2[k]` where `0 <= i < nums1.length` and `0 <= j < k < nums2.length`. 
 Type 2: Triplet (i, j, k) if `nums2[i]^2 == nums1[j] * nums1[k]` where `0 <= i < nums2.length` and `0 <= j < k < nums1.length`.

## Constraints
- `1 <= nums1.length, nums2.length <= 1000`
- `1 <= nums1[i], nums2[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums1 = [7,4], nums2 = [5,2,8,9]`
- **Output:** `1`
- **Explanation:** Type 1: (1, 1, 2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8).

### Example 2
- **Input:** `nums1 = [1,1], nums2 = [1,1,1]`
- **Output:** `9`
- **Explanation:** All Triplets are valid, because 1^2 = 1 * 1.
Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2). nums1[i]^2 = nums2[j] * nums2[k].
Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].

### Example 3
- **Input:** `nums1 = [7,7,8,3], nums2 = [1,2,9,7]`
- **Output:** `2`
- **Explanation:** There are 2 valid triplets.
Type 1: (3,0,2). nums1[3]^2 = nums2[0] * nums2[2].
Type 2: (3,0,1). nums2[3]^2 = nums1[0] * nums1[1].

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Ways Where Square of Number Is Equal to Product of Two Numbers**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums1 = [7,4], nums2 = [5,2,8,9]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Type 1: (1, 1, 2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter, defaultdict
from typing import List

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count_triplets(squares_arr: List[int], products_arr: List[int]) -> int:
            total = 0
            square_counts = Counter(squares_arr)
            
            for x, freq in square_counts.items():
                target = x * x
                seen = defaultdict(int)
                pairs = 0
                
                for y in products_arr:
                    if target % y == 0:
                        pairs += seen[target // y]
                    seen[y] += 1
                    
                total += freq * pairs
                
            return total

        return count_triplets(nums1, nums2) + count_triplets(nums2, nums1)
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [1977. Number of Ways to Separate Numbers](../../1501-2000/1977-number-of-ways-to-separate-numbers/)
- [3566. Partition Array into Two Equal Product Subsets](../../3501-4000/3566-partition-array-into-two-equal-product-subsets/)
- [3226. Number of Bit Changes to Make Two Integers Equal](../../3001-3500/3226-number-of-bit-changes-to-make-two-integers-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/)
