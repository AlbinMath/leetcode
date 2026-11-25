# LeetCode 2043: Simple Bank System

**LeetCode Problem #2043 — Simple Bank System**
Solve LeetCode Simple Bank System using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Simple Bank System |
| LeetCode | #2043 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has `n` accounts numbered from `1` to `n`. The initial balance of each account is stored in a **0-indexed** integer array `balance`, with the `(i + 1)^th` account having an initial balance of `balance[i]`.

Execute all the **valid** transactions. A transaction is **valid** if:

The given account number(s) are between `1` and `n`, and 
 The amount of money withdrawn or transferred from is **less than or equal** to the balance of the account.

Implement the `Bank` class:

`Bank(long[] balance)` Initializes the object with the **0-indexed** integer array `balance`. 
 `boolean transfer(int account1, int account2, long money)` Transfers `money` dollars from the account numbered `account1` to the account numbered `account2`. Return `true` if the transaction was successful, `false` otherwise. 
 `boolean deposit(int account, long money)` Deposit `money` dollars into the account numbered `account`. Return `true` if the transaction was successful, `false` otherwise. 
 `boolean withdraw(int account, long money)` Withdraw `money` dollars from the account numbered `account`. Return `true` if the transaction was successful, `false` otherwise.

## Constraints
- `n == balance.length`
- `1 <= n, account, account1, account2 <= 10^5`
- `0 <= balance[i], money <= 10^12`
- At most `10^4` calls will be made to **each** function `transfer`, `deposit`, `withdraw`.

## Examples
### Example 1
- **Input:** `["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]`
- **Output:** `[null, true, true, true, false, false]`
- **Explanation:** Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10); // return true, account 3 has a balance of $20, so it is valid to withdraw $10.
 // Account 3 has $20 - $10 = $10.
bank.transfer(5, 1, 20); // return true, account 5 has a balance of $30, so it is valid to transfer $20.
 // Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
bank.deposit(5, 20); // return true, it is valid to deposit $20 to account 5.
 // Account 5 has $10 + $20 = $30.
bank.transfer(3, 4, 15); // return false, the current balance of account 3 is $10,
 // so it is invalid to transfer $15 from it.
bank.withdraw(10, 50); // return false, it is invalid because account 10 does not exist.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Simple Bank System**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, true, true, true, false, false]`.
4. **Verification:** Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10); // return true, account 3 has a balance of $20, so it is valid to withdraw $10.
 // Account 3 has $20 - $10 = $10.
bank.transfer(5, 1, 20); // return true, account 5 has a balance of $30, so it is valid to transfer $20.
 // Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
bank.deposit(5, 20); // return true, it is valid to deposit $20 to account 5.
 // Account 5 has $10 + $20 = $30.
bank.transfer(3, 4, 15); // return false, the current balance of account 3 is $10,
 // so it is invalid to transfer $15 from it.
bank.withdraw(10, 50); // return false, it is invalid because account 10 does not exist.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Validate account numbers
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False

        # Check whether the source account has enough money
        if self.balance[account1 - 1] < money:
            return False

        # Perform the transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money

        return True

    def deposit(self, account: int, money: int) -> bool:
        # Validate account number
        if not (1 <= account <= self.n):
            return False

        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # Validate account number
        if not (1 <= account <= self.n):
            return False

        # Check sufficient balance
        if self.balance[account - 1] < money:
            return False

        self.balance[account - 1] -= money
        return True
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
- [1587. Bank Account Summary II](../../1501-2000/1587-bank-account-summary-ii/)
- [1716. Calculate Money in Leetcode Bank](../../1501-2000/1716-calculate-money-in-leetcode-bank/)
- [609. Find Duplicate File in System](../../0501-1000/0609-find-duplicate-file-in-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/simple-bank-system/)
