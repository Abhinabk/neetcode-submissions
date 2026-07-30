class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int maxP = 0;
        for(int right = 1;right<prices.length;right++){
            if(prices[right]<prices[left]){
                //so there is a lowe price we can buy at
                left = right;
                continue;
            }
            else if(prices[right]>=prices[left]){
                //we can try an d sell to see thg eprofit
                int currP = prices[right]-prices[left];
                maxP = currP>maxP?currP:maxP;
            }
        }
        return maxP;
        
    }
}
