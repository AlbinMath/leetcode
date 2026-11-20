
var Spreadsheet = function(rows) {
    this.cells = new Map();
};
Spreadsheet.prototype.setCell = function(cell, value) {
    this.cells.set(cell, value);
};
Spreadsheet.prototype.resetCell = function(cell) {
    this.cells.delete(cell);
};
Spreadsheet.prototype.getValue = function(formula) {
    const [x, y] = formula.slice(1).split('+');
    
    const resolve = (token) => {
        const code = token.charCodeAt(0);
        if (code >= 65 && code <= 90) {
            return this.cells.get(token) || 0;
        }
        return Number(token);
    };
    
    return resolve(x) + resolve(y);
};
