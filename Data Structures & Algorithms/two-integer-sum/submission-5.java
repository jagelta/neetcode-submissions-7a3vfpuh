class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> set = new HashMap<>();
        int[] sol = new int[2];

        for (int i = 0; i < nums.length; i++){
            int lookFor = target - nums[i];
            if (set.containsKey(lookFor)) {
                sol[0] = set.get(lookFor);
                sol[1] = i;
            } else {
                set.put(nums[i], i);
            }



        }
        return sol;
    }
}
