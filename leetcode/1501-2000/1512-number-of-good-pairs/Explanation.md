# LeetCode 1512: Number of Good Pairs

**LeetCode Problem #1512 — Number of Good Pairs**
Solve LeetCode Number of Good Pairs using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Good Pairs |
| LeetCode | #1512 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `nums`, return *the number of **good pairs***.

A pair `(i, j)` is called *good* if `nums[i] == nums[j]` and `i` < `j`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,1,1,3]`
- **Output:** `4`
- **Explanation:** There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

### Example 2
- **Input:** `nums = [1,1,1,1]`
- **Output:** `6`
- **Explanation:** Each pair in the array are *good*.

### Example 3
- **Input:** `nums = [1,2,3]`
- **Output:** `0`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Good Pairs**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,1,1,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

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
    def numIdenticalPairs(self, nums: list[int]) -> int:
        frequency = {}
        count = 0

        for num in nums:
            count += frequency.get(num, 0)
            frequency[num] = frequency.get(num, 0) + 1

        return count
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
- [1530. Number of Good Leaf Nodes Pairs](../../1501-2000/1530-number-of-good-leaf-nodes-pairs/)
- [1525. Number of Good Ways to Split a String](../../1501-2000/1525-number-of-good-ways-to-split-a-string/)
- [1987. Number of Unique Good Subsequences](../../1501-2000/1987-number-of-unique-good-subsequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-good-pairs/)
