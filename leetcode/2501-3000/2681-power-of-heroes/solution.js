
var sumOfPower = function(nums) {
    const MOD = 1000000007n;
    nums.sort((a, b) => a - b);
    let sumMin = 0n;
    let ans = 0n;
    for (let x of nums) {
        let num = BigInt(x);

        let contribution =
            (num * num % MOD) *
            ((sumMin + num) % MOD) % MOD;

        ans = (ans + contribution) % MOD;

        sumMin = (sumMin * 2n + num) % MOD;
    }

    return Number(ans);
};

