# function for add two numbers

def add(x,y):
    return x + y

# function for subtracts two numbers

def sub(x,y):
    return x - y

#function for multiplies two numbers

def mul(x,y):
    return x * y

#function for divides two numbers

def div(x,y):
    return x / y

#write print for select opeartion

print("Seclect operation")
print("+.ADD")
print("-.Subtract")
print("*.Multiplies")
print("/.Divides")

#write to get user input numbers

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))


#for select to opeaterion input

oper = input("Enter oper(+/-/*///): ")

#calculatasion with caling function

if oper == '+':
    print(num1,"+",num2,"=",add(num1,num2))

elif oper == '-':
    print(num1,"-",num2,"=",sub(num1,num2))

elif oper == " * ":
   print(num1," * ",num2,"=",mul(num1,num2))

elif oper == "/":
    print(num1,"/",num2,"=",div(num1,num2))

else:
    print("Invalid input!!!")
