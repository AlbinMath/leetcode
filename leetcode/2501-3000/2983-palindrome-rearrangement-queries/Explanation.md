# LeetCode 2983: Palindrome Rearrangement Queries

**LeetCode Problem #2983 — Palindrome Rearrangement Queries**
Solve LeetCode Palindrome Rearrangement Queries using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Palindrome Rearrangement Queries |
| LeetCode | #2983 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string `s` having an **even** length `n`.

You are also given a **0-indexed** 2D integer array, `queries`, where `queries[i] = [a_i, b_i, c_i, d_i]`.

For each query `i`, you are allowed to perform the following operations:

Rearrange the characters within the **substring** `s[a_i:b_i]`, where `0 <= a_i <= b_i < n / 2`. 
 Rearrange the characters within the **substring** `s[c_i:d_i]`, where `n / 2 <= c_i <= d_i < n`.

For each query, your task is to determine whether it is possible to make `s` a **palindrome** by performing the operations.

Each query is answered **independently** of the others.

Return *a **0-indexed** array *`answer`*, where *`answer[i] == true`* if it is possible to make *`s`* a palindrome by performing operations specified by the *`i^th`* query, and *`false`* otherwise.*

A **substring** is a contiguous sequence of characters within a string. 
 `s[x:y]` represents the substring consisting of characters from the index `x` to index `y` in `s`, **both inclusive**.

## Constraints
- `2 <= n == s.length <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 4`
- `a_i == queries[i][0], b_i == queries[i][1]`
- `c_i == queries[i][2], d_i == queries[i][3]`
- `0 <= a_i <= b_i < n / 2`
- `n / 2 <= c_i <= d_i < n `
- `n` is even.
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]]`
- **Output:** `[true,true]`
- **Explanation:** In this example, there are two queries:
In the first query:
- a_0 = 1, b_0 = 1, c_0 = 3, d_0 = 5.
- So, you are allowed to rearrange s[1:1] => a b cabc and s[3:5] => abc abc .
- To make s a palindrome, s[3:5] can be rearranged to become => abc cba .
- Now, s is a palindrome. So, answer[0] = true.
In the second query:
- a_1 = 0, b_1 = 2, c_1 = 5, d_1 = 5.
- So, you are allowed to rearrange s[0:2] => abc abc and s[5:5] => abcab c .
- To make s a palindrome, s[0:2] can be rearranged to become => cba abc.
- Now, s is a palindrome. So, answer[1] = true.

### Example 2
- **Input:** `s = "abbcdecbba", queries = [[0,2,7,9]]`
- **Output:** `[false]`
- **Explanation:** In this example, there is only one query.
a_0 = 0, b_0 = 2, c_0 = 7, d_0 = 9.
So, you are allowed to rearrange s[0:2] => abb cdecbba and s[7:9] => abbcdec bba .
It is not possible to make s a palindrome by rearranging these substrings because s[3:6] is not a palindrome.
So, answer[0] = false.

### Example 3
- **Input:** `s = "acbcab", queries = [[1,2,4,5]]`
- **Output:** `[true]`
- **Explanation:** In this example, there is only one query.
a_0 = 1, b_0 = 2, c_0 = 4, d_0 = 5.
So, you are allowed to rearrange s[1:2] => a cb cab and s[4:5] => acbc ab .
To make s a palindrome s[1:2] can be rearranged to become a bc cab.
Then, s[4:5] can be rearranged to become abcc ba .
Now, s is a palindrome. So, answer[0] = true.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Palindrome Rearrangement Queries**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[true,true]`.
4. **Verification:** In this example, there are two queries:
In the first query:
- a_0 = 1, b_0 = 1, c_0 = 3, d_0 = 5.
- So, you are allowed to rearrange s[1:1] => a b cabc and s[3:5] => abc abc .
- To make s a palindrome, s[3:5] can be rearranged to become => abc cba .
- Now, s is a palindrome. So, answer[0] = true.
In the second query:
- a_1 = 0, b_1 = 2, c_1 = 5, d_1 = 5.
- So, you are allowed to rearrange s[0:2] => abc abc and s[5:5] => abcab c .
- To make s a palindrome, s[0:2] can be rearranged to become => cba abc.
- Now, s is a palindrome. So, answer[1] = true.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var canMakePalindromeQueries = function(s, queries) {
    const n = s.length;
    const m = n / 2;
    const left = s.slice(0, m);
    const right = s.slice(m).split('').reverse().join('');
    const prefL = Array.from(
        { length: 26 },
        () => new Int32Array(m + 1)
    );
    const prefR = Array.from(
        { length: 26 },
        () => new Int32Array(m + 1)
    );
    const mismatch = new Int32Array(m + 1);
    for (let i = 0; i < m; i++) {
        const x = left.charCodeAt(i) - 97;
        const y = right.charCodeAt(i) - 97;
        for (let c = 0; c < 26; c++) {
            prefL[c][i + 1] = prefL[c][i];
            prefR[c][i + 1] = prefR[c][i];
        }
        prefL[x][i + 1]++;
        prefR[y][i + 1]++;
        mismatch[i + 1] =
            mismatch[i] + (x !== y ? 1 : 0);
    }
    const getCount = (pref, c, l, r) => {
        if (l > r) return 0;
        return pref[c][r + 1] - pref[c][l];
    };
    const getMismatch = (l, r) => {
        if (l > r) return 0;
        return mismatch[r + 1] - mismatch[l];
    };
    const answer = [];
    for (const [a, b, c, d] of queries) {
        const l2 = n - 1 - d;
        const r2 = n - 1 - c;
        const start = Math.max(a, l2);
        const end = Math.min(b, r2);
        let bad = mismatch[m];
        bad -= getMismatch(a, b);
        bad -= getMismatch(l2, r2);
        if (start <= end) {
            bad += getMismatch(start, end);
        }
        if (bad !== 0) {
            answer.push(false);
            continue;
        }
        let valid = true;
        for (let ch = 0; ch < 26; ch++) {
            const leftAvailable =
                getCount(prefL, ch, a, b);
            const rightFixed =
                getCount(prefR, ch, a, b) -
                getCount(prefR, ch, start, end);
            const rightAvailable =
                getCount(prefR, ch, l2, r2);
            const leftFixed =
                getCount(prefL, ch, l2, r2) -
                getCount(prefL, ch, start, end);
            const remainingLeft =
                leftAvailable - rightFixed;

            const remainingRight =
                rightAvailable - leftFixed;
            if (
                remainingLeft < 0 ||
                remainingRight < 0 ||
                remainingLeft !== remainingRight
            ) {
                valid = false;
                break;
            }
        }
        answer.push(valid);
    }
    return answer;
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [985. Sum of Even Numbers After Queries](../../0501-1000/0985-sum-of-even-numbers-after-queries/)
- [1211. Queries Quality and Percentage](../../1001-1500/1211-queries-quality-and-percentage/)
- [1310. XOR Queries of a Subarray](../../1001-1500/1310-xor-queries-of-a-subarray/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/palindrome-rearrangement-queries/)
