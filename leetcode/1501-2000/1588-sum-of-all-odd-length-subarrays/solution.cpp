
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        int n = arr.size();
        int sum = 0;

        for (int i = 0; i < n; i++) {
            int total = (i + 1) * (n - i);
            int odd = (total + 1) / 2;

            sum += arr[i] * odd;
        }

        return sum;
    }
};

