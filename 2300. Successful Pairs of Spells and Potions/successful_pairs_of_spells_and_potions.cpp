class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        vector<int> res(spells.size());

        for (int i = 0; i < spells.size(); i++) {
            long long min_strength = (success + spells[i] - 1) / spells[i];
            res[i] = potions.end() - lower_bound(potions.begin(), potions.end(), min_strength);
        }

        return res;
    }
};