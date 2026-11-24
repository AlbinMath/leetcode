
var LUPrefix = function(n) {
    this.uploaded = new Array(n + 1).fill(false);
    this.prefix = 0;
};

LUPrefix.prototype.upload = function(video) {
    this.uploaded[video] = true;

    // Extend the prefix while the next video is uploaded
    while (
        this.prefix + 1 < this.uploaded.length &&
        this.uploaded[this.prefix + 1]
    ) {
        this.prefix++;
    }
};

LUPrefix.prototype.longest = function() {
    return this.prefix;
};

