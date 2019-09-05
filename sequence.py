#1. Let the user input a number which determines the length of the sequence
#2. Assign 1,2,3 as the first 3 numbers of the sequence
#3. Add the first 3 numbers together to get your fourth number
#4. Continue adding together the latest 3 numbers of the sequence to get the next number
#5. Continue adding new numbers to the sequence until the length is reached
n = int(input("Enter the length of the sequence: ")) # Do not change this line

num1 = 1
num2 = 2
num3 = 3
print(num1)
print(num2)
print(num3)
for i in range(1, n+1):
    num4 = num1 + num2 + num3
    print(num4)
    num1 = num2
    num2 = num3
    num3 = num4


