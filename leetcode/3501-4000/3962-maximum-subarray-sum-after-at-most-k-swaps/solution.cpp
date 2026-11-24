class Solution {
    int n, LOG;
    vector<long long> val; // value by rank (1-indexed)
    struct BIT {
        vector<int> c; vector<long long> s;
    };
    void upd(BIT &b, int i, int dc, long long ds) {
        for (; i <= n; i += i & -i) { b.c[i] += dc; b.s[i] += ds; }
    }
    // returns k-th smallest value (k>=1); sumOut = sum of k smallest
    long long kth(const BIT &b, int k, long long &sumOut) {
        int pos = 0; long long acc = 0;
        for (int pw = LOG; pw > 0; pw >>= 1) {
            int np = pos + pw;
            if (np <= n && b.c[np] < k) {
                pos = np; k -= b.c[np]; acc += b.s[np];
            }
        }
        sumOut = acc + val[pos + 1];
        return val[pos + 1];
    }
public:
    long long maxSum(vector<int>& nums, int k) {
        n = nums.size();
        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);
        sort(idx.begin(), idx.end(), [&](int a, int b) {
            return nums[a] != nums[b] ? nums[a] < nums[b] : a < b;
        });
        vector<int> rk(n);
        val.assign(n + 2, 0);
        for (int i = 0; i < n; i++) { rk[idx[i]] = i + 1; val[i + 1] = nums[idx[i]]; }
        LOG = 1; while (LOG * 2 <= n) LOG *= 2;

        BIT full{vector<int>(n + 1, 0), vector<long long>(n + 1, 0)};
        for (int i = 1; i <= n; i++) {
            full.c[i] += 1; full.s[i] += val[i];
            int j = i + (i & -i);
            if (j <= n) { full.c[j] += full.c[i]; full.s[j] += full.s[i]; }
        }
        long long totalAll = 0;
        for (int x : nums) totalAll += x;

        long long ans = LLONG_MIN;
        BIT in{vector<int>(n + 1, 0), vector<long long>(n + 1, 0)};
        BIT out = full;
        for (int l = 0; l < n; l++) {
            fill(in.c.begin(), in.c.end(), 0);
            fill(in.s.begin(), in.s.end(), 0);
            out = full;
            long long inSum = 0, outSum = totalAll;
            int t = 0;
            for (int r = l; r < n; r++) {
                int x = nums[r];
                upd(in, rk[r], 1, x);
                upd(out, rk[r], -1, -x);
                inSum += x; outSum -= x;
                int I = r - l + 1, O = n - I;
                int m = min(k, min(I, O));
                long long d;
                // cond(j): j-th largest outside > j-th smallest inside
                auto cond = [&](int j) {
                    return kth(out, O - j + 1, d) > kth(in, j, d);
                };
                if (t > m) t = m;
                while (t < m && cond(t + 1)) t++;
                while (t > 0 && !cond(t)) t--;

                long long gain = 0;
                if (t > 0) {
                    long long sIn, smallOut = 0;
                    kth(in, t, sIn);
                    if (O - t > 0) kth(out, O - t, smallOut);
                    gain = (outSum - smallOut) - sIn;
                }
                ans = max(ans, inSum + gain);
            }
        }
        return ans;
    }
};
