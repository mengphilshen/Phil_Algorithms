# -*- coding: utf-8 -*-
"""

Project: LintCode
Program: 37_Reverse_3-digit_Integer
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
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self,number):
        return number % 10 * 100 + number // 10 % 10 * 10 + number // 100


"""

Time Complexity: O(n)
Space Complexity:

"""