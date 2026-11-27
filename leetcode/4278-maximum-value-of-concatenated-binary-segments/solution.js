
var maxValue = function(nums1, nums0) {
    const MOD = 1000000007n;
    const n = nums1.length;

    const segments = [];

    let totalLength = 0;

    for (let i = 0; i < n; i++) {
        segments.push([nums1[i], nums0[i]]);
        totalLength += nums1[i] + nums0[i];
    }

    function compare(A, B) {
        const x = [
            [1, A[0]],
            [0, A[1]],
            [1, B[0]],
            [0, B[1]]
        ];

        const y = [
            [1, B[0]],
            [0, B[1]],
            [1, A[0]],
            [0, A[1]]
        ];

        let i = 0;
        let j = 0;
        let remX = 0;
        let remY = 0;

        while (i < 4 && j < 4) {
            while (i < 4 && remX === 0) {
                remX = x[i][1];
                if (remX === 0) i++;
            }

            while (j < 4 && remY === 0) {
                remY = y[j][1];
                if (remY === 0) j++;
            }

            if (i === 4 || j === 4) break;

            if (x[i][0] !== y[j][0]) {
                return x[i][0] === 1 ? -1 : 1;
            }

            const take = Math.min(remX, remY);

            remX -= take;
            remY -= take;

            if (remX === 0) i++;
            if (remY === 0) j++;
        }

        return 0;
    }

    segments.sort(compare);

    const pow2 = new Array(totalLength + 1);
    pow2[0] = 1n;

    for (let i = 1; i <= totalLength; i++) {
        pow2[i] = (pow2[i - 1] * 2n) % MOD;
    }

    let ans = 0n;

    for (const [ones, zeros] of segments) {
        ans = (ans * pow2[ones] + pow2[ones] - 1n) % MOD;

        ans = (ans * pow2[zeros]) % MOD;
    }

    return Number(ans);
};

