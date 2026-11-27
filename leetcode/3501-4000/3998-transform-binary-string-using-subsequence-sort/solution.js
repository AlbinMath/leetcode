
var transformStr = function(s, strs) {
    const n = s.length;

    let totalOnes = 0;

    for (let i = 0; i < n; i++) {
        if (s[i] === '1') totalOnes++;
    }

    const ans = [];

    for (const pattern of strs) {
        let fixedOnes = 0;
        let questionMarks = 0;

        for (let i = 0; i < n; i++) {
            if (pattern[i] === '1') {
                fixedOnes++;
            } else if (pattern[i] === '?') {
                questionMarks++;
            }
        }

        const needed = totalOnes - fixedOnes;

        if (needed < 0 || needed > questionMarks) {
            ans.push(false);
            continue;
        }

        let remaining = needed;
        let sourceOnes = 0;
        let targetOnes = 0;
        let possible = true;

        const wildcardOnes = new Array(n).fill(false);

        for (let i = n - 1; i >= 0 && remaining > 0; i--) {
            if (pattern[i] === '?') {
                wildcardOnes[i] = true;
                remaining--;
            }
        }

        for (let i = 0; i < n; i++) {
            if (s[i] === '1') sourceOnes++;

            if (pattern[i] === '1' || wildcardOnes[i]) {
                targetOnes++;
            }

            if (targetOnes > sourceOnes) {
                possible = false;
                break;
            }
        }

        ans.push(possible);
    }

    return ans;
};

