# LeetCode 2442: Count Number of Distinct Integers After Reverse Operations

**LeetCode Problem #2442 — Count Number of Distinct Integers After Reverse Operations**
Solve LeetCode Count Number of Distinct Integers After Reverse Operations using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Distinct Integers After Reverse Operations |
| LeetCode | #2442 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array `nums` consisting of **positive** integers.

You have to take each integer in the array, **reverse its digits**, and add it to the end of the array. You should apply this operation to the original integers in `nums`.

Return *the number of **distinct** integers in the final array*.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,13,10,12,31]`
- **Output:** `6`
- **Explanation:** After including the reverse of each number, the resulting array is [1,13,10,12,31, 1,31,1,21,13 ].
The reversed integers that were added to the end of the array are underlined. Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).

### Example 2
- **Input:** `nums = [2,2,2]`
- **Output:** `1`
- **Explanation:** After including the reverse of each number, the resulting array is [2,2,2, 2,2,2 ].
The number of distinct integers in this array is 1 (The number 2).

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Number of Distinct Integers After Reverse Operations**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,13,10,12,31]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** After including the reverse of each number, the resulting array is [1,13,10,12,31, 1,31,1,21,13 ].
The reversed integers that were added to the end of the array are underlined. Note that for the integer 10, after reversing it, it becomes 01 which is just 1.
The number of distinct integers in this array is 6 (The numbers 1, 10, 12, 13, 21, and 31).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        distinct = set(nums)
        
        for num in list(distinct):
            rev = 0
            temp = num
            while temp > 0:
                rev = rev * 10 + temp % 10
                temp //= 10
            distinct.add(rev)
            
        return len(distinct)
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1481. Least Number of Unique Integers after K Removals](../../1001-1500/1481-least-number-of-unique-integers-after-k-removals/)
- [3859. Count Subarrays With K Distinct Integers](../../3501-4000/3859-count-subarrays-with-k-distinct-integers/)
- [3569. Maximize Count of Distinct Primes After Split](../../3501-4000/3569-maximize-count-of-distinct-primes-after-split/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/)
