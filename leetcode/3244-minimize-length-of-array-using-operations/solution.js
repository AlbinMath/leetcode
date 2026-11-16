/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumArrayLength = function(nums) {
    // 1. Find the minimum element in the array
    let minVal = Infinity;
    for (const num of nums) {
        if (num < minVal) {
            minVal = num;
        }
    }

    // 2. Check if any element is not divisible by minVal,
    //    and count occurrences of minVal
    let minCount = 0;
    for (const num of nums) {
        if (num % minVal !== 0) {
            // We can generate (num % minVal) < minVal, reducing the array to length 1
            return 1;
        }
        if (num === minVal) {
            minCount++;
        }
    }

    // 3. All elements are multiples of minVal; pair up the minVal copies
    return Math.ceil(minCount / 2);
};
