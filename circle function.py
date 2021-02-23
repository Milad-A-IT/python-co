"""
def weird(x, y, z):  #function definition
    print((x**x + y**z) // z ) # code block

weird(5,6,7) #function call with passed parameters
"""
def weird(x, y, z):  #function definition
    output = ((x**x + y**z) // z ) # code block
    return output
some_number = weird(5,6,7)
print("some_number:" , some_number)
 #function call with passed parameters