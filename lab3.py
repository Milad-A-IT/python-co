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

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird




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


