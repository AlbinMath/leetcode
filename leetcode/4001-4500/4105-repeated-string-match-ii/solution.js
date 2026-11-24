
var repeatedStringMatch = function(a, b, x, y) {
    const la = a.length;
    const lb = b.length;
    const totalA = BigInt(la) * BigInt(x);
    const totalB = BigInt(lb) * BigInt(y);

    if (totalB > totalA) return false;
    const minRepsB = Math.ceil((la + lb) / lb) + 1;
    const effY = Math.min(y, minRepsB);
    const pattern = b.repeat(effY);
    const maxOffset = Number(totalA - totalB < BigInt(la - 1) ? totalA - totalB : BigInt(la - 1));
    const neededLenA = maxOffset + pattern.length;
    const effX = Math.min(x, Math.ceil(neededLenA / la));
    const text = a.repeat(effX);
    const firstMatch = text.indexOf(pattern);
    return firstMatch !== -1 && BigInt(firstMatch) <= totalA - totalB;
};
