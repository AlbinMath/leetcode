# LeetCode 3267: Count Almost Equal Pairs II

**LeetCode Problem #3267 — Count Almost Equal Pairs II**
Solve LeetCode Count Almost Equal Pairs II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Almost Equal Pairs II |
| LeetCode | #3267 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
**Attention**: In this version, the number of operations that can be performed, has been increased to **twice**.

You are given an array `nums` consisting of positive integers.

We call two integers `x` and `y` **almost equal** if both integers can become equal after performing the following operation **at most twice **:

Choose **either** `x` or `y` and swap any two digits within the chosen number.

Return the number of indices `i` and `j` in `nums` where `i < j` such that `nums[i]` and `nums[j]` are **almost equal**.

**Note** that it is allowed for an integer to have leading zeros after performing an operation.

## Constraints
- `2 <= nums.length <= 5000`
- `1 <= nums[i] < 10^7`

## Examples
### Example 1
- **Input:** `nums = [1023,2310,2130,213]`
- **Output:** `4`
- **Explanation:** The almost equal pairs of elements are: 

 
 1023 and 2310. By swapping the digits 1 and 2, and then the digits 0 and 3 in 1023, you get 2310. 
 1023 and 213. By swapping the digits 1 and 0, and then the digits 1 and 2 in 1023, you get 0213, which is 213. 
 2310 and 213. By swapping the digits 2 and 0, and then the digits 3 and 2 in 2310, you get 0213, which is 213. 
 2310 and 2130. By swapping the digits 3 and 1 in 2310, you get 2130.

### Example 2
- **Input:** `nums = [1,10,100]`
- **Output:** `3`
- **Explanation:** The almost equal pairs of elements are: 

 
 1 and 10. By swapping the digits 1 and 0 in 10, you get 01 which is 1. 
 1 and 100. By swapping the second 0 with the digit 1 in 100, you get 001, which is 1. 
 10 and 100. By swapping the first 0 with the digit 1 in 100, you get 010, which is 10.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Almost Equal Pairs II**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1023,2310,2130,213]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The almost equal pairs of elements are: 

 
 1023 and 2310. By swapping the digits 1 and 2, and then the digits 0 and 3 in 1023, you get 2310. 
 1023 and 213. By swapping the digits 1 and 0, and then the digits 1 and 2 in 1023, you get 0213, which is 213. 
 2310 and 213. By swapping the digits 2 and 0, and then the digits 3 and 2 in 2310, you get 0213, which is 213. 
 2310 and 2130. By swapping the digits 3 and 1 in 2310, you get 2130.

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
from typing import List
from collections import Counter

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        L = len(str(max(nums)))
        cnt = Counter()
        ans = 0

        for x in nums:
            s = str(x).zfill(L)
            reach = {s}
            lst = list(s)

            for i in range(L):
                for j in range(i + 1, L):
                    lst[i], lst[j] = lst[j], lst[i]
                    reach.add(''.join(lst))
                    for p in range(L):
                        for q in range(p + 1, L):
                            lst[p], lst[q] = lst[q], lst[p]
                            reach.add(''.join(lst))
                            lst[p], lst[q] = lst[q], lst[p]
                    lst[i], lst[j] = lst[j], lst[i]

            for r in reach:
                ans += cnt[r]
            cnt[s] += 1

        return ans
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
- [3265. Count Almost Equal Pairs I](../../3501-4000/3534-count-almost-equal-pairs-i/)
- [4043. Count Rotations With Exactly K Equal Adjacent Pairs](../../4001-4500/4411-count-rotations-with-exactly-k-equal-adjacent-pairs/)
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1501-2000/1553-count-triplets-that-can-form-two-arrays-of-equal-xor/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-almost-equal-pairs-ii/)
