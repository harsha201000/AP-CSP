#   a114_divisible.py

# get two numbers from user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

# loop while the numbers are not divisible (the remainder is not 0)
while num2 == 0 or num1 % num2 != 0:
  if num2 == 0:
  # inform user of result
    print("Zero Division Error")
  else:
    print("{} is not divisible by {}".format(num1,num2))
  
  # gather user input again
  num1 = int(input("Enter number 1: "))
  num2 = int(input("Enter number 2: "))
  
# inform user of result 
print("{} is divisible by {}".format(num1,num2))