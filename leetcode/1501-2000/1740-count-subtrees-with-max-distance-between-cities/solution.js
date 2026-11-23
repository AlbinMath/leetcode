/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var countSubgraphsForEachDiameter = function (n, edges) {
  const INF = 1e9;
  const dist = Array.from({ length: n }, (_, i) =>
    Array.from({ length: n }, (_, j) => (i === j ? 0 : INF))
  );
  for (const [u, v] of edges) {
    dist[u - 1][v - 1] = 1;
    dist[v - 1][u - 1] = 1;
  }
  for (let k = 0; k < n; k++)
    for (let i = 0; i < n; i++)
      for (let j = 0; j < n; j++)
        if (dist[i][k] + dist[k][j] < dist[i][j])
          dist[i][j] = dist[i][k] + dist[k][j];

  const ans = new Array(n - 1).fill(0);

  for (let mask = 1; mask < 1 << n; mask++) {
    let size = 0;
    for (let x = mask; x; x &= x - 1) size++;
    if (size < 2) continue;

    let inside = 0;
    for (const [u, v] of edges) {
      if (mask & (1 << (u - 1)) && mask & (1 << (v - 1))) inside++;
    }
    if (inside !== size - 1) continue;

    let diameter = 0;
    for (let i = 0; i < n; i++) {
      if (!(mask & (1 << i))) continue;
      for (let j = i + 1; j < n; j++) {
        if (mask & (1 << j)) diameter = Math.max(diameter, dist[i][j]);
      }
    }
    ans[diameter - 1]++;
  }

  return ans;
};
