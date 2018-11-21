# -*- coding: utf-8 -*-
"""

Project: LeetCode
Program: 7_Reverse_Integer
Function:
Dependencies:	
Dependents:
Outputs:
Author:
Version:
Comments:
Revisions:

"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result, x_remaining = 0, abs(x)
        while x_remaining:
            result = result * 10 + x_remaining % 10
            x_remaining //= 10
        return -result if x < 0 else result


"""

Time Complexity: O(n)
Space Complexity:

"""