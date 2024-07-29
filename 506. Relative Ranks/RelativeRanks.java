class Solution {
    public String[] findRelativeRanks(int[] score) {
        int N = score.length;
        int maxScore = findMax(score);

        int[] indices = new int[maxScore + 1];
        for (int i = 0; i < N; i++) {
            indices[score[i]] = i + 1;
        }

        String[] res = new String[N];
        int rank = 1;

        for (int i = maxScore; i >= 0; i--) {
            if (indices[i] != 0) {
                int index = indices[i] - 1;
                switch (rank) {
                    case 1:
                        res[index] = "Gold Medal";
                        break;
                    case 2:
                        res[index] = "Silver Medal";
                        break;
                    case 3:
                        res[index] = "Bronze Medal";
                        break;
                    default:
                        res[index] = Integer.toString(rank);
                        break;
                }
                rank++;
            }
        }

        return res;
    }

    int findMax(int[] arr) {
        int max = arr[0];
        for (int a : arr) {
            if (a > max) {
                max = a;
            }
        }
        return max;
    }
}
