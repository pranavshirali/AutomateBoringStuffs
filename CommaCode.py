def Comma_code(list):
    if list == []:
        return 'Error: Empty list is being passed.'
    elif len(list) == 1:
        return str(list[0])
    else:
        empty_string = ""
        for i in range(len(list)):
            if i == (len(list)-2):
                empty_string += str(list[i]) + ' and ' + str(list[i+1])
                break
            else:
                empty_string += str(list[i]) + ', '
        return empty_string
                


spam = ["apples", "bananas", "tofu", "cats"]
print('Example for string list:',Comma_code(spam))  # Output: "apples, bananas, tofu, and cats"

empty_string = []
print('Example for empty list:',Comma_code(empty_string))  # Output: ""

numbers = [1, 2, 3, 4, 5]
print('Example for integer string:',Comma_code(numbers))  # Output: "1, 2, 3, 4 and 5"
