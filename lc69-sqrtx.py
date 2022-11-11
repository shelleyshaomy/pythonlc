
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
#runtime error
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        for i in range(1,x+1):
            if i * i == x:
                return i
            elif i * i > x:
                return (i-1)

#binary
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1: return x
        max = x;
        min = 0;
        q = (min+max)//2;
        
        while(min < max):
            
            c = q * q;
            if c == x: 
                return q;
            elif c < x: 
                min = q+1;
            else: 
                max=q;
            q = (min+max)//2;
            
        return q-1 ;
    
