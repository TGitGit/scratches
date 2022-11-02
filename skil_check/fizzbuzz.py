class Solution(object):
    def fizzBuzz(self,n):
        for fb_num in range(1,n+1):
            if fb_num %3==0and fb_num %5==0:
               print("fizzbuzz")
            elif fb_num % 3==0:
              print("fizz")
            elif fb_num % 5==0:
              print("buzz")
            else:
              print(fb_num)
So=Solution()
So.fizzBuzz(50)