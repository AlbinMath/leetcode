/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var checkIfPrerequisite = function (numCourses, prerequisites, queries) {
    const n = numCourses;
    const reach = Array.from({ length: n }, () => new Uint8Array(n));

    for (const [a, b] of prerequisites) reach[a][b] = 1; // a must come before b

    for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
            if (!reach[i][k]) continue;
            for (let j = 0; j < n; j++) {
                if (reach[k][j]) reach[i][j] = 1;
            }
        }
    }

    return queries.map(([u, v]) => reach[u][v] === 1);
};
