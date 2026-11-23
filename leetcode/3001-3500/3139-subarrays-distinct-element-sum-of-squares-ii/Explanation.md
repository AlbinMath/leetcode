# LeetCode 2916: Subarrays Distinct Element Sum of Squares II

**LeetCode Problem #2916 — Subarrays Distinct Element Sum of Squares II**
Solve LeetCode Subarrays Distinct Element Sum of Squares II using JavaScript, Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Subarrays Distinct Element Sum of Squares II |
| LeetCode | #2916 |
| Difficulty | Hard |
| Language | JavaScript, Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed **integer array `nums`.

The **distinct count** of a subarray of `nums` is defined as:

Let `nums[i..j]` be a subarray of `nums` consisting of all the indices from `i` to `j` such that `0 <= i <= j < nums.length`. Then the number of distinct values in `nums[i..j]` is called the distinct count of `nums[i..j]`.

Return *the sum of the **squares** of **distinct counts** of all subarrays of *`nums`.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Examples
### Example 1
- **Input:** `nums = [1,2,1]`
- **Output:** `15`
- **Explanation:** Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15.

### Example 2
- **Input:** `nums = [2,2]`
- **Output:** `3`
- **Explanation:** Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 = 3.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Subarrays Distinct Element Sum of Squares II**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var sumCounts = function(nums) {
    const MOD = 1000000007;
    const n = nums.length;

    const sum = new Array(4 * n).fill(0);
    const sumSq = new Array(4 * n).fill(0);
    const lazy = new Array(4 * n).fill(0);

    function apply(node, left, right, delta) {
        const len = right - left + 1;

        sumSq[node] = (
            sumSq[node] +
            2 * delta * sum[node] +
            delta * delta * len
        ) % MOD;

        sum[node] = (sum[node] + delta * len) % MOD;
        lazy[node] += delta;
    }

    function push(node, left, right) {
        if (lazy[node] === 0 || left === right) return;

        const mid = Math.floor((left + right) / 2);
        const delta = lazy[node];

        apply(node * 2, left, mid, delta);
        apply(node * 2 + 1, mid + 1, right, delta);

        lazy[node] = 0;
    }

    function update(node, left, right, ql, qr) {
        if (ql > right || qr < left) return;

        if (ql <= left && right <= qr) {
            apply(node, left, right, 1);
            return;
        }

        push(node, left, right);

        const mid = Math.floor((left + right) / 2);

        update(node * 2, left, mid, ql, qr);
        update(node * 2 + 1, mid + 1, right, ql, qr);

        sum[node] = (
            sum[node * 2] + sum[node * 2 + 1]
        ) % MOD;

        sumSq[node] = (
            sumSq[node * 2] + sumSq[node * 2 + 1]
        ) % MOD;
    }

    const lastSeen = new Map();
    let answer = 0;

    for (let i = 0; i < n; i++) {
        const prev = lastSeen.has(nums[i])
            ? lastSeen.get(nums[i])
            : -1;

        update(1, 0, n - 1, prev + 1, i);

        lastSeen.set(nums[i], i);

        answer = (answer + sumSq[1]) % MOD;
    }

    return answer;
};
```

### Python
```python
class Solution:
    def sumCounts(self, nums):
        n, mod = len(nums), 10**9+7
        s, q, lazy = [0]*(4*n), [0]*(4*n), [0]*(4*n)

        def upd(p,l,r,a,b):
            if a<=l and r<=b:
                d=r-l+1
                q[p]=(q[p]+2*s[p]+d)%mod
                s[p]=(s[p]+d)%mod
                lazy[p]+=1
                return
            m=(l+r)//2
            if lazy[p]:
                v=lazy[p]
                for c,x,y in ((p*2,l,m),(p*2+1,m+1,r)):
                    d=y-x+1
                    q[c]=(q[c]+2*v*s[c]+v*v*d)%mod
                    s[c]=(s[c]+v*d)%mod
                    lazy[c]+=v
                lazy[p]=0
            if a<=m: upd(p*2,l,m,a,b)
            if b>m: upd(p*2+1,m+1,r,a,b)
            s[p]=(s[p*2]+s[p*2+1])%mod
            q[p]=(q[p*2]+q[p*2+1])%mod

        last, ans = {}, 0
        for i,x in enumerate(nums):
            j=last.get(x,-1)+1
            upd(1,0,n-1,j,i)
            last[x]=i
            ans=(ans+q[1])%mod
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
- [2913. Subarrays Distinct Element Sum of Squares I](../../3001-3500/3163-subarrays-distinct-element-sum-of-squares-i/)
- [2461. Maximum Sum of Distinct Subarrays With Length K](../../2501-3000/2552-maximum-sum-of-distinct-subarrays-with-length-k/)
- [2862. Maximum Element-Sum of a Complete Subset of Indices](../../3001-3500/3047-maximum-element-sum-of-a-complete-subset-of-indices/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/)
