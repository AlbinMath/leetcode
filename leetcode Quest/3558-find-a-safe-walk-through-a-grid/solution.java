import java.util.*;

class Solution {
    public boolean findSafeWalk(List<List<Integer>> grid, int health) {
        int m = grid.size();
        int n = grid.get(0).size();

        // best[i][j] = maximum health remaining when reaching (i, j)
        int[][] best = new int[m][n];

        for (int[] row : best) {
            Arrays.fill(row, -1);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(b[2], a[2])
        );

        // Starting cell also costs health if it is unsafe
        int startHealth = health - grid.get(0).get(0);

        if (startHealth <= 0) {
            return false;
        }

        best[0][0] = startHealth;
        pq.offer(new int[]{0, 0, startHealth});

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();

            int r = cur[0];
            int c = cur[1];
            int currentHealth = cur[2];

            // Ignore an outdated state
            if (currentHealth < best[r][c]) {
                continue;
            }

            if (r == m - 1 && c == n - 1) {
                return true;
            }

            for (int k = 0; k < 4; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];

                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    continue;
                }

                int newHealth =
                    currentHealth - grid.get(nr).get(nc);

                // Health must remain positive
                if (newHealth <= 0) {
                    continue;
                }

                if (newHealth > best[nr][nc]) {
                    best[nr][nc] = newHealth;
                    pq.offer(new int[]{nr, nc, newHealth});
                }
            }
        }

        return false;
    }
}
