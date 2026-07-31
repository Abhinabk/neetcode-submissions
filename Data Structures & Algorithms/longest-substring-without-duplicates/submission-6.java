class Solution {
    public int lengthOfLongestSubstring(String s) {
       Map<Character,Integer> set = new HashMap<>();
       int maxLength = 0; 
       int windowStart = 0;
       for(var i =0;i< s.length();i++){
        if(set.containsKey(s.charAt(i))){
            windowStart = Math.max(windowStart,set.get(s.charAt(i))+1);
        }
        set.put(s.charAt(i),i);
        maxLength = Math.max(maxLength,i-windowStart+1);
       }
       return maxLength;

    }

}
