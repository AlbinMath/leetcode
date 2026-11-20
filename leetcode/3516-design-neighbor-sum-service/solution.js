var NeighborSum = function(grid) {
    this.grid = grid;
    this.n = grid.length;
    this.pos = new Array(this.n * this.n);
    
    for (let r = 0; r < this.n; r++) {
        for (let c = 0; c < this.n; c++) {
            this.pos[grid[r][c]] = [r, c];
        }
    }
};
NeighborSum.prototype._sumNeighbors = function(value, dirs) {
    const [r, c] = this.pos[value];
    let total = 0;
    
    for (const [dr, dc] of dirs) {
        const nr = r + dr;
        const nc = c + dc;
        if (nr >= 0 && nr < this.n && nc >= 0 && nc < this.n) {
            total += this.grid[nr][nc];
        }
    }
    return total;
};
NeighborSum.prototype.adjacentSum = function(value) {
    return this._sumNeighbors(value, [[-1, 0], [1, 0], [0, -1], [0, 1]]);
};
NeighborSum.prototype.diagonalSum = function(value) {
    return this._sumNeighbors(value, [[-1, -1], [-1, 1], [1, -1], [1, 1]]);
};
