# LeetCode 1442: Count Triplets That Can Form Two Arrays of Equal XOR

**LeetCode Problem #1442 — Count Triplets That Can Form Two Arrays of Equal XOR**
Solve LeetCode Count Triplets That Can Form Two Arrays of Equal XOR using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Triplets That Can Form Two Arrays of Equal XOR |
| LeetCode | #1442 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `arr`.

We want to select three indices `i`, `j` and `k` where `(0 <= i < j <= k < arr.length)`.

Let's define `a` and `b` as follows:

`a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]` 
 `b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]`

Note that **^** denotes the **bitwise-xor** operation.

Return *the number of triplets* (`i`, `j` and `k`) Where `a == b`.

## Constraints
- `1 <= arr.length <= 300`
- `1 <= arr[i] <= 10^8`

## Examples
### Example 1
- **Input:** `arr = [2,3,1,6,7]`
- **Output:** `4`
- **Explanation:** The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

### Example 2
- **Input:** `arr = [1,1,1,1,1]`
- **Output:** `10`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Count Triplets That Can Form Two Arrays of Equal XOR**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [2,3,1,6,7]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

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
from collections import defaultdict

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cnt = defaultdict(int)   # prefix value -> how many earlier indices
        total = defaultdict(int) # prefix value -> sum of those indices
        cnt[0] = 1               # p[0] = 0 at index 0
        total[0] = 0

        pref = 0
        ans = 0
        for m in range(1, len(arr) + 1):
            pref ^= arr[m - 1]
            ans += cnt[pref] * (m - 1) - total[pref]
            cnt[pref] += 1
            total[pref] += m

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
- [2791. Count Paths That Can Form a Palindrome in a Tree](../../2501-3000/2905-count-paths-that-can-form-a-palindrome-in-a-tree/)
- [1460. Make Two Arrays Equal by Reversing Subarrays](../../1501-2000/1556-make-two-arrays-equal-by-reversing-subarrays/)
- [1725. Number Of Rectangles That Can Form The Largest Square](../../1501-2000/1843-number-of-rectangles-that-can-form-the-largest-square/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)
