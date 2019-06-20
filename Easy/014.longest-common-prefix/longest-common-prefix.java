class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0)
            return "";
        else if (strs.length == 1)
            return strs[0];
        
        int smallLen = strs[0].length();
        String smallStr = strs[0];
        
        for(int i = 1; i < strs.length; i++){
            smallLen = (strs[i].length() < smallLen) ? strs[i].length() : smallLen;
            smallStr = smallStr.substring(0,smallLen);
            
            for(int j = 0; j < smallLen; j++){
                if(smallStr.charAt(j) != strs[i].charAt(j)){
                    smallLen = j;
                }
            }
        }
        
        return smallStr.substring(0,smallLen);      
                
    }
}