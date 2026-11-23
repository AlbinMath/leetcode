/**
 * The rand7() API is already defined for you.
 * @return {number} a random integer in [1, 7]
 */

/**
 * @return {number}
 */
var rand10 = function() {
    while (true) {
        const a = rand7() - 1;
        const b = rand7() - 1;

        const num = a * 7 + b; // Uniform integer from 0 to 48

        if (num < 40) {
            return (num % 10) + 1;
        }
    }
};
