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



"""
N = int(input("enter number: "))

if N % 2 != 0:
    print("Weird")
else:
    if N >= 2 and N <= 5:
        print ("Not Weird")
    elif N >= 6 and N <= 20:
        print ("Weird")
    elif N > 20:
        print ("Not Weird")    """
#++++++++++++++++++++++++++++++++++++++++
#Q4
"""(Medium) Write a function that takes an array of integers and places the zeroes in the center of the array.
 All non-zero integers should keep their relative position. For the purpose of this question, center is defined as floor(length of array / 2).
 center_zeros([1, 1, 3, 0, 6, 0]) -> [1, 1, 0, 0, 3, 6]"""
""" from math import floor


def center_zeros(array):
    # write your function here
    # center means the floor(x / 2) where floor means rounding a float (decimal number) down to the nearest integer
    # i.e. floor(1) = 1, floor(1.5) = 1, floor(1.75) = 1, floor(2) = 2
    pass


if __name__ == "__main__":
    # write your debug code here
    pass"""

"""from question2 import center_zeros


def test_1():
    assert center_zeros([0, 3, 1]) == [3, 0, 1]


def test_2():
    assert center_zeros([1, 1, 3, 0]) == [1, 1, 0, 3]


def test_3():
    assert center_zeros([1, 1, 3, 0, 6, 0]) == [1, 1, 0, 0, 3, 6]


def test_4():
    assert center_zeros([0, 0, 1]) == [0, 0, 1]


def test_5():
    assert center_zeros([]) == []


"""
"""#Q5
(Warm-up) Write a function that selects the maximum value from an array of integers.
 Do not use any built-in max functions. select_max([1, 2, 3, 4]) -> 4

 def select_max(array):
        # write your function here
    # do NOT use the built-in max() function
    pass


if __name__ == "__main__":
    # write your debug code here
    pass"""

#Q6

"""def printValues(l):
        l = list()
for i in range(1,21):
	l.append(i**2)
	print(l)
		
printValues(l)"""
#===========================================================
"""#fibonnaci numbers less than 1000
x,y=0,1

while y<1000:
    print(y)
    x,y = y,x+y
"""