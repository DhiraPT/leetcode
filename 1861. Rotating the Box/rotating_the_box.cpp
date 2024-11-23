class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m = box.size(), n = box[0].size();
        vector<vector<char>> rotated_box(n, vector<char>(m, '.'));

        for (int i = 0; i < m; ++i) {
            int empty = -1;

            for (int j = n - 1; j >= 0; --j) {
                if (empty == -1) {
                    if (box[i][j] == '.') {
                        empty = j;
                    }
                } else if (box[i][j] == '#') {
                    box[i][empty] = '#';
                    box[i][j] = '.';
                    --empty;
                } else if (box[i][j] == '*') {
                    empty = -1;
                }
            }

            for (int j = 0; j < n; ++j) {
                rotated_box[j][m-i-1] = box[i][j];
            }
        }

        return rotated_box;
    }
};