//Binary search solution
class Solution69 {
    public int mySqrt(int x) {
        int left = 1;
        int right = x;
        
        int guess = 0;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            
            if (middle <= x / middle) {
                left = middle + 1;
                guess = middle;
            } else {
                right = middle - 1;
            }
        }
        return guess;
    }
}