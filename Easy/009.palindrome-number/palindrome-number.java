class Solution {
    public boolean isPalindrome(int x) {
        if( x < 0 || (x != 0 && x % 10 == 0)){
            return false;
        }
        
        int reverse = 0;
        while(x > reverse){
            reverse = x % 10 + reverse * 10;
            x /= 10;
        }
    
        return x == reverse || x == reverse/10;
        
    }
}