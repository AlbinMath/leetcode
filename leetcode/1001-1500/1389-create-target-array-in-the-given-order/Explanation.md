# LeetCode 1389: Create Target Array in the Given Order

**LeetCode Problem #1389 — Create Target Array in the Given Order**
Solve LeetCode Create Target Array in the Given Order using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Create Target Array in the Given Order |
| LeetCode | #1389 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two arrays of integers `nums` and `index`. Your task is to create *target* array under the following rules:

Initially *target* array is empty. 
 From left to right read nums[i] and index[i], insert at index `index[i]` the value `nums[i]` in *target* array. 
 Repeat the previous step until there are no elements to read in `nums` and `index.`

Return the *target* array.

It is guaranteed that the insertion operations will be valid.

## Constraints
- `1 <= nums.length, index.length <= 100`
- `nums.length == index.length`
- `0 <= nums[i] <= 100`
- `0 <= index[i] <= i`

## Examples
### Example 1
- **Input:** `nums = [0,1,2,3,4], index = [0,1,2,2,1]`
- **Output:** `[0,4,1,3,2]`
- **Explanation:** nums index target
0 0 [0]
1 1 [0,1]
2 2 [0,1,2]
3 2 [0,1,3,2]
4 1 [0,4,1,3,2]

### Example 2
- **Input:** `nums = [1,2,3,4,0], index = [0,1,2,3,0]`
- **Output:** `[0,1,2,3,4]`
- **Explanation:** nums index target
1 0 [1]
2 1 [1,2]
3 2 [1,2,3]
4 3 [1,2,3,4]
0 0 [0,1,2,3,4]

### Example 3
- **Input:** `nums = [1], index = [0]`
- **Output:** `[1]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Create Target Array in the Given Order**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,2,3,4], index = [0,1,2,2,1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,4,1,3,2]`.
4. **Verification:** nums index target
0 0 [0]
1 1 [0,1]
2 2 [0,1,2]
3 2 [0,1,3,2]
4 1 [0,4,1,3,2]

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
    def createTargetArray(
        self, nums: list[int], index: list[int]
    ) -> list[int]:
        target = []

        for i in range(len(nums)):
            target.insert(index[i], nums[i])

        return target
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
- [1639. Number of Ways to Form a Target String Given a Dictionary](../../1501-2000/1639-number-of-ways-to-form-a-target-string-given-a-dictionary/)
- [1802. Maximum Value at a Given Index in a Bounded Array](../../1501-2000/1802-maximum-value-at-a-given-index-in-a-bounded-array/)
- [1982. Find Array Given Subset Sums](../../1501-2000/1982-find-array-given-subset-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/create-target-array-in-the-given-order/)
