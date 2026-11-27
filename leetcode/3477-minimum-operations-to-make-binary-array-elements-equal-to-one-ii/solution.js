
var minOperations = function(nums) {
    let operations = 0;
    let flipped = 0;

    for (let num of nums) {
        const current = num ^ flipped;

        if (current === 0) {
            operations++;
            flipped ^= 1;
        }
    }

    return operations;
};

