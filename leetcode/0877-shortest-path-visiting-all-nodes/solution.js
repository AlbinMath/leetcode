/**
 * @param {number[][]} graph
 * @return {number}
 */
var shortestPathLength = function (graph) {
  const n = graph.length;
  if (n === 1) return 0;

  const full = (1 << n) - 1;
  const visited = Array.from({ length: n }, () => new Array(1 << n).fill(false));

  let queue = [];
  for (let i = 0; i < n; i++) {
    visited[i][1 << i] = true;
    queue.push([i, 1 << i]);
  }

  let steps = 0;
  while (queue.length > 0) {
    steps++;
    const next = [];
    for (const [node, mask] of queue) {
      for (const nb of graph[node]) {
        const newMask = mask | (1 << nb);
        if (newMask === full) return steps;
        if (!visited[nb][newMask]) {
          visited[nb][newMask] = true;
          next.push([nb, newMask]);
        }
      }
    }
    queue = next;
  }

  return -1;
};
