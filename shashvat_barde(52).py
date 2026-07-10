#basic program
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
sum = a + b
print("Addition of two given numbers is:", sum)

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
area = length * breadth
print("area of reactangle is:" , area)

a = int(input("Enter number: "))
if a % 2 == 0:
    print("number is even")
else :
    print("number is odd ")

#conditionalstatement
a = int(input("Enter number: "))
if a < 0:
    print("number is negative")
elif a > 0:
    print("number is positive")
else :
    print("number is zero")


year = int(input("Enter year: "))
if year % 4 == 0:
    print("Its a leap year")
else :
    print("not a leap year")


a = input("Enter a character in small alphabet only : ")
if a == "a" or a == "e" or a == "i" or a =="o" or a == "u":
    print(" leter is vowel")
else :
    print("letter is consonent")


#loop
for i in range(1,101):
    print(i)

num = int(input("Enter a number: "))
fact = 1 
for i in range(1,num+1):
    fact = fact*i
print("factorial is" , fact)

#strings
string = input("enter a string : ")
revers = string[::-1]
print("reverse string is :", revers)

#list
list = [10,9,11,13,14]
list.sort()
print("sorted list in ascending order is ", list)

#functions
list = [10,9,11,13,14]
list.sort()
print("sorted list in ascending order is ", list)

#dictionaries
dict1 = {"city":"mumbai"}
dict2 = {"state":"maharashtra"}
dict1.update(dict2)
print(dict1)

#file handling
file = open("shash.txt","w")
file.write("Hi this is shashvats file")
file.close()

#exceptionhandling
a = int(input("first number: "))
b = int(input("Enter second number: "))
if b == 0:
    raise ZeroDivisionError("division by zero not possible")
print("result", a/b)
