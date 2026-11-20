var FrequencyTracker = function() {
    this.numFreq = new Map();
    this.freqCount = new Map();
};
FrequencyTracker.prototype.add = function(number) {
    const oldF = this.numFreq.get(number) || 0;
    const newF = oldF + 1;
    
    if (oldF > 0) {
        this.freqCount.set(oldF, this.freqCount.get(oldF) - 1);
    }
    
    this.numFreq.set(number, newF);
    this.freqCount.set(newF, (this.freqCount.get(newF) || 0) + 1);
};
FrequencyTracker.prototype.deleteOne = function(number) {
    const oldF = this.numFreq.get(number) || 0;
    if (oldF === 0) return;
    
    const newF = oldF - 1;
    this.freqCount.set(oldF, this.freqCount.get(oldF) - 1);
    this.numFreq.set(number, newF);
    
    if (newF > 0) {
        this.freqCount.set(newF, (this.freqCount.get(newF) || 0) + 1);
    }
};
FrequencyTracker.prototype.hasFrequency = function(frequency) {
    return (this.freqCount.get(frequency) || 0) > 0;
};
