#import math

#result = math.sqrt(3) ** 2
#print(result)
#1: 1**3
#2: 2**3
#3: 3**3
#4: 4**3   
#5: 5**3   
total = 0    
n = int(input("Enter number: "))
for x in range(1, n+1):
    cube = x**3
    print(cube, end=" , ")
    total = total + cube
    print("Total: ", total)