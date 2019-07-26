class Solution {
    public int reverse(int x) {
        boolean isNegative = false;
        if(x < 0){
            isNegative = true;
            x = -x;
        }
        
        long answer = 0;
        while(x != 0){
	       // may cause overflow here
            answer = answer * 10 + x % 10 ;
            x /= 10;
        }
        
        if(isNegative == true){
            answer = -answer;
        }
        
        if(answer > Integer.MAX_VALUE || answer < Integer.MIN_VALUE)
            return 0;
        else
            return (int)answer;
        
    }
}