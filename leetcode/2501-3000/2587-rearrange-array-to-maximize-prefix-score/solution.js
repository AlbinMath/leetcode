
var maxScore = function(nums) {
    nums.sort((a, b) => b - a);

    let sum = 0;
    let score = 0;

    for (let num of nums) {
        sum += num;

        if (sum > 0) {
            score++;
        } else {
            break;
        }
    }

    return score;
};

