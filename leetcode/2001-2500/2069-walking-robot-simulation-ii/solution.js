
var Robot = function(width, height) {
    this.cells = [];
    this.dirs = [];
    this.pos = 0;
    this.moved = false;
    for (let x = 0; x < width; x++) {
        this.cells.push([x, 0]);
        this.dirs.push("East");
    }
    for (let y = 1; y < height; y++) {
        this.cells.push([width - 1, y]);
        this.dirs.push("North");
    }
    for (let x = width - 2; x >= 0; x--) {
        this.cells.push([x, height - 1]);
        this.dirs.push("West");
    }
    for (let y = height - 2; y >= 1; y--) {
        this.cells.push([0, y]);
        this.dirs.push("South");
    }
    this.dirs[0] = "South";
};
Robot.prototype.step = function(num) {
    this.moved = true;
    this.pos = (this.pos + num) % this.cells.length;
};
Robot.prototype.getPos = function() {
    return this.cells[this.pos];
};
Robot.prototype.getDir = function() {
    if (!this.moved) return "East";
    return this.dirs[this.pos];
};
