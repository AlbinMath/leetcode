# LeetCode 2006: Count Number of Pairs With Absolute Difference K

**LeetCode Problem #2006 — Count Number of Pairs With Absolute Difference K**
Solve LeetCode Count Number of Pairs With Absolute Difference K using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Number of Pairs With Absolute Difference K |
| LeetCode | #2006 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `nums` and an integer `k`, return *the number of pairs* `(i, j)` *where* `i < j` *such that* `|nums[i] - nums[j]| == k`.

The value of `|x|` is defined as:

`x` if `x >= 0`. 
 `-x` if `x < 0`.

## Constraints
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`
- `1 <= k <= 99`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,1], k = 1`
- **Output:** `4`
- **Explanation:** The pairs with an absolute difference of 1 are:
- [

### Example 2
- **Input:** `nums = [1,3], k = 3`
- **Output:** `0`
- **Explanation:** There are no pairs with an absolute difference of 3.

### Example 3
- **Input:** `nums = [3,2,1,5,4], k = 2`
- **Output:** `3`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Number of Pairs With Absolute Difference K**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,1], k = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The pairs with an absolute difference of 1 are:
- [

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
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        freq = {}
        pairs = 0
        
        for num in nums:
            pairs += freq.get(num - k, 0) + freq.get(num + k, 0)
            freq[num] = freq.get(num, 0) + 1
            
        return pairs
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
- [3774. Absolute Difference Between Maximum and Minimum K Elements](../../3501-4000/3774-absolute-difference-between-maximum-and-minimum-k-elements/)
- [1679. Max Number of K-Sum Pairs](../../1501-2000/1679-max-number-of-k-sum-pairs/)
- [2183. Count Array Pairs Divisible by K](../../2001-2500/2183-count-array-pairs-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/)
