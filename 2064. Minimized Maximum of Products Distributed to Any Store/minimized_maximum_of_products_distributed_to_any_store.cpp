class Solution {
public:
    int minimizedMaximum(int n, vector<int>& quantities) {
        auto can_distribute = [&](int num) {
            int count = 0;
            for (int q : quantities) {
                count += (q + num - 1) / num;
            }
            return count <= n;
        };

        int low = 1, high = *std::max_element(quantities.begin(), quantities.end());

        while (low <= high) {
            int mid = (low + high) >> 1;
            if (can_distribute(mid)) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }
};