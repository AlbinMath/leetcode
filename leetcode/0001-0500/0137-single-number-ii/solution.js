
var singleNumber = function(nums) {
    let result = 0;

    for (let i = 0; i < 32; i++) {
        let count = 0;

        for (const num of nums) {
            // Check bit i
            count += (num >>> i) & 1;
        }

        // Restore the bit if it appears a non-multiple of 3 times
        if (count % 3 !== 0) {
            result |= (1 << i);
        }
    }

    return result | 0;
};

