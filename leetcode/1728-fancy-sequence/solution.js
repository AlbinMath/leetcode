var Fancy = function () {
    this.MOD = 1000000007n;
    this.vals = [];
    this.mul = 1n;
    this.add = 0n;
};

Fancy.prototype.power = function (base, exp) {
    const MOD = this.MOD;
    let result = 1n;
    base %= MOD;
    while (exp > 0n) {
        if (exp & 1n) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1n;
    }
    return result;
};

/** @param {number} val */
Fancy.prototype.append = function (val) {
    const MOD = this.MOD;
    const inv = this.power(this.mul, MOD - 2n);
    const stored = (((BigInt(val) - this.add) % MOD + MOD) % MOD) * inv % MOD;
    this.vals.push(stored);
};

/** @param {number} inc */
Fancy.prototype.addAll = function (inc) {
    this.add = (this.add + BigInt(inc)) % this.MOD;
};

/** @param {number} m */
Fancy.prototype.multAll = function (m) {
    const bm = BigInt(m);
    this.mul = (this.mul * bm) % this.MOD;
    this.add = (this.add * bm) % this.MOD;
};

/** @param {number} idx */
Fancy.prototype.getIndex = function (idx) {
    if (idx >= this.vals.length) return -1;
    return Number((this.vals[idx] * this.mul + this.add) % this.MOD);
};
