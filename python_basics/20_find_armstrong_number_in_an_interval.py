'''
A positive integer is called an Armstrong number of order n if

abcd... = an + bn + cn + dn + ...
For example,

153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.
'''

# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
