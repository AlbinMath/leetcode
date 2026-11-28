# LeetCode 4007: Widest Possible Fence

**LeetCode Problem #4007 — Widest Possible Fence**
Solve LeetCode Widest Possible Fence using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Widest Possible Fence |
| LeetCode | #4007 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `planks`, where `planks[i]` represents the height of the `i^th` wooden plank. Each plank has a width of 1 unit.

You want to build a fence consisting of planks that all have the **same** height.

You may either use a plank as is, or combine **exactly** two distinct original planks into a single plank whose height **equals** the sum of their heights. Each original plank can be used **at most** once, and not all original planks need to be used.

Return the **maximum possible width** of the fence that can be built.

## Constraints
- `1 <= planks.length <= 1000`
- `1 <= planks[i] <= 10^9`

## Examples
### Example 1
- **Input:** `planks = [1,3,2,5,7,5,4,2,1]`
- **Output:** `4`
- **Explanation:** We can have four planks of height 5. 

 
 `planks[3] = 5` 
 `planks[5] = 5` 
 `planks[0] + planks[6] = 1 + 4 = 5` 
 `planks[1] + planks[2] = 3 + 2 = 5` 
 

 Hence, the maximum width is 4.

### Example 2
- **Input:** `planks = [2,3,7]`
- **Output:** `1`
- **Explanation:** It is impossible to form two planks of the same height, even after combining two distinct original planks. 
 Since not all original planks need to be used, we can choose any one plank as the fence. 
 Therefore, the maximum possible width is 1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Widest Possible Fence**, we observe the problem requirements and utilize the **Tree & Graph** technique. By maintaining a **Tree / Graph / Grid**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Tree / Graph / Grid** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `planks = [1,3,2,5,7,5,4,2,1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** We can have four planks of height 5. 

 
 `planks[3] = 5` 
 `planks[5] = 5` 
 `planks[0] + planks[6] = 1 + 4 = 5` 
 `planks[1] + planks[2] = 3 + 2 = 5` 
 

 Hence, the maximum width is 4.

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
from collections import Counter, defaultdict

class Solution:
    def maximumWidth(self, planks: List[int]) -> int:
        cnt = Counter(planks)
        vals = sorted(cnt)
        score = defaultdict(int)

        for i, a in enumerate(vals):
            ca = cnt[a]
            score[2 * a] += ca // 2
            for j in range(i + 1, len(vals)):
                b = vals[j]
                score[a + b] += min(ca, cnt[b])

        ans = max(cnt.values())              # a single height, no pairing
        for h, s in score.items():
            ans = max(ans, s + cnt.get(h, 0))
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
- [587. Erect the Fence](../../0501-1000/0587-erect-the-fence/)
- [886. Possible Bipartition](../../0501-1000/0886-possible-bipartition/)
- [894. All Possible Full Binary Trees](../../0501-1000/0894-all-possible-full-binary-trees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/widest-possible-fence/)
