# LeetCode 3811: Number of Alternating XOR Partitions

**LeetCode Problem #3811 — Number of Alternating XOR Partitions**
Solve LeetCode Number of Alternating XOR Partitions using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Alternating XOR Partitions |
| LeetCode | #3811 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and two **distinct** integers `target1` and `target2`.

A **partition** of `nums` splits it into one or more **contiguous, non-empty** blocks that cover the entire array without overlap.

A partition is **valid** if the **bitwise XOR** of elements in its blocks **alternates** between `target1` and `target2`, starting with `target1`.

Formally, for blocks `b1`, `b2`, &hellip;:

`XOR(b1) = target1` 
 `XOR(b2) = target2` (if it exists) 
 `XOR(b3) = target1`, and so on.

Return the number of valid partitions of `nums`, modulo `10^9 + 7`.

**Note:** A single block is valid if its **XOR** equals `target1`.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i], target1, target2 <= 10^5`
- `target1 != target2`

## Examples
### Example 1
- **Input:** `nums = [2,3,1,4], target1 = 1, target2 = 5`
- **Output:** `1`
- **Explanation:** ​​​​​​​ 

 
 The XOR of `[2, 3]` is 1, which matches `target1`. 
 The XOR of the remaining block `[1, 4]` is 5, which matches `target2`. 
 This is the only valid alternating partition, so the answer is 1.

### Example 2
- **Input:** `nums = [1,0,0], target1 = 1, target2 = 0`
- **Output:** `3`

### Example 3
- **Input:** `nums = [7], target1 = 1, target2 = 7`
- **Output:** `0`
- **Explanation:** The XOR of `[7]` is 7, which does not match `target1`, so no valid partition exists.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Alternating XOR Partitions**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,3,1,4], target1 = 1, target2 = 5`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** ​​​​​​​ 

 
 The XOR of `[2, 3]` is 1, which matches `target1`. 
 The XOR of the remaining block `[1, 4]` is 5, which matches `target2`. 
 This is the only valid alternating partition, so the answer is 1.

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
    def alternatingXOR(self, nums, target1, target2):
        MOD = 10**9 + 7
        A = {0: 1}  # sums of dp2 (plus the empty prefix) by prefix xor
        B = {}      # sums of dp1 by prefix xor
        P = 0
        dp1 = dp2 = 0
        for x in nums:
            P ^= x
            dp1 = A.get(P ^ target1, 0)
            dp2 = B.get(P ^ target2, 0)
            A[P] = (A.get(P, 0) + dp2) % MOD
            B[P] = (B.get(P, 0) + dp1) % MOD
        return (dp1 + dp2) % MOD
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
- [2997. Minimum Number of Operations to Make Array XOR Equal to K](../../2501-3000/2997-minimum-number-of-operations-to-make-array-xor-equal-to-k/)
- [3513. Number of Unique XOR Triplets I](../../3501-4000/3513-number-of-unique-xor-triplets-i/)
- [3514. Number of Unique XOR Triplets II](../../3501-4000/3514-number-of-unique-xor-triplets-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-alternating-xor-partitions/)
