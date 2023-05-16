import time, sys
indent = 0      #How many steps has to increased
indent_increase = True
#Author: Pranav Shirali
print(id(indent))
#140704580952840
#140704580952840
#140704580952840
try:
    while True:
        print(' ' * indent, end='')
        print('*******')
        time.sleep(0.1)

        if indent_increase:
            #Increase the indent
            indent += 1
            #Change the direction if indent in equal to 5
            if indent == 3:
                indent_increase = False
        
        else:
            #Decrease the indent
            indent -= 1
            #Change the direction if indent is equal to 0
            if indent == 0:
                indent_increase = True

#Exit the program if user presses ctrl+c 
except KeyboardInterrupt:
    sys.exit()