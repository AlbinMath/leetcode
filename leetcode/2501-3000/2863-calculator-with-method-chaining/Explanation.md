# LeetCode 2726: Calculator with Method Chaining

**LeetCode Problem #2726 — Calculator with Method Chaining**
Solve LeetCode Calculator with Method Chaining using TypeScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Calculator with Method Chaining |
| LeetCode | #2726 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design a `Calculator` class. The class should provide the mathematical operations of addition, subtraction, multiplication, division, and exponentiation. It should also allow consecutive operations to be performed using method chaining. The `Calculator` class constructor should accept a number which serves as the initial value of `result`.

Your `Calculator` class should have the following methods:

`add` - This method adds the given number `value` to the `result` and returns the updated `Calculator`. 
 `subtract` - This method subtracts the given number `value` from the `result` and returns the updated `Calculator`. 
 `multiply` - This method multiplies the `result` by the given number `value` and returns the updated `Calculator`. 
 `divide` - This method divides the `result` by the given number `value` and returns the updated `Calculator`. If the passed value is `0`, an error `"Division by zero is not allowed"` should be thrown. 
 `power` - This method raises the `result` to the power of the given number `value` and returns the updated `Calculator`. 
 `getResult` - This method returns the `result`.

Solutions within `10^-5` of the actual result are considered correct.

## Constraints
- `actions` is a valid JSON array of strings
- `values` is a valid JSON array of numbers
- `2 <= actions.length <= 2 * 10^4`
- `1 <= values.length <= 2 * 10^4 - 1`
- `actions[i]` is one of "Calculator", "add", "subtract", "multiply", "divide", "power", and "getResult"
- First action is always "Calculator"
- Last action is always "getResult"

## Examples
### Example 1
- **Input:** `actions = ["Calculator", "add", "subtract", "getResult"], 
values = [10, 5, 7]`
- **Output:** `8`
- **Explanation:** new Calculator(10).add(5).subtract(7).getResult() // 10 + 5 - 7 = 8

### Example 2
- **Input:** `actions = ["Calculator", "multiply", "power", "getResult"], 
values = [2, 5, 2]`
- **Output:** `100`
- **Explanation:** new Calculator(2).multiply(5).power(2).getResult() // (2 * 5) ^ 2 = 100

### Example 3
- **Input:** `actions = ["Calculator", "divide", "getResult"], 
values = [20, 0]`
- **Output:** `"Division by zero is not allowed"`
- **Explanation:** new Calculator(20).divide(0).getResult() // 20 / 0 

The error should be thrown because we cannot divide by zero.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
Each method (`add`, `subtract`, `multiply`, `divide`) modifies the internal `result` and returns `this` to enable chaining. `divide` throws an error if dividing by zero. `getResult` returns the current value.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `actions = ["Calculator", "add", "subtract", "getResult"], 
values = [10, 5, 7]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** new Calculator(10).add(5).subtract(7).getResult() // 10 + 5 - 7 = 8

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
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
class Calculator {
    result: number;

    constructor(value: number) {
        this.result = value;
    }

    add(value: number): Calculator {
        this.result += value;
        return this;
    }

    subtract(value: number): Calculator {
        this.result -= value;
        return this;
    }

    multiply(value: number): Calculator {
        this.result *= value;
        return this;
    }

    divide(value: number): Calculator {
        if (value === 0) {
            throw new Error("Division by zero is not allowed");
        }

        this.result /= value;
        return this;
    }

    power(value: number): Calculator {
        this.result = Math.pow(this.result, value);
        return this;
    }

    getResult(): number {
        return this.result;
    }
}
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
- [2891. Method Chaining](../../3001-3500/3063-method-chaining/)
- [224. Basic Calculator](../../0001-0500/0224-basic-calculator/)
- [227. Basic Calculator II](../../0001-0500/0227-basic-calculator-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/calculator-with-method-chaining/)
