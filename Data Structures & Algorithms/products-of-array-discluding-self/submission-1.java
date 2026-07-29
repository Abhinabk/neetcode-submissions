class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output= new int[nums.length];
        int prevOutput;
        for(int i=0;i<nums.length;i++){
            prevOutput = 1; 
            for(int j = 0;j<nums.length;j++){
                if(i==j) continue;
                prevOutput *= nums[j]; 
            }
            output[i] = prevOutput;
        }
        return output;
    }
}  
