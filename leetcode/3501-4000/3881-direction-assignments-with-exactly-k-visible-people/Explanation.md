# LeetCode 3881: Direction Assignments with Exactly K Visible People

**LeetCode Problem #3881 — Direction Assignments with Exactly K Visible People**
Solve LeetCode Direction Assignments with Exactly K Visible People using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Direction Assignments with Exactly K Visible People |
| LeetCode | #3881 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three integers `n`, `pos`, and `k`.

There are `n` people standing in a line indexed from 0 to `n - 1`. Each person **independently** chooses a direction:

`'L'`: **visible** only to people on their **right** 
 `'R'`: **visible** only to people on their **left** 
 
A person at index `pos` sees others as follows:

A person `i < pos` is visible if and only if they choose `'L'`. 
 A person `i > pos` is visible if and only if they choose `'R'`.

Return the number of possible direction assignments such that the person at index `pos` sees **exactly** `k` people.

Since the answer may be large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= n <= 10^5`
- `0 <= pos, k <= n - 1`

## Examples
### Example 1
- **Input:** `n = 3, pos = 1, k = 0`
- **Output:** `2`
- **Explanation:** ​​​​​​​ 

 
 Index 0 is to the left of `pos = 1`, and index 2 is to the right of `pos = 1`. 
 To see `k = 0` people, index 0 must choose `'R'` and index 2 must choose `'L'`, keeping both invisible. 
 The person at index 1 can choose `'L'` or `'R'` since it does not affect the count. Thus, the answer is 2.

### Example 2
- **Input:** `n = 3, pos = 2, k = 1`
- **Output:** `4`
- **Explanation:** Index 0 and index 1 are left of `pos = 2`, and there is no index to the right. 
 To see `k = 1` person, exactly one of index 0 or index 1 must choose `'L'`, and the other must choose `'R'`. 
 There are 2 ways to choose which index is visible from the left. 
 The person at index 2 can choose `'L'` or `'R'` since it does not affect the count. Thus, the answer is `2 + 2 = 4`.

### Example 3
- **Input:** `n = 1, pos = 0, k = 0`
- **Output:** `2`
- **Explanation:** There are no indices to the left or right of `pos = 0`. 
 To see `k = 0` people, no additional condition is required. 
 The person at index 0 can choose `'L'` or `'R'`. Thus, the answer is 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Direction Assignments with Exactly K Visible People**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, pos = 1, k = 0`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** ​​​​​​​ 

 
 Index 0 is to the left of `pos = 1`, and index 2 is to the right of `pos = 1`. 
 To see `k = 0` people, index 0 must choose `'R'` and index 2 must choose `'L'`, keeping both invisible. 
 The person at index 1 can choose `'L'` or `'R'` since it does not affect the count. Thus, the answer is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
int N = 100001;
int MOD = 1e9 + 7;
long long f[100001];
long long g[100001];

long long qmi(long long a, long long k, long long p) {
    long long res = 1;
    while (k != 0) {
        if ((k & 1) == 1) {
            res = res * a % p;
        }
        k >>= 1;
        a = a * a % p;
    }
    return res;
}

int init = []() {
    f[0] = 1;
    g[0] = 1;
    for (int i = 1; i < N; ++i) {
        f[i] = f[i - 1] * i % MOD;
        g[i] = qmi(f[i], MOD - 2, MOD);
    }
    return 0;
}();

long long comb(int n, int k) {
    return f[n] * g[k] % MOD * g[n - k] % MOD;
}

class Solution {
public:
    int countVisiblePeople(int n, int pos, int k) {
        int l = pos, r = n - pos - 1;
        long long ans = 0;

        for (int a = 0; a <= min(k, l); ++a) {
            int b = k - a;
            if (b <= r) {
                ans = (ans + 2 * comb(l, a) % MOD * comb(r, b) % MOD) % MOD;
            }
        }
        return ans;
    }
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1944. Number of Visible People in a Queue](../../1501-2000/1944-number-of-visible-people-in-a-queue/)
- [2400. Number of Ways to Reach a Position After Exactly k Steps](../../2001-2500/2400-number-of-ways-to-reach-a-position-after-exactly-k-steps/)
- [3988. Create Grid With Exactly K Paths I](../../3501-4000/3988-create-grid-with-exactly-k-paths-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/)
