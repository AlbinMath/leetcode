# Destroying Asteroids

## Problem Explanation
A planet has mass `mass`. Asteroids come in array form. You can absorb an asteroid if your mass ≥ its mass, increasing your mass. Return whether you can destroy all asteroids (in any order).

## How the Code Works
Sort asteroids in ascending order. Greedily absorb from smallest to largest. If at any point the planet's mass is less than the current asteroid, return `false`.
