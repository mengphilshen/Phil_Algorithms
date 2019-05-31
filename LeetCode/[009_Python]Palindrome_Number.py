class Solution:

    """
    Determine whether an integer is a palindrome
    @param x an integer
    @return is a palindrome or not
    """

    # Revert half of the number
    def isPalindrome(self, x):       
        if (x < 0 or (x != 0 and x % 10 == 0 )):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return (x == rev or x == rev//10)
    # Time Complexity: O(log10(n))
    # Space Complexity: O(1)


