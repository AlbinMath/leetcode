var minimumOperations = function(nums) {
    // Store distinct non-zero elements in a Set
    const uniquePositives = new Set();
    for (const num of nums) {
        if (num > 0) {
            uniquePositives.add(num);
        }
    }
    return uniquePositives.size;
};
