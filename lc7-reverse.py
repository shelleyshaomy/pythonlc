
class Solution(object):
    def __init__(self) -> None:
        pass

    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
        
        
        if x>=0:
            x_str = str(x)
            r_str = x_str[::-1]
            rev =  int(r_str)
        else:
            x_str = str(x)[1:]
            r_str = x_str[::-1]
            rev = -int(r_str)
        
        if rev > pow(2,31)-1 or rev < -pow(2,31):
            return 0
        else:
            return rev

S = Solution()
S.reverse(124)




# int(32.9) = 32

# SOLUTION2: not good enough because the env doesn't allow exceed 32 bit
# class Solution:
#     def reverse(self, x):
#         if x < 0:
#             return -1 * self.reverseUtil(-x)
#         return self.reverseUtil(x)
        
#     def reverseUtil(self, x):
#         result = 0
#         while x != 0:
#             digit = x % 10
#             result = result * 10 + digit
#             x = int(x / 10)
			
#         return 0 if result > pow(2, 31) - 1 or result < -pow(2, 31) else result


# solution3: modify the constraint condition check.
# class Solution:
#     def reverse(self, x):
#         result, sign = 0, (-1 if x<0 else 1)
#         x = x*sign
#         while x > 0:
#             digit = x%10
#             if (sign*result > (2**31)//10) or (sign*result == (2**31)//10 and digit > 7):
#                 return 0
#             if (sign*result < (-2**31)//10) or (sign*result == (-2**31)//10 and digit < -8):
#                 return 0
#             result = result*10 + digit;
#             x = x//10
#         return sign*result
