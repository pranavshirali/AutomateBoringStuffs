#Author: Pranav Shirali
#Description: Python program to check a given number is palindrome and to count the number of occurence of each digit.
#changes
#Input the number
number = int(input("Enter the number to be evaluted: "))

#Check for palindrome:
reverse_number = 0
check_number = number
while check_number != 0:
    remainder = check_number % 10
    reverse_number = (reverse_number * 10) + remainder
    check_number //= 10

if number == reverse_number:
    print(f"Number {number} is a palindrome.")
else:
    print(f"Number {number} is not a palindrome.")

#To count the number of occurence of each digit:
digit_count = [0] * 10
while number != 0:
    remainder2 = number % 10
    digit_count[remainder2] += 1
    number //= 10

for digit in range(10):
    print(f"{digit} | {digit_count[digit]}")