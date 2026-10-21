
/**
 * @param {number[][]} students
 * @param {number[][]} mentors
 * @return {number}
 */
var maxCompatibilitySum = function(students, mentors) {
    const m = students.length;
    const totalMasks = 1 << m;

    // score[i][j] = compatibility score of student i and mentor j
    const score = Array.from({ length: m }, () => new Array(m).fill(0));

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < m; j++) {
            for (let k = 0; k < students[i].length; k++) {
                if (students[i][k] === mentors[j][k]) {
                    score[i][j]++;
                }
            }
        }
    }

    // dp[mask] = maximum score after assigning mentors in mask
    const dp = new Array(totalMasks).fill(-1);
    dp[0] = 0;

    for (let mask = 0; mask < totalMasks; mask++) {
        if (dp[mask] === -1) continue;

        // Assign the next student
        const student = countBits(mask);

        if (student === m) continue;

        for (let j = 0; j < m; j++) {
            // Skip mentors who are already assigned
            if (mask & (1 << j)) continue;

            const nextMask = mask | (1 << j);

            dp[nextMask] = Math.max(
                dp[nextMask],
                dp[mask] + score[student][j]
            );
        }
    }

    return dp[totalMasks - 1];

    function countBits(mask) {
        let count = 0;

        while (mask > 0) {
            mask &= mask - 1;
            count++;
        }

        return count;
    }
};

