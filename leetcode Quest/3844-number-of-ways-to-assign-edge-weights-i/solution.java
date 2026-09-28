class Solution {
    public int assignEdgeWeights(int[][] edges) {
        final int MOD = 1_000_000_007;

        int n = edges.length + 1;

        // Build adjacency list
        List<Integer>[] graph = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        // Find maximum depth from node 1
        int maxDepth = 0;

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);

        int[] depth = new int[n + 1];
        Arrays.fill(depth, -1);
        depth[1] = 0;

        while (!queue.isEmpty()) {
            int node = queue.poll();

            for (int next : graph[node]) {
                if (depth[next] == -1) {
                    depth[next] = depth[node] + 1;
                    maxDepth = Math.max(maxDepth, depth[next]);
                    queue.offer(next);
                }
            }
        }

        // For a path with d edges:
        // Number of assignments with odd sum = 2^(d-1)
        //
        // We select a node at maximum depth,
        // so the path contains maxDepth edges.

        long ans = 1;

        for (int i = 1; i < maxDepth; i++) {
            ans = (ans * 2) % MOD;
        }

        return (int) ans;
    }
}
