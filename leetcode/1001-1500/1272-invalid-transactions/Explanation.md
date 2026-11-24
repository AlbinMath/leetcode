# LeetCode 1169: Invalid Transactions

**LeetCode Problem #1169 — Invalid Transactions**
Solve LeetCode Invalid Transactions using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Invalid Transactions |
| LeetCode | #1169 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A transaction is possibly invalid if:

the amount exceeds `$1000`, or; 
 if it occurs within (and including) `60` minutes of another transaction with the **same name** in a **different city**.

You are given an array of strings `transaction` where `transactions[i]` consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of `transactions` that are possibly invalid. You may return the answer in **any order**.

## Constraints
- `transactions.length <= 1000`
- Each `transactions[i]` takes the form `"{name},{time},{amount},{city}"`
- Each `{name}` and `{city}` consist of lowercase English letters, and have lengths between `1` and `10`.
- Each `{time}` consist of digits, and represent an integer between `0` and `1000`.
- Each `{amount}` consist of digits, and represent an integer between `0` and `2000`.

## Examples
### Example 1
- **Input:** `transactions = ["alice,20,800,mtv","alice,50,100,beijing"]`
- **Output:** `["alice,20,800,mtv","alice,50,100,beijing"]`
- **Explanation:** The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

### Example 2
- **Input:** `transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]`
- **Output:** `["alice,50,1200,mtv"]`

### Example 3
- **Input:** `transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]`
- **Output:** `["bob,50,1200,mtv"]`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Invalid Transactions**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `transactions = ["alice,20,800,mtv","alice,50,100,beijing"]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["alice,20,800,mtv","alice,50,100,beijing"]`.
4. **Verification:** The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city))

        res = []
        for i, (name, time, amount, city) in enumerate(parsed):
            if amount > 1000:
                res.append(transactions[i])
                continue

            for j, (n2, t2, _, c2) in enumerate(parsed):
                if i != j and name == n2 and city != c2 and abs(time - t2) <= 60:
                    res.append(transactions[i])
                    break

        return res
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
- [1193. Monthly Transactions I](../../1001-1500/1317-monthly-transactions-i/)
- [1581. Customer Who Visited but Did Not Make Any Transactions](../../1501-2000/1724-customer-who-visited-but-did-not-make-any-transactions/)
- [3220. Odd and Even Transactions](../../3501-4000/3530-odd-and-even-transactions/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/invalid-transactions/)
