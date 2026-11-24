# LeetCode 2980: Check if Bitwise OR Has Trailing Zeros

**LeetCode Problem #2980 — Check if Bitwise OR Has Trailing Zeros**
Solve LeetCode Check if Bitwise OR Has Trailing Zeros using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if Bitwise OR Has Trailing Zeros |
| LeetCode | #2980 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of **positive** integers `nums`.

You have to check if it is possible to select **two or more** elements in the array such that the bitwise `OR` of the selected elements has **at least **one trailing zero in its binary representation.

For example, the binary representation of `5`, which is `"101"`, does not have any trailing zeros, whereas the binary representation of `4`, which is `"100"`, has two trailing zeros.

Return `true` *if it is possible to select two or more elements whose bitwise* `OR` *has trailing zeros, return* `false` *otherwise*.

## Constraints
- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `true`
- **Explanation:** If we select the elements 2 and 4, their bitwise OR is 6, which has the binary representation "110" with one trailing zero.

### Example 2
- **Input:** `nums = [2,4,8,16]`
- **Output:** `true`
- **Explanation:** If we select the elements 2 and 4, their bitwise OR is 6, which has the binary representation "110" with one trailing zero.
Other possible ways to select elements to have trailing zeroes in the binary representation of their bitwise OR are: (2, 8), (2, 16), (4, 8), (4, 16), (8, 16), (2, 4, 8), (2, 4, 16), (2, 8, 16), (4, 8, 16), and (2, 4, 8, 16).

### Example 3
- **Input:** `nums = [1,3,5,7,9]`
- **Output:** `false`
- **Explanation:** There is no possible way to select two or more elements to have trailing zeros in the binary representation of their bitwise OR.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Check if Bitwise OR Has Trailing Zeros**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** If we select the elements 2 and 4, their bitwise OR is 6, which has the binary representation "110" with one trailing zero.

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
class Solution(object):
    def hasTrailingZeros(self, nums):
        return sum(1 for x in nums if x % 2 == 0) >= 2
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
- [1784. Check if Binary String Has at Most One Segment of Ones](../../1501-2000/1784-check-if-binary-string-has-at-most-one-segment-of-ones/)
- [2283. Check if Number Has Equal Digit Count and Digit Value](../../2001-2500/2283-check-if-number-has-equal-digit-count-and-digit-value/)
- [3591. Check if Any Element Has Prime Frequency](../../3501-4000/3591-check-if-any-element-has-prime-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/)
