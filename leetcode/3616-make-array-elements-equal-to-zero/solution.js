var countValidSelections = function(nums) {
    let totalSum = 0;
    for (const num of nums) totalSum += num;

    let leftSum = 0;
    let validSelections = 0;

    for (const num of nums) {
        if (num === 0) {
            const rightSum = totalSum - leftSum;
            const diff = Math.abs(leftSum - rightSum);
            if (diff === 0) {
                validSelections += 2;
            } else if (diff === 1) {
                validSelections += 1;
            }
        } else {
            leftSum += num;
        }
    }

    return validSelections;
};
