# LeetCode 3753: Total Waviness of Numbers in Range II

**LeetCode Problem #3753 — Total Waviness of Numbers in Range II**
Solve LeetCode Total Waviness of Numbers in Range II using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Total Waviness of Numbers in Range II |
| LeetCode | #3753 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers `num1` and `num2` representing an **inclusive** range `[num1, num2]`.

The **waviness** of a number is defined as the total count of its **peaks** and **valleys**:

A digit is a **peak** if it is **strictly greater** than both of its immediate neighbors. 
 A digit is a **valley** if it is **strictly less** than both of its immediate neighbors. 
 The first and last digits of a number **cannot** be peaks or valleys. 
 Any number with fewer than 3 digits has a waviness of 0. 
 
Return the total sum of waviness for all numbers in the range `[num1, num2]`.

## Constraints
- `1 <= num1 <= num2 <= 10^15`​​​​​​​

## Examples
### Example 1
- **Input:** `num1 = 120, num2 = 130`
- **Output:** `3`
- **Explanation:** In the range `[120, 130]`: 

 
 `120`: middle digit 2 is a peak, waviness = 1. 
 `121`: middle digit 2 is a peak, waviness = 1. 
 `130`: middle digit 3 is a peak, waviness = 1. 
 All other numbers in the range have a waviness of 0. 
 

 Thus, total waviness is `1 + 1 + 1 = 3`.

### Example 2
- **Input:** `num1 = 198, num2 = 202`
- **Output:** `3`
- **Explanation:** In the range `[198, 202]`: 

 
 `198`: middle digit 9 is a peak, waviness = 1. 
 `201`: middle digit 0 is a valley, waviness = 1. 
 `202`: middle digit 0 is a valley, waviness = 1. 
 All other numbers in the range have a waviness of 0. 
 

 Thus, total waviness is `1 + 1 + 1 = 3`.

### Example 3
- **Input:** `num1 = 4848, num2 = 4848`
- **Output:** `2`
- **Explanation:** Number `4848`: the second digit 8 is a peak, and the third digit 4 is a valley, giving a waviness of 2.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Total Waviness of Numbers in Range II**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num1 = 120, num2 = 130`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** In the range `[120, 130]`: 

 
 `120`: middle digit 2 is a peak, waviness = 1. 
 `121`: middle digit 2 is a peak, waviness = 1. 
 `130`: middle digit 3 is a peak, waviness = 1. 
 All other numbers in the range have a waviness of 0. 
 

 Thus, total waviness is `1 + 1 + 1 = 3`.

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

    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n):
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            # State:
            # (tight, started, prevPrev, prev)
            #
            # value = (number of ways, total waviness)
            #
            # prevPrev = -1 means we don't have two previous
            # digits yet.
            dp = {
                (True, False, -1, -1): (1, 0)
            }

            for pos in range(m):
                ndp = {}

                for (tight, started, pp, p), (ways, total) in dp.items():

                    limit = digits[pos] if tight else 9

                    for d in range(limit + 1):

                        ntight = tight and (d == limit)

                        # Still skipping leading zeros
                        if not started and d == 0:
                            key = (ntight, False, -1, -1)

                            oldWays, oldTotal = ndp.get(key, (0, 0))
                            ndp[key] = (
                                oldWays + ways,
                                oldTotal + total
                            )
                            continue

                        # First real digit
                        if not started:
                            key = (ntight, True, -1, d)

                            oldWays, oldTotal = ndp.get(key, (0, 0))
                            ndp[key] = (
                                oldWays + ways,
                                oldTotal + total
                            )
                            continue

                        # We have only one previous digit.
                        if pp == -1:
                            key = (ntight, True, p, d)

                            oldWays, oldTotal = ndp.get(key, (0, 0))
                            ndp[key] = (
                                oldWays + ways,
                                oldTotal + total
                            )
                            continue

                        # We now have:
                        #
                        # pp, p, d
                        #
                        # p is a peak if p > pp and p > d
                        # p is a valley if p < pp and p < d

                        add = 0

                        if (p > pp and p > d) or \
                           (p < pp and p < d):
                            add = 1

                        key = (ntight, True, p, d)

                        oldWays, oldTotal = ndp.get(key, (0, 0))

                        ndp[key] = (
                            oldWays + ways,
                            oldTotal + total + ways * add
                        )

                dp = ndp

            # Sum waviness over all numbers <= n.
            answer = 0

            for (tight, started, pp, p), (ways, total) in dp.items():
                answer += total

            return answer

        return solve(num2) - solve(num1 - 1)
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
- [3751. Total Waviness of Numbers in Range I](../../4001-4500/4057-total-waviness-of-numbers-in-range-i/)
- [201. Bitwise AND of Numbers Range](../../0001-0500/0201-bitwise-and-of-numbers-range/)
- [1523. Count Odd Numbers in an Interval Range](../../1501-2000/1630-count-odd-numbers-in-an-interval-range/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/)
