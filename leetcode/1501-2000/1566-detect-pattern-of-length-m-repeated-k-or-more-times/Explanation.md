# LeetCode 1566: Detect Pattern of Length M Repeated K or More Times

**LeetCode Problem #1566 — Detect Pattern of Length M Repeated K or More Times**
Solve LeetCode Detect Pattern of Length M Repeated K or More Times using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Detect Pattern of Length M Repeated K or More Times |
| LeetCode | #1566 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of positive integers `arr`, find a pattern of length `m` that is repeated `k` or more times.

A **pattern** is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times **consecutively **without overlapping. A pattern is defined by its length and the number of repetitions.

Return `true` *if there exists a pattern of length* `m` *that is repeated* `k` *or more times, otherwise return* `false`.

## Constraints
- `2 <= arr.length <= 100`
- `1 <= arr[i] <= 100`
- `1 <= m <= 100`
- `2 <= k <= 100`

## Examples
### Example 1
- **Input:** `arr = [1,2,4,4,4,4], m = 1, k = 3`
- **Output:** `true`
- **Explanation:** The pattern

### Example 2
- **Input:** `arr = [1,2,1,2,1,1,1,3], m = 2, k = 2`
- **Output:** `true`
- **Explanation:** The pattern

### Example 3
- **Input:** `arr = [1,2,1,2,1,3], m = 2, k = 3`
- **Output:** `false`
- **Explanation:** The pattern (1,2) is of length 2 but is repeated only 2 times. There is no pattern of length 2 that is repeated 3 or more times.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Detect Pattern of Length M Repeated K or More Times**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,4,4,4,4], m = 1, k = 3`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The pattern

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
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        n = len(arr)

        for i in range(n - m * k + 1):
            count = 0

            for j in range(m * (k - 1)):
                if arr[i + j] == arr[i + j + m]:
                    count += 1
                else:
                    break

            if count == m * (k - 1):
                return True

        return False
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
- [2014. Longest Subsequence Repeated k Times](../../2001-2500/2014-longest-subsequence-repeated-k-times/)
- [3473. Sum of K Subarrays With Length at Least M](../../3001-3500/3473-sum-of-k-subarrays-with-length-at-least-m/)
- [1415. The k-th Lexicographical String of All Happy Strings of Length n](../../1001-1500/1415-the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/)
