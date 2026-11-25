var canMakePalindromeQueries = function(s, queries) {
    const n = s.length;
    const m = n / 2;
    const left = s.slice(0, m);
    const right = s.slice(m).split('').reverse().join('');
    const prefL = Array.from(
        { length: 26 },
        () => new Int32Array(m + 1)
    );
    const prefR = Array.from(
        { length: 26 },
        () => new Int32Array(m + 1)
    );
    const mismatch = new Int32Array(m + 1);
    for (let i = 0; i < m; i++) {
        const x = left.charCodeAt(i) - 97;
        const y = right.charCodeAt(i) - 97;
        for (let c = 0; c < 26; c++) {
            prefL[c][i + 1] = prefL[c][i];
            prefR[c][i + 1] = prefR[c][i];
        }
        prefL[x][i + 1]++;
        prefR[y][i + 1]++;
        mismatch[i + 1] =
            mismatch[i] + (x !== y ? 1 : 0);
    }
    const getCount = (pref, c, l, r) => {
        if (l > r) return 0;
        return pref[c][r + 1] - pref[c][l];
    };
    const getMismatch = (l, r) => {
        if (l > r) return 0;
        return mismatch[r + 1] - mismatch[l];
    };
    const answer = [];
    for (const [a, b, c, d] of queries) {
        const l2 = n - 1 - d;
        const r2 = n - 1 - c;
        const start = Math.max(a, l2);
        const end = Math.min(b, r2);
        let bad = mismatch[m];
        bad -= getMismatch(a, b);
        bad -= getMismatch(l2, r2);
        if (start <= end) {
            bad += getMismatch(start, end);
        }
        if (bad !== 0) {
            answer.push(false);
            continue;
        }
        let valid = true;
        for (let ch = 0; ch < 26; ch++) {
            const leftAvailable =
                getCount(prefL, ch, a, b);
            const rightFixed =
                getCount(prefR, ch, a, b) -
                getCount(prefR, ch, start, end);
            const rightAvailable =
                getCount(prefR, ch, l2, r2);
            const leftFixed =
                getCount(prefL, ch, l2, r2) -
                getCount(prefL, ch, start, end);
            const remainingLeft =
                leftAvailable - rightFixed;

            const remainingRight =
                rightAvailable - leftFixed;
            if (
                remainingLeft < 0 ||
                remainingRight < 0 ||
                remainingLeft !== remainingRight
            ) {
                valid = false;
                break;
            }
        }
        answer.push(valid);
    }
    return answer;
};

