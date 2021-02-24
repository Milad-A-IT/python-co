"""
def weird(x, y, z):  #function definition
    print((x**x + y**z) // z ) # code block

weird(5,6,7) #function call with passed parameters
"""
#=========================================================
"""def weird(x, y, z):  #function definition
    output = ((x**x + y**z) // z ) # code block
    return output
some_number = weird(5,6,7)
print("some_number:" , some_number)"""
#==================================================================
"""PI = 3.14

radius = float(input(' Please Enter the radius of a circle: '))
area = PI * radius * radius
circumference = 2 * PI * radius
 
print(" Area Of a Circle = %.2f" %area)
print(" Circumference Of a Circle = %.2f" %circumference)"""
#================================================================
# Python program to find Area of a circle 

def findArea(r): 
	PI = 3.142
	return PI * (r*r)

# Driver method 
print("Area is %.6f" % findArea(6)) 

# This code is contributed by Chinmoy Lenka 
#================================================================