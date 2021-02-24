tup = (1, 2, 3, 4, 5)   #immutable cannot be change
a,b,c,d,e = tup
print(a)
print(b)
print(type(tup))

output = tup[2]
print(output)


#tup[2] = 5    can not be change


set_of_unique_numbers = set([1,1,1,1,1,1,2,2,2,3,3,3,4,4,5,6,7]) #we cannot iterate data set
print(set_of_unique_numbers)