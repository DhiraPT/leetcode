class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        int unguarded = m * n;
        vector<vector<int>> grid(m, vector<int>(n, 0));

        for (const auto& wall : walls) {
            grid[wall[0]][wall[1]] = 3;
            --unguarded;
        }

        for (const auto& guard : guards) {
            grid[guard[0]][guard[1]] = 2;
            --unguarded;
        }

        for (const auto& guard : guards) {
            int row = guard[0], col = guard[1];
            for (int r = row + 1; r < m; ++r) {
                if (grid[r][col] >= 2) {
                    break;
                } else if (grid[r][col] == 0) {
                    grid[r][col] = 1;
                    --unguarded;
                }
            }
            for (int r = row - 1; r >= 0; --r) {
                if (grid[r][col] >= 2) {
                    break;
                } else if (grid[r][col] == 0) {
                    grid[r][col] = 1;
                    --unguarded;
                }
            }
            for (int c = col + 1; c < n; ++c) {
                if (grid[row][c] >= 2) {
                    break;
                } else if (grid[row][c] == 0) {
                    grid[row][c] = 1;
                    --unguarded;
                }
            }
            for (int c = col - 1; c >= 0; --c) {
                if (grid[row][c] >= 2) {
                    break;
                } else if (grid[row][c] == 0) {
                    grid[row][c] = 1;
                    --unguarded;
                }
            }
        }

        return unguarded;
    }
};