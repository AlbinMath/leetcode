# LeetCode 165: Compare Version Numbers

**LeetCode Problem #165 — Compare Version Numbers**
Solve LeetCode Compare Version Numbers using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Compare Version Numbers |
| LeetCode | #165 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two **version strings**, `version1` and `version2`, compare them. A version string consists of **revisions** separated by dots `'.'`. The **value of the revision** is its **integer conversion** ignoring leading zeros.

To compare version strings, compare their revision values in **left-to-right order**. If one of the version strings has fewer revisions, treat the missing revision values as `0`.

Return the following:

If `version1 < version2`, return -1. 
 If `version1 > version2`, return 1. 
 Otherwise, return 0.

## Constraints
- `1 <= version1.length, version2.length <= 500`
- `version1` and `version2` only contain digits and `'.'`.
- `version1` and `version2` **are valid version numbers**.
- All the given revisions in `version1` and `version2` can be stored in a **32-bit integer**.

## Examples
### Example 1
- **Input:** `version1 = "1.2", version2 = "1.10"`
- **Output:** `-1`
- **Explanation:** version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

### Example 2
- **Input:** `version1 = "1.01", version2 = "1.001"`
- **Output:** `0`
- **Explanation:** Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

### Example 3
- **Input:** `version1 = "1.0", version2 = "1.0.0.0"`
- **Output:** `0`
- **Explanation:** version1 has less revisions, which means every missing revision are treated as "0".

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Compare Version Numbers**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `version1 = "1.2", version2 = "1.10"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `-1`.
4. **Verification:** version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

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
from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for a, b in zip_longest(version1.split('.'), version2.split('.'), fillvalue='0'):
            x, y = int(a), int(b)
            if x < y:
                return -1
            if x > y:
                return 1
        return 0
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
- [278. First Bad Version](../../0001-0500/0278-first-bad-version/)
- [844. Backspace String Compare](../../0501-1000/0844-backspace-string-compare/)
- [1170. Compare Strings by Frequency of the Smallest Character](../../1001-1500/1170-compare-strings-by-frequency-of-the-smallest-character/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/compare-version-numbers/)
