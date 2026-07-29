class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        int n = nums.length;
        //left of i
        int left = 1;
        int prefix[] = new int[nums.length];

        for(int i=0;i<n;i++){
            left*=nums[i];
            prefix[i]=left;
        }
        //right
        int right=1;
        int[] suffix = new int[nums.length];
        for(int i=n-1;i>=0;i--){
            right*=nums[i];
            suffix[i]=right;
        }
        output[0] = 1*suffix[1];
        
        for(int i=1;i<n-1;i++){
            output[i]=suffix[i+1]*prefix[i-1];
        }
        output[n-1] = prefix[n-2] * 1;
       
        return output;
        
    }
}  
