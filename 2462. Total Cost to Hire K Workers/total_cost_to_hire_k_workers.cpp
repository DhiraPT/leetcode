class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        if (costs.size() == k) {
            return accumulate(costs.begin(), costs.end(), 0LL);
        }

        long long total_cost = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        int left = 0, right = costs.size() - 1;
        while (left < candidates) {
            pq.push(make_pair(costs[left], false));
            left++;
        }
        while (right >= max(candidates, static_cast<int>(costs.size()) - candidates)) {
            pq.push(make_pair(costs[right], true));
            right--;
        }

        while (k-- > 0) {
            pair<int, int> w = pq.top();
            pq.pop();
            total_cost += w.first;
            if (left <= right) {
                if (!w.second) {
                    pq.push(make_pair(costs[left], false));
                    left++;
                } else {
                    pq.push(make_pair(costs[right], true));
                    right--;
                }
            }
        }

        return total_cost;
    }
};