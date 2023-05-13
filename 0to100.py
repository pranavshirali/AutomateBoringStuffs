import random

print('Sum of first 100 numbers:')
sum = 0
for num in range(1,6):
    sum = sum + num
print(sum)
#Example for step argument, where after each iteration last digit 'N' of range() will be skipped.
print('Example for step argument:')
for num in range(0 , 121, 12):
    print(num)

# print('Printing first 100 numbers in reverse order: ')
# for num in range(100 , 0 , -1):
#     print(num)

for i in range(5):
    print('Printing random numbers:', random.randint(1 , 10))