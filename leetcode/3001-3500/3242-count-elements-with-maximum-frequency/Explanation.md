# LeetCode 3005: Count Elements With Maximum Frequency

**LeetCode Problem #3005 — Count Elements With Maximum Frequency**
Solve LeetCode Count Elements With Maximum Frequency using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Elements With Maximum Frequency |
| LeetCode | #3005 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `nums` consisting of **positive** integers.

Return *the **total frequencies** of elements in** *`nums` *such that those elements all have the **maximum** frequency*.

The **frequency** of an element is the number of occurrences of that element in the array.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,3,1,4]`
- **Output:** `4`
- **Explanation:** The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

### Example 2
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `5`
- **Explanation:** All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Elements With Maximum Frequency**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,3,1,4]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

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
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq = [0] * 101
        max_freq = 0
        total = 0
        
        for num in nums:
            freq[num] += 1
            count = freq[num]
            
            if count > max_freq:
                max_freq = count
                total = count
            elif count == max_freq:
                total += count
                
        return total
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
- [895. Maximum Frequency Stack](../../0501-1000/0931-maximum-frequency-stack/)
- [3325. Count Substrings With K-Frequency Characters I](../../3501-4000/3502-count-substrings-with-k-frequency-characters-i/)
- [3346. Maximum Frequency of an Element After Performing Operations I](../../3501-4000/3622-maximum-frequency-of-an-element-after-performing-operations-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-elements-with-maximum-frequency/)
