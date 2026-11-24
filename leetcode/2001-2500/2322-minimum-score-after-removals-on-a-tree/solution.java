import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<List<Integer>> adj;
    private int[] subXor, tin, tout;
    private int timer = 0;

    public int minimumScore(int[] nums, int[][] edges) {
        int n = nums.length;
        adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }

        subXor = new int[n];
        tin = new int[n];
        tout = new int[n];

        dfs(0, -1, nums);
        int totalXor = subXor[0];
        int ans = Integer.MAX_VALUE;

        for (int u = 1; u < n; u++) {
            for (int v = u + 1; v < n; v++) {
                int a, b, c;
                if (tin[u] < tin[v] && tout[v] <= tout[u]) {
                    a = subXor[v];
                    b = subXor[u] ^ subXor[v];
                    c = totalXor ^ subXor[u];
                } else if (tin[v] < tin[u] && tout[u] <= tout[v]) {
                    a = subXor[u];
                    b = subXor[v] ^ subXor[u];
                    c = totalXor ^ subXor[v];
                } else {
                    a = subXor[u];
                    b = subXor[v];
                    c = totalXor ^ subXor[u] ^ subXor[v];
                }
                int mx = Math.max(a, Math.max(b, c));
                int mn = Math.min(a, Math.min(b, c));
                ans = Math.min(ans, mx - mn);
            }
        }
        return ans;
    }

    private void dfs(int u, int parent, int[] nums) {
        tin[u] = ++timer;
        int val = nums[u];
        for (int v : adj.get(u)) {
            if (v != parent) {
                dfs(v, u, nums);
                val ^= subXor[v];
            }
        }
        subXor[u] = val;
        tout[u] = timer;
    }
}
