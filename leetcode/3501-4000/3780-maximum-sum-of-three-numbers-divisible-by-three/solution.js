var maximumSum = function(nums) {
    const groups = [[], [], []];

    for (const num of nums) {
        groups[num % 3].push(num);
    }

    for (const group of groups) {
        group.sort((a, b) => b - a);
    }

    let ans = 0;

    if (groups[0].length >= 3) {
        ans = Math.max(
            ans,
            groups[0][0] + groups[0][1] + groups[0][2]
        );
    }

    if (groups[1].length >= 3) {
        ans = Math.max(
            ans,
            groups[1][0] + groups[1][1] + groups[1][2]
        );
    }

    if (groups[2].length >= 3) {
        ans = Math.max(
            ans,
            groups[2][0] + groups[2][1] + groups[2][2]
        );
    }

    if (
        groups[0].length >= 1 &&
        groups[1].length >= 1 &&
        groups[2].length >= 1
    ) {
        ans = Math.max(
            ans,
            groups[0][0] + groups[1][0] + groups[2][0]
        );
    }

    return ans;
};
