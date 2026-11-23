# LeetCode 677: Map Sum Pairs

**LeetCode Problem #677 — Map Sum Pairs**
Solve LeetCode Map Sum Pairs using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Map Sum Pairs |
| LeetCode | #677 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design a map that allows you to do the following:

Maps a string key to a given value. 
 Returns the sum of the values that have a key with a prefix equal to a given string.

Implement the `MapSum` class:

`MapSum()` Initializes the `MapSum` object. 
 `void insert(String key, int val)` Inserts the `key-val` pair into the map. If the `key` already existed, the original `key-value` pair will be overridden to the new one. 
 `int sum(string prefix)` Returns the sum of all the pairs' value whose `key` starts with the `prefix`.

## Constraints
- `1 <= key.length, prefix.length <= 50`
- `key` and `prefix` consist of only lowercase English letters.
- `1 <= val <= 1000`
- At most `50` calls will be made to `insert` and `sum`.

## Examples
### Example 1
- **Input:** `["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]`
- **Output:** `[null, null, 3, null, 5]`
- **Explanation:** MapSum mapSum = new MapSum();
mapSum.insert("apple", 3); 
mapSum.sum("ap"); // return 3 ( ap ple = 3)
mapSum.insert("app", 2); 
mapSum.sum("ap"); // return 5 ( ap ple + ap p = 3 + 2 = 5)

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Map Sum Pairs**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, 3, null, 5]`.
4. **Verification:** MapSum mapSum = new MapSum();
mapSum.insert("apple", 3); 
mapSum.sum("ap"); // return 3 ( ap ple = 3)
mapSum.insert("app", 2); 
mapSum.sum("ap"); // return 5 ( ap ple + ap p = 3 + 2 = 5)

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
class MapSum:

    def __init__(self):
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        return sum(v for k, v in self.d.items() if k.startswith(prefix))
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
- [1679. Max Number of K-Sum Pairs](../../1501-2000/1798-max-number-of-k-sum-pairs/)
- [1835. Find XOR Sum of All Pairs Bitwise AND](../../1501-2000/1963-find-xor-sum-of-all-pairs-bitwise-and/)
- [1862. Sum of Floored Pairs](../../1001-1500/1326-sum-of-floored-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/map-sum-pairs/)
