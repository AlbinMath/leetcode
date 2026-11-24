# LeetCode 3953: Maximum Score with Co-Prime Element

**LeetCode Problem #3953 — Maximum Score with Co-Prime Element**
Solve LeetCode Maximum Score with Co-Prime Element using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Score with Co-Prime Element |
| LeetCode | #3953 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n` and an integer `maxVal`.

You **may** change any element in `nums` to any positive integer **less than or equal** to `maxVal`. Each such change costs 1.

Two integers are **co-prime** if their **greatest common divisor (GCD)** is 1.

After all modifications, you **must** choose an index `i` such that, `nums[i]` is **co-prime** with every other element `nums[j]`.

`selectedValue` be the final value of `nums[i]` after modifications. 
 `modificationCost` be the total number of elements changed.

The score is defined as `score = selectedValue - modificationCost`.

Return the **maximum** possible score.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= maxVal <= 10^​​​​​​​5`

## Examples
### Example 1
- **Input:** `nums = [3,4,6], maxVal = 5`
- **Output:** `4`
- **Explanation:** Change `nums[2]` from 6 to 5, which costs 1. Choose `nums[2] = 5`, since it is co-prime with 3 and 4. 

 
 `selectedValue = 5` 
 `modificationCost = 1` 
 The score is `5 - 1 = 4`

### Example 2
- **Input:** `nums = [1,2,3], maxVal = 4`
- **Output:** `3`
- **Explanation:** No modifications are required. Choose `nums[2] = 3`, since it is co-prime with 1 and 2. 

 
 `selectedValue = 3` 
 `modificationCost = 0` 
 The score is `3 - 0 = 3`

### Example 3
- **Input:** `nums = [2,2], maxVal = 1`
- **Output:** `1`
- **Explanation:** Change `nums[0]` from 2 to 1, which costs 1. Choose `nums[1] = 2`, since it is co-prime with 1. 

 
 `selectedValue = 2` 
 `modificationCost = 1` 
 The score is ​​​​​​​`2 - 1 = 1`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Score with Co-Prime Element**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,4,6], maxVal = 5`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** Change `nums[2]` from 6 to 5, which costs 1. Choose `nums[2] = 5`, since it is co-prime with 3 and 4. 

 
 `selectedValue = 5` 
 `modificationCost = 1` 
 The score is `5 - 1 = 4`

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int maxScore(vector<int>& nums, int maxVal) {
        int n = nums.size();
        int M = max(maxVal, *max_element(nums.begin(), nums.end()));

        vector<int> freq(M + 1);
        for (int x : nums) freq[x]++;

        vector<int> mu(M + 1), lp(M + 1), primes;
        mu[1] = 1;
        for (int i = 2; i <= M; i++) {
            if (lp[i] == 0) {
                lp[i] = i;
                primes.push_back(i);
                mu[i] = -1;
            }
            for (int p : primes) {
                long long v = 1LL * i * p;
                if (v > M) break;
                lp[v] = p;
                if (i % p == 0) {
                    mu[v] = 0;
                    break;
                } else {
                    mu[v] = -mu[i];
                }
            }
        }

        vector<int> multCnt(M + 1);
        for (int d = 1; d <= M; d++) {
            for (int k = d; k <= M; k += d) {
                multCnt[d] += freq[k];
            }
        }

        vector<int> cop(M + 1);
        for (int d = 1; d <= M; d++) {
            if (mu[d] == 0) continue;
            int add = mu[d] * multCnt[d];
            for (int x = d; x <= M; x += d) {
                cop[x] += add;
            }
        }

        int ans = 0;

        for (int x = 1; x <= M; x++) {
            int bad = n - cop[x];

            if (freq[x] > 0) {
                if (x == 1) ans = max(ans, 1);
                else ans = max(ans, x - bad + 1);
            } else if (x <= maxVal) {
                if (bad > 0) ans = max(ans, x - bad);
                else ans = max(ans, x - 1);
            }
        }

        return ans;
    }
};
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
- [3115. Maximum Prime Difference](../../3001-3500/3115-maximum-prime-difference/)
- [3591. Check if Any Element Has Prime Frequency](../../3501-4000/3591-check-if-any-element-has-prime-frequency/)
- [1255. Maximum Score Words Formed by Letters](../../1001-1500/1255-maximum-score-words-formed-by-letters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-score-with-co-prime-element/)
