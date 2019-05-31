class Solution {

    /**
     * Given a 32-bit signed integer, reverse digits of an integer
     * @param x an integer
     * @return reverse digits of an integer
     */

    // Pop and Push Digits
    public int reverseInteger(int x) {
        long rev = 0;
        while (x != 0) {
            rev = rev * 10 + x % 10;
            x /= 10; 
        }
        if (rev >= Integer.MIN_VALUE && rev <= Integer.MAX_VALUE)
            return (int)rev;
        else
            return 0;
    }
    // Time Complexity: O(log10(n))
    // Space Complexity: O(1)
 
}


