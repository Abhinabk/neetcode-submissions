class Solution {
    public int lengthOfLongestSubstring(String s) {
       Set<Character> set = new HashSet<>();
       int maxLength = 0; 
       int windowStart = 0;
       for(var i =0;i< s.length();i++){
        while(set.contains(s.charAt(i))){
            set.remove(s.charAt(windowStart));
            windowStart++;
        }
        set.add(s.charAt(i));
        maxLength = Math.max(maxLength,i-windowStart+1);
       }
       return maxLength;

    }

}
