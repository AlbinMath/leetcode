
class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        int population[101] = {0};

        for (const auto& log : logs) {
            population[log[0] - 1950]++;
            population[log[1] - 1950]--;
        }

        int currentPopulation = 0;
        int maxPopulation = 0;
        int result = 1950;

        for (int i = 0; i < 101; i++) {
            currentPopulation += population[i];

            if (currentPopulation > maxPopulation) {
                maxPopulation = currentPopulation;
                result = 1950 + i;
            }
        }

        return result;
    }
};

