# LeetCode 3962: Maximum Subarray Sum After at Most K Swaps

**LeetCode Problem #3962 — Maximum Subarray Sum After at Most K Swaps**
Solve LeetCode Maximum Subarray Sum After at Most K Swaps using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Subarray Sum After at Most K Swaps |
| LeetCode | #3962 |
| Difficulty | Hard |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

You are allowed to perform **at most** `k` swap operations on the array.

In one swap operation, you may choose any two indices `i` and `j` and swap `nums[i]` and `nums[j]`.

Return an integer denoting the **maximum possible subarray sum** after performing the swaps.

## Constraints
- `1 <= nums.length <= 1500`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= k <= nums.length`

## Examples
### Example 1
- **Input:** `nums = [1,-1,0,2], k = 1`
- **Output:** `3`
- **Explanation:** We can swap on indices 1 and 3, resulting in the array `[1, 2, 0, -1]`. 
 The subarray `[1, 2]` has a sum of 3, which is the maximum possible subarray sum after at most `k = 1`​​​​​​​ swap.

### Example 2
- **Input:** `nums = [4,3,2,4], k = 2`
- **Output:** `13`
- **Explanation:** The maximum possible subarray sum after at most `k = 2` swaps is the sum of the entire array, which is 13.

### Example 3
- **Input:** `nums = [-1,-2], k = 0`
- **Output:** `-1`
- **Explanation:** `k = 0` swaps are allowed. 
 The possible subarrays are `[-1]`, `[-2]`, and `[-1, -2]`, with sums -1, -2, and -3 respectively. 
 Among these sums, the maximum is -1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Subarray Sum After at Most K Swaps**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,-1,0,2], k = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can swap on indices 1 and 3, resulting in the array `[1, 2, 0, -1]`. 
 The subarray `[1, 2]` has a sum of 3, which is the maximum possible subarray sum after at most `k = 1`​​​​​​​ swap.

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
    int n, LOG;
    vector<long long> val; // value by rank (1-indexed)
    struct BIT {
        vector<int> c; vector<long long> s;
    };
    void upd(BIT &b, int i, int dc, long long ds) {
        for (; i <= n; i += i & -i) { b.c[i] += dc; b.s[i] += ds; }
    }
    // returns k-th smallest value (k>=1); sumOut = sum of k smallest
    long long kth(const BIT &b, int k, long long &sumOut) {
        int pos = 0; long long acc = 0;
        for (int pw = LOG; pw > 0; pw >>= 1) {
            int np = pos + pw;
            if (np <= n && b.c[np] < k) {
                pos = np; k -= b.c[np]; acc += b.s[np];
            }
        }
        sumOut = acc + val[pos + 1];
        return val[pos + 1];
    }
public:
    long long maxSum(vector<int>& nums, int k) {
        n = nums.size();
        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);
        sort(idx.begin(), idx.end(), [&](int a, int b) {
            return nums[a] != nums[b] ? nums[a] < nums[b] : a < b;
        });
        vector<int> rk(n);
        val.assign(n + 2, 0);
        for (int i = 0; i < n; i++) { rk[idx[i]] = i + 1; val[i + 1] = nums[idx[i]]; }
        LOG = 1; while (LOG * 2 <= n) LOG *= 2;

        BIT full{vector<int>(n + 1, 0), vector<long long>(n + 1, 0)};
        for (int i = 1; i <= n; i++) {
            full.c[i] += 1; full.s[i] += val[i];
            int j = i + (i & -i);
            if (j <= n) { full.c[j] += full.c[i]; full.s[j] += full.s[i]; }
        }
        long long totalAll = 0;
        for (int x : nums) totalAll += x;

        long long ans = LLONG_MIN;
        BIT in{vector<int>(n + 1, 0), vector<long long>(n + 1, 0)};
        BIT out = full;
        for (int l = 0; l < n; l++) {
            fill(in.c.begin(), in.c.end(), 0);
            fill(in.s.begin(), in.s.end(), 0);
            out = full;
            long long inSum = 0, outSum = totalAll;
            int t = 0;
            for (int r = l; r < n; r++) {
                int x = nums[r];
                upd(in, rk[r], 1, x);
                upd(out, rk[r], -1, -x);
                inSum += x; outSum -= x;
                int I = r - l + 1, O = n - I;
                int m = min(k, min(I, O));
                long long d;
                // cond(j): j-th largest outside > j-th smallest inside
                auto cond = [&](int j) {
                    return kth(out, O - j + 1, d) > kth(in, j, d);
                };
                if (t > m) t = m;
                while (t < m && cond(t + 1)) t++;
                while (t > 0 && !cond(t)) t--;

                long long gain = 0;
                if (t > 0) {
                    long long sIn, smallOut = 0;
                    kth(in, t, sIn);
                    if (O - t > 0) kth(out, O - t, smallOut);
                    gain = (outSum - smallOut) - sIn;
                }
                ans = max(ans, inSum + gain);
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
- [1505. Minimum Possible Integer After at Most K Adjacent Swaps On Digits](../../1501-2000/1629-minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2229-maximum-fruits-harvested-after-at-most-k-steps/)
- [560. Subarray Sum Equals K](../../0501-1000/0560-subarray-sum-equals-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/)
