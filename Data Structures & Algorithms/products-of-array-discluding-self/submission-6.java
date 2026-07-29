class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        int n = nums.length;
        //left of i
        int left = 1;
        for(int i=0;i<n;i++){
            output[i] = left;
            left = left*nums[i];
        }
        //right
        int right=1;
        for(int i=n-1;i>=0;i--){
            output[i] *=right;
            right*=nums[i];
        }
        return output;
        
    }
}  
