class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        //sort the array O(log(n))
        Arrays.sort(nums); //inplace
        
        int sum;
        List<List<Integer>> result = new ArrayList<>();
        for(int k=0;k<nums.length;k++){
            //check for duplicates preocss first skip next
            if(k>0 && nums[k]==nums[k-1])continue;
            int target = -nums[k];
            int left = k+1;
            int right = nums.length-1;
            while(left<right){
                sum = nums[left]+nums[right];
                if(sum==target){
                    result.add(Arrays.asList(nums[left],nums[right],nums[k]));
                    left++;
                    right--;
                       //check for duplicates and skip
                    while(left<right && nums[left]==nums[left-1]) left++;
                    while(right>left && nums[right]==nums[right+1]) right--;
                }
                else if(sum<target) left++;
                else right--; 
            }
        }
        return result;

    }
}
