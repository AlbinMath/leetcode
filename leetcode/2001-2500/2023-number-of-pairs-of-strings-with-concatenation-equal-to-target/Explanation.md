# LeetCode 2023: Number of Pairs of Strings With Concatenation Equal to Target

**LeetCode Problem #2023 — Number of Pairs of Strings With Concatenation Equal to Target**
Solve LeetCode Number of Pairs of Strings With Concatenation Equal to Target using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Pairs of Strings With Concatenation Equal to Target |
| LeetCode | #2023 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of **digit** strings `nums` and a **digit** string `target`, return *the number of pairs of indices *`(i, j)`* (where *`i != j`*) such that the **concatenation** of *`nums[i] + nums[j]`* equals *`target`.

## Constraints
- `2 <= nums.length <= 100`
- `1 <= nums[i].length <= 100`
- `2 <= target.length <= 100`
- `nums[i]` and `target` consist of digits.
- `nums[i]` and `target` do not have leading zeros.

## Examples
### Example 1
- **Input:** `nums = ["777","7","77","77"], target = "7777"`
- **Output:** `4`
- **Explanation:** Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"

### Example 2
- **Input:** `nums = ["123","4","12","34"], target = "1234"`
- **Output:** `2`
- **Explanation:** Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"

### Example 3
- **Input:** `nums = ["1","1","1"], target = "11"`
- **Output:** `6`
- **Explanation:** Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Pairs of Strings With Concatenation Equal to Target**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = ["777","7","77","77"], target = "7777"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"

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
from collections import Counter

class Solution:
    def numOfPairs(self, nums: list[str], target: str) -> int:
        freq = Counter(nums)
        pairs = 0
        target_len = len(target)
        
        for prefix, count in freq.items():
            if len(prefix) < target_len and target.startswith(prefix):
                suffix = target[len(prefix):]
                if suffix in freq:
                    if prefix == suffix:
                        pairs += count * (count - 1)
                    else:
                        pairs += count * freq[suffix]
                        
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
- [3291. Minimum Number of Valid Strings to Form Target I](../../3001-3500/3291-minimum-number-of-valid-strings-to-form-target-i/)
- [3292. Minimum Number of Valid Strings to Form Target II](../../3001-3500/3292-minimum-number-of-valid-strings-to-form-target-ii/)
- [3309. Maximum Possible Number by Binary Concatenation](../../3001-3500/3309-maximum-possible-number-by-binary-concatenation/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/)
