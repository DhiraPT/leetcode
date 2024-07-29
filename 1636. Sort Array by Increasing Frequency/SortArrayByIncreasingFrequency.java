class Solution {
    public int[] frequencySort(int[] nums) {
        int[] f = new int[201];
        for (int num : nums) {
            f[num + 100]++;
        }

        Integer[] numsArr = Arrays.stream(nums).boxed().toArray(Integer[]::new);

        Arrays.sort(numsArr, (a, b) -> {
            if (f[a+100] == f[b+100]) {
                return Integer.compare(b, a);
            }
            return Integer.compare(f[a+100], f[b+100]);
        });

        return Arrays.stream(numsArr).mapToInt(Integer::intValue).toArray();
    }
}
