#Question 1 :

num1=float(input("enter the value of Number1: "))
num2=float(input("enter the value of Number2: "))
num3=float(input("enter the value of Number3: "))
num4=float(input("enter the value of Number4: "))
num5=float(input("enter the value of Number5: "))
Sum=num1+num2+num3+num4+num5
if num1 < 0 or num2<0 or num3<0 or num4<0 or num5<0 :
    print("enter a positive number")
else:
    print("The sum of all numbers is : ",Sum)
x=open("data.txt","a")
print("the value of number1:",num1,file=x)
print("the value of number2:",num2,file=x)
print("the value of number3:",num3,file=x)
print("the value of number4:",num4,file=x)
print("the value of number5:",num5,file=x)
print("the values of all numbers: ",Sum,file=x)



#Question 2:


Cars={}
var1 = input("enter a brandname: ")
var2 = input("enter the color: ")
Cars[var1] = var2
x=open("data.txt","a")
print("the details: ",Cars,file=x)
print(Cars)