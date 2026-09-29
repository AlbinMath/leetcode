# To Be Or Not To Be

## Problem Explanation
Implement `expect(val)` that returns an object with `toBe(val2)` and `notToBe(val2)` methods for value comparison.

## How the Code Works
`toBe` compares with `===` and throws "Not Equal" if they differ. `notToBe` throws "Equal" if they match. Otherwise both return `true`.
