var Bitset = function(size) {
    this.size = size;
    this.bits = new Uint8Array(size);
    this.ones = 0;
    this.flipped = 0; // 0 for false, 1 for true
};
Bitset.prototype.fix = function(idx) {
    if (this.bits[idx] === this.flipped) {
        this.bits[idx] ^= 1;
        this.ones++;
    }
};
Bitset.prototype.unfix = function(idx) {
    if (this.bits[idx] !== this.flipped) {
        this.bits[idx] ^= 1;
        this.ones--;
    }
};
Bitset.prototype.flip = function() {
    this.flipped ^= 1;
    this.ones = this.size - this.ones;
};
Bitset.prototype.all = function() {
    return this.ones === this.size;
};
Bitset.prototype.one = function() {
    return this.ones > 0;
};
Bitset.prototype.count = function() {
    return this.ones;
};
Bitset.prototype.toString = function() {
    const res = new Array(this.size);
    for (let i = 0; i < this.size; i++) {
        res[i] = this.bits[i] ^ this.flipped;
    }
    return res.join('');
};
