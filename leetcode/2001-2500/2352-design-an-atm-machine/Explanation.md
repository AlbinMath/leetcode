# LeetCode 2241: Design an ATM Machine

**LeetCode Problem #2241 — Design an ATM Machine**
Solve LeetCode Design an ATM Machine using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design an ATM Machine |
| LeetCode | #2241 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an ATM machine that stores banknotes of `5` denominations: `20`, `50`, `100`, `200`, and `500` dollars. Initially the ATM is empty. The user can use the machine to deposit or withdraw any amount of money.

When withdrawing, the machine prioritizes using banknotes of **larger** values.

For example, if you want to withdraw `$300` and there are `2` `$50` banknotes, `1` `$100` banknote, and `1` `$200` banknote, then the machine will use the `$100` and `$200` banknotes. 
 However, if you try to withdraw `$600` and there are `3` `$200` banknotes and `1` `$500` banknote, then the withdraw request will be rejected because the machine will first try to use the `$500` banknote and then be unable to use banknotes to complete the remaining `$100`. Note that the machine is **not** allowed to use the `$200` banknotes instead of the `$500` banknote.

Implement the ATM class:

`ATM()` Initializes the ATM object. 
 `void deposit(int[] banknotesCount)` Deposits new banknotes in the order `$20`, `$50`, `$100`, `$200`, and `$500`. 
 `int[] withdraw(int amount)` Returns an array of length `5` of the number of banknotes that will be handed to the user in the order `$20`, `$50`, `$100`, `$200`, and `$500`, and update the number of banknotes in the ATM after withdrawing. Returns `[-1]` if it is not possible (do **not** withdraw any banknotes in this case).

## Constraints
- `banknotesCount.length == 5`
- `0 <= banknotesCount[i] <= 10^9`
- `1 <= amount <= 10^9`
- At most `5000` calls **in total** will be made to `withdraw` and `deposit`.
- At least **one** call will be made to each function `withdraw` and `deposit`.
- Sum of `banknotesCount[i]` in all deposits doesn't exceed `10^9`

## Examples
### Example 1
- **Input:** `["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"]
[[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]`
- **Output:** `[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]`
- **Explanation:** ATM atm = new ATM();
atm.deposit([0,0,1,2,1]); // Deposits 1 $100 banknote, 2 $200 banknotes,
 // and 1 $500 banknote.
atm.withdraw(600); // Returns [0,0,1,0,1]. The machine uses 1 $100 banknote
 // and 1 $500 banknote. The banknotes left over in the
 // machine are [0,0,0,2,0].
atm.deposit([0,1,0,1,1]); // Deposits 1 $50, $200, and $500 banknote.
 // The banknotes in the machine are now [0,1,0,3,1].
atm.withdraw(600); // Returns [-1]. The machine will try to use a $500 banknote
 // and then be unable to complete the remaining $100,
 // so the withdraw request will be rejected.
 // Since the request is rejected, the number of banknotes
 // in the machine is not modified.
atm.withdraw(550); // Returns [0,1,0,0,1]. The machine uses 1 $50 banknote
 // and 1 $500 banknote.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Design an ATM Machine**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["ATM", "deposit", "withdraw", "deposit", "withdraw", "withdraw"]
[[], [[0,0,1,2,1]], [600], [[0,1,0,1,1]], [600], [550]]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, [0,0,1,0,1], null, [-1], [0,1,0,0,1]]`.
4. **Verification:** ATM atm = new ATM();
atm.deposit([0,0,1,2,1]); // Deposits 1 $100 banknote, 2 $200 banknotes,
 // and 1 $500 banknote.
atm.withdraw(600); // Returns [0,0,1,0,1]. The machine uses 1 $100 banknote
 // and 1 $500 banknote. The banknotes left over in the
 // machine are [0,0,0,2,0].
atm.deposit([0,1,0,1,1]); // Deposits 1 $50, $200, and $500 banknote.
 // The banknotes in the machine are now [0,1,0,3,1].
atm.withdraw(600); // Returns [-1]. The machine will try to use a $500 banknote
 // and then be unable to complete the remaining $100,
 // so the withdraw request will be rejected.
 // Since the request is rejected, the number of banknotes
 // in the machine is not modified.
atm.withdraw(550); // Returns [0,1,0,0,1]. The machine uses 1 $50 banknote
 // and 1 $500 banknote.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var ATM = function() {
    this.denoms = [20, 50, 100, 200, 500];
    this.counts = [0, 0, 0, 0, 0];
};
ATM.prototype.deposit = function(banknotesCount) {
    for (let i = 0; i < 5; i++) {
        this.counts[i] += banknotesCount[i];
    }
};

ATM.prototype.withdraw = function(amount) {
    const used = [0, 0, 0, 0, 0];
    for (let i = 4; i >= 0; i--) {
        const take = Math.min(this.counts[i], Math.floor(amount / this.denoms[i]));
        used[i] = take;
        amount -= take * this.denoms[i];
    }
    if (amount !== 0) {
        return [-1];
    }
    for (let i = 0; i < 5; i++) {
        this.counts[i] -= used[i];
    }
    
    return used;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)
- [355. Design Twitter](../../0001-0500/0355-design-twitter/)
- [622. Design Circular Queue](../../0501-1000/0860-design-circular-queue/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-an-atm-machine/)
