class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        List<Integer> res = new ArrayList<>();

        for (int r = 0; r < m; r++) {
            int minVal = matrix[r][0];
            int minCol = 0;

            for (int c = 1; c < n; c++) {
                if (matrix[r][c] < minVal) {
                    minVal = matrix[r][c];
                    minCol = c;
                }
            }

            boolean isLucky = true;
            for (int i = 0; i < m; i++) {
                if (matrix[i][minCol] > minVal) {
                    isLucky = false;
                    break;
                }
            }

            if (isLucky) {
                res.add(minVal);
                break;
            }
        }

        return res;
    }
}
