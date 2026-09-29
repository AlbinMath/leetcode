# Calculator With Method Chaining

## Problem Explanation
Implement a Calculator class with `add`, `subtract`, `multiply`, `divide`, and `getResult` methods that support method chaining.

## How the Code Works
Each method (`add`, `subtract`, `multiply`, `divide`) modifies the internal `result` and returns `this` to enable chaining. `divide` throws an error if dividing by zero. `getResult` returns the current value.
