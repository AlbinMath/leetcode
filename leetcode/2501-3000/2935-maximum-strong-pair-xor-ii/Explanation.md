# LeetCode 2935: Maximum Strong Pair XOR II

**LeetCode Problem #2935 — Maximum Strong Pair XOR II**
Solve LeetCode Maximum Strong Pair XOR II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Strong Pair XOR II |
| LeetCode | #2935 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums`. A pair of integers `x` and `y` is called a **strong** pair if it satisfies the condition:

`|x - y| <= min(x, y)`

You need to select two integers from `nums` such that they form a strong pair and their bitwise `XOR` is the **maximum** among all strong pairs in the array.

Return *the **maximum** *`XOR`* value out of all possible strong pairs in the array* `nums`.

**Note** that you can pick the same integer twice to form a pair.

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 2^20 - 1`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4,5]`
- **Output:** `7`
- **Explanation:** There are 11 strong pairs in the array `nums`: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
The maximum XOR possible from these pairs is 3 XOR 4 = 7.

### Example 2
- **Input:** `nums = [10,100]`
- **Output:** `0`
- **Explanation:** There are 2 strong pairs in the array nums: (10, 10) and (100, 100).
The maximum XOR possible from these pairs is 10 XOR 10 = 0 since the pair (100, 100) also gives 100 XOR 100 = 0.

### Example 3
- **Input:** `nums = [500,520,2500,3000]`
- **Output:** `1020`
- **Explanation:** There are 6 strong pairs in the array nums: (500, 500), (500, 520), (520, 520), (2500, 2500), (2500, 3000) and (3000, 3000).
The maximum XOR possible from these pairs is 500 XOR 520 = 1020 since the only other non-zero XOR value is 2500 XOR 3000 = 636.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Strong Pair XOR II**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4,5]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** There are 11 strong pairs in the array `nums`: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
The maximum XOR possible from these pairs is 3 XOR 4 = 7.

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
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = left = 0
        trie = {}

        def add(x, v):
            node = trie
            for b in range(20, -1, -1):
                bit = (x >> b) & 1
                node = node.setdefault(bit, {})
                node['#'] = node.get('#', 0) + v

        def query(x):
            node = trie
            res = 0
            for b in range(20, -1, -1):
                bit = (x >> b) & 1
                t = 1 - bit
                if t in node and node[t]['#'] > 0:
                    res |= 1 << b
                    node = node[t]
                else:
                    node = node[bit]
            return res

        for x in nums:
            add(x, 1)
            while nums[left] * 2 < x:
                add(nums[left], -1)
                left += 1
            ans = max(ans, query(x))
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
- [2932. Maximum Strong Pair XOR I](../../2501-3000/2932-maximum-strong-pair-xor-i/)
- [646. Maximum Length of Pair Chain](../../0501-1000/0646-maximum-length-of-pair-chain/)
- [1855. Maximum Distance Between a Pair of Values](../../1501-2000/1855-maximum-distance-between-a-pair-of-values/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-strong-pair-xor-ii/)
