public class LeetCode1 {

    /**
     * Given an array of integers, return indices of the two numbers such that they add up to a specific target
     * @param nums an array of integers
     * @param target target number = nums[index1] + nums[index2]
     * @return [index1, index2]
     */
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++){
            for (int j = i+1; j < nums.length; j++){
                if (nums[j] == target - nums[i]){
                    return new int[] {i, j};
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }

    /*
    * Time Complexity: O(n^2)
    * Space Complexity: O(1)
    * */
}

