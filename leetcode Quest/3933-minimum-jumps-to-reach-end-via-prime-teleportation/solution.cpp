class Solution {
public:
    int minJumps(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;

        int mx = *max_element(nums.begin(), nums.end());

        // Smallest Prime Factor (SPF)
        vector<int> spf(mx + 1);
        for (int i = 0; i <= mx; i++)
            spf[i] = i;

        for (int i = 2; i * i <= mx; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= mx; j += i) {
                    if (spf[j] == j)
                        spf[j] = i;
                }
            }
        }

        // prime -> indices whose values are divisible by that prime
        vector<vector<int>> groups(mx + 1);

        for (int i = 0; i < n; i++) {
            int x = nums[i];

            while (x > 1) {
                int p = spf[x];
                groups[p].push_back(i);

                while (x % p == 0)
                    x /= p;
            }
        }

        vector<int> dist(n, -1);
        vector<bool> usedPrime(mx + 1, false);

        queue<int> q;
        q.push(0);
        dist[0] = 0;

        while (!q.empty()) {
            int i = q.front();
            q.pop();

            if (i == n - 1)
                return dist[i];

            // Adjacent jumps
            if (i + 1 < n && dist[i + 1] == -1) {
                dist[i + 1] = dist[i] + 1;
                q.push(i + 1);
            }

            if (i - 1 >= 0 && dist[i - 1] == -1) {
                dist[i - 1] = dist[i] + 1;
                q.push(i - 1);
            }

            // Prime teleportation
            int value = nums[i];

            // Teleportation is possible only if nums[i] itself is prime
            if (value >= 2 && spf[value] == value &&
                !usedPrime[value]) {

                usedPrime[value] = true;

                for (int j : groups[value]) {
                    if (dist[j] == -1) {
                        dist[j] = dist[i] + 1;
                        q.push(j);
                    }
                }
            }
        }

        return -1;
    }
};
