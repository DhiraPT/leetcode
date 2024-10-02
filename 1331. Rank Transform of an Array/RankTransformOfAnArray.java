class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int[] ranks = new int[arr.length];

        if (arr.length == 0) {
            return ranks;
        }

        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);

        HashMap<Integer, Integer> rankMap = new HashMap<>();
        int rank = 1;
        for (int num : sortedArr) {
            if (!rankMap.containsKey(num)) {
                rankMap.put(num, rank++);
            }
        }

        for (int i = 0; i < arr.length; i++) {
            ranks[i] = rankMap.get(arr[i]);
        }

        return ranks;
    }
}