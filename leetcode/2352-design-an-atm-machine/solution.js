var ATM = function() {
    this.denoms = [20, 50, 100, 200, 500];
    this.counts = [0, 0, 0, 0, 0];
};
ATM.prototype.deposit = function(banknotesCount) {
    for (let i = 0; i < 5; i++) {
        this.counts[i] += banknotesCount[i];
    }
};

ATM.prototype.withdraw = function(amount) {
    const used = [0, 0, 0, 0, 0];
    for (let i = 4; i >= 0; i--) {
        const take = Math.min(this.counts[i], Math.floor(amount / this.denoms[i]));
        used[i] = take;
        amount -= take * this.denoms[i];
    }
    if (amount !== 0) {
        return [-1];
    }
    for (let i = 0; i < 5; i++) {
        this.counts[i] -= used[i];
    }
    
    return used;
};
