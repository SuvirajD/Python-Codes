import math


x = input('Enter the number of decimal places till which you want the value of "e" (0-15):\n')
y = int(x)

if y >= 0 and y <= 15:
    z = round(math.e,y)
    print(z)
else:
    print('Number out of range!!')  # Can achieve asking for input until condition satisfied using another loop.


