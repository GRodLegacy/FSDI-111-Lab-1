
def say_hello():
    print("I'm a function")

def perform_sum(num1, num2):
    print('performing some operations inside a function...')
    return num1 + num2

def perform_sub(num1, num2):
    print('Subtracting numbers..')
    return num1 - num2

def perform_mul(num1, num2):
    print('Multiplying numbers..')
    return num1 * num2

def perform_div(num1, num2):
    # validate
    # if num2 is zero, print error and return 0
    if(num2 == 0):
        print('Error. Cannot divide by 0')
        return 0
    else:
        return num1/num2

def print_menu():
    print("     Menu       ")
    print("1 - Sum ")
    print("2 - Sub ")
    print("3 - Mul ")
    print("4 - Div")
    print("x - Exit")




print('*' * 20)
print(" Welcome to my Calc")
print('*' * 20)

num1 = input("Please provide num1: ")
num2 = input("Please provide num2: ")

f_num1 = float(num1)
f_num2 = float(num2)

#say_hello() # call a function
#res = perform_sum(f_num1, f_num2)
#print("Sum result " + str(res) )
#
## call _div here
#div_res = perform_div(f_num1, f_num2)
#print("Div result " + str(div_res))
#
#print('*' * 25)
#
#for i in range(3, 10): # for i = 3; i < 10; i++
#    print(i)
#
#fruits = ["apple", "orange", "banana", "chery"] # array
#
#print(fruits)
#print(fruits[0])
#
#print('with a for loop')

#for fruit in fruits:
 #   print

# while loop
opc = ''
while(opc != "x"):
    print_menu()
    opc = input("Select an option: ")

    if(opc == '1'):
        res = perform_sum(f_num1, f_num2)
        print('Result: ' + str(res))
    
    elif(opc == '2'):
        res = perform_sub(f_num1, f_num2)
        print('Result: ' + str(res))
    
    elif(opc == '3'):
        res = perform_mul(f_num1, f_num2)
        print('Result: ' + str(res))
    
    elif(opc == '4'):
        res = perform_div(f_num1, f_num2)
        print("Result: " + str(res))

print("")
print("Thank you and byte byte!")