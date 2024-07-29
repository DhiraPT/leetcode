class Solution {
    public int[] sortJumbled(int[] mapping, int[] nums) {
        int n = nums.length;
        int[][] mappedNums = new int[n][2];

        for (int i = 0; i < n; i++) {
            mappedNums[i] = new int[]{nums[i], doMapping(nums[i], mapping)};
        }
        Arrays.sort(mappedNums, Comparator.comparingInt(a -> a[1]));
        for (int i = 0; i < n; i++) {
            nums[i] = mappedNums[i][0];
        }

        return nums;
    }

    int doMapping(int num, int[] mapping) {
        if (num == 0) return mapping[0];
        int newNum = 0;
        int place = 1;
        while (num != 0) {
            int digit = num % 10;
            int newDigit = mapping[digit];
            newNum += newDigit * place;
            place *= 10;
            num /= 10;
        }
        return newNum;
    }
}
