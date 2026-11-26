# LeetCode 659: Split Array into Consecutive Subsequences

**LeetCode Problem #659 — Split Array into Consecutive Subsequences**
Solve LeetCode Split Array into Consecutive Subsequences using Python and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split Array into Consecutive Subsequences |
| LeetCode | #659 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` that is **sorted in non-decreasing order**.

Determine if it is possible to split `nums` into **one or more subsequences** such that **both** of the following conditions are true:

Each subsequence is a **consecutive increasing sequence** (i.e. each integer is **exactly one** more than the previous integer). 
 All subsequences have a length of `3`** or more**.

Return `true`* if you can split *`nums`* according to the above conditions, or *`false`* otherwise*.

A **subsequence** of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., `[1,3,5]` is a subsequence of `[ 1 ,2, 3 ,4, 5 ]` while `[1,3,2]` is not).

## Constraints
- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`
- `nums` is sorted in **non-decreasing** order.

## Examples
### Example 1
- **Input:** `nums = [1,2,3,3,4,5]`
- **Output:** `true`
- **Explanation:** nums can be split into the following subsequences:
[

### Example 2
- **Input:** `nums = [1,2,3,3,4,4,5,5]`
- **Output:** `true`
- **Explanation:** nums can be split into the following subsequences:
[

### Example 3
- **Input:** `nums = [1,2,3,4,4,5]`
- **Output:** `false`
- **Explanation:** It is impossible to split nums into consecutive increasing subsequences of length 3 or more.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Split Array into Consecutive Subsequences**, we observe the problem requirements and utilize the **Dynamic Programming** technique. By maintaining a **DP Table / Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **DP Table / Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,3,4,5]`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** nums can be split into the following subsequences:
[

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter, defaultdict
from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        need = defaultdict(int)
        
        for num in nums:
            if freq[num] == 0:
                continue
            if need[num] > 0:
                need[num] -= 1
                need[num + 1] += 1
                freq[num] -= 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] += 1
            else:
                return False
                
        return True
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0842-split-array-into-fibonacci-sequence/)
- [1712. Ways to Split Array Into Three Subarrays](../../1501-2000/1712-ways-to-split-array-into-three-subarrays/)
- [2871. Split Array Into Maximum Number of Subarrays](../../2501-3000/2871-split-array-into-maximum-number-of-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)
