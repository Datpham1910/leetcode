class Solution {
    public int numTimesAllBlue(int[] light) {
        int max_right = 1;
        int count = 0;
        for (int i = 0; i < light.length; i++) {
            if (light[i] > max_right) max_right = light[i];
            if (max_right == i + 1) count += 1;
        }
        return count;
    }
}