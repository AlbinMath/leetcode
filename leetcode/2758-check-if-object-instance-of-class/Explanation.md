# Check If Object Instance Of Class

## Problem Explanation
Implement `instanceof` — check if an object is an instance of a class by traversing the prototype chain.

## How the Code Works
Walk up the prototype chain of `obj` using `Object.getPrototypeOf()`. At each step, check if the prototype matches `classFunction.prototype`. Return true if found, false if the chain ends (null).
