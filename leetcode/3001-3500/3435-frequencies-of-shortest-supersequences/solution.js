/**
 * @param {string[]} supersequences
 * @return {number[][]}
 */
var supersequences = function (words) {
    const idx = new Map();
    const letters = [];
    for (const w of words) {
        for (const ch of w) {
            if (!idx.has(ch)) {
                idx.set(ch, letters.length);
                letters.push(ch);
            }
        }
    }
    const k = letters.length;
    const inAdj = new Array(k).fill(0);
    let selfMask = 0;
    for (const w of words) {
        const a = idx.get(w[0]), b = idx.get(w[1]);
        if (a === b) selfMask |= 1 << a;
        else inAdj[b] |= 1 << a;
    }

    const full = (1 << k) - 1;
    const popcount = (x) => {
        let c = 0;
        while (x) { x &= x - 1; c++; }
        return c;
    };

    const acyclic = (rem) => {
        let changed = true;
        while (rem && changed) {
            changed = false;
            for (let v = 0; v < k; v++) {
                if ((rem >> v) & 1 && (inAdj[v] & rem) === 0) {
                    rem &= ~(1 << v);
                    changed = true;
                }
            }
        }
        return rem === 0;
    };

    let best = Infinity;
    let masks = [];
    for (let mask = 0; mask <= full; mask++) {
        if ((mask & selfMask) !== selfMask) continue;
        const pc = popcount(mask);
        if (pc > best) continue;
        if (!acyclic(full & ~mask)) continue;
        if (pc < best) {
            best = pc;
            masks = [];
        }
        masks.push(mask);
    }

    return masks.map((mask) => {
        const f = new Array(26).fill(0);
        for (let i = 0; i < k; i++) {
            f[letters[i].charCodeAt(0) - 97] = (mask >> i) & 1 ? 2 : 1;
        }
        return f;
    });
};
