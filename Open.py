print("hello")
#How to swap 2 variable with the help of 3rd  variable .
a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
C=a
a=b
b=C
print("a is :",a," b is :",b)

#How to swap 2 variable without the help of 3rd  variable .
a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is :",a," b is :",b)


#How to swap 3 variable without help of 4th variable.

a = int(input())
b = int(input())
c = int(input())
a = a + b + c
b = a - b-c
c = a - b-c
a = a - b-c
print("After swapping a = ",a,", b = ",b,", c = ",c) 


