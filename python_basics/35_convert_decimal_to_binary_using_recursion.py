'''
Decimal number is converted into binary by dividing the number successively by 2 and printing the remainder in reverse order.
https://www.programiz.com/python-programming/examples/decimal-binary-recursion
'''

# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = 34

convertToBinary(dec)
print()
