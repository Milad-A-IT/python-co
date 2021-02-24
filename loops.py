#list_of_numbers = [0, 1, 2, 3, "blue", 5]

#for loops
#for elem in list_of_numbers:
#   print(elem)




#for loops
#for elem in list_of_numbers:
 #   if type(elem) == str:
  #      continue
   # print(elem)



#range loop
#for i in range(5, 20, 3):
#   print(i)

#for i in range(5):
#  print(i)


#i = 0
#while i<10:
    #print(i)
    #i = i + 1
    #i += 1

#i = 0
#while True
#i += 1
#print(i)
#if i>10:
#break

#=========iteration labs from slides================
#Q1
#for i in range(5):
 # print(i)

#i = 0
#while i<8:
    #print(i)
    #i = i + 1
    #i += 1
#Q2
#x = 0
#while(x < 100):
 #   x+=2
  #  print(x)

#Q3
"""input(int("enter number"))
if N%2 == 0:
    print("weird")            
elif N >= 2 && N <= 5:
    print("not weird")
elif N >= 6 && N <= 20:
    print("weird")
else:
    print("not weird")"""

#++++++++++++++++++++++++
#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird

#import sys


N = int(input("enter number: "))

if N % 2 != 0:
    print("Weird")
else:
    if N >= 2 and N <= 5:
        print ("Not Weird")
    elif N >= 6 and N <= 20:
        print ("Weird")
    elif N > 20:
        print ("Not Weird")
#++++++++++++++++++++++++++++++++++++++++


