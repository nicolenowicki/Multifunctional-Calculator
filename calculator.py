from easygui import *

#FUNCTIONS:
def store(calc, counter, file):
    '''store(str)
    Store the current score in self.__file, and then return text stating whether self.__score is greater than any score stored in self.__file'''
    lines = []
    in_file = open(file)
    
    for line in in_file:
        lines.append(line.strip("\n"))
        
    calc = "{}) {}".format(counter, calc)    
    lines.append(calc)
    
    in_file.close()  
    
    out_file = open(file, "w")
    out = ""

    for n in lines:
        out_file.write("{}\n".format(n))
        out += "{}\n".format(n)
    out_file.close() 
    
    return out

def clear(file):
    '''clear()
    Clear the contents of this file.'''
    out_file = open(file, "w")
    out_file.close()

file = "userdata.txt"
answers = ""
out = ""
counter = 0

user = "Yes"
while user == "Yes":
    choice = buttonbox("MAIN MENU:", "CALCULATOR", ["Powers", "Quadratics", "Percents", "Basic Ops", "MEM"])
    
    #POWERS
    if choice == 'Powers':
        values = multenterbox("Enter respective values: ", "POWERS", ["Base: ", "Exponent: "])
        
        base = int(values[0])
        exponent = int(values[1])
        power = (base)**(exponent)
        
        if base >= 0 and exponent >= 0:
            out = "{}^{} = {}".format(base, exponent, power)
        elif base < 0 and exponent < 0:
            out = "({})^({}) = {}".format(base, exponent, power)        
        elif base < 0:
            out = "({})^{} = {}".format(base, exponent, power) 
        elif exponent < 0:
            out = "{}^({}) = {}".format(base, exponent, power)
            
        msgbox(out, "ANSWER:") 
        counter += 1
        answers = store(out, counter, file)
     
    #QUADRATICS
    elif choice == 'Quadratics':
        values = multenterbox("Enter the integer values for the quadratic equation ax^2 + bx + c = 0: ", "QUADRATICS", ["a: ", "b: ", "c: "])
        
        a = int(values[0])
        b = int(values[1])
        c = int(values[2])
        
        discriminant = b**2 - 4 * a * c
        rootofd = (discriminant)**0.5
        
        root_1 = ((b * -1) + rootofd) / (2 * a)
        root_2 = ((b * -1) - rootofd) / (2 * a)
        
        out = ""
        p = ""
        
        if discriminant < 0:
            discriminant *= -1
            rootofd = (discriminant)**0.5
            p = "i"
            #out = "Non-real root."
            
           
        if rootofd == 0:
            out += "{:^3} i \n".format(b * -1)
            out += "---   ({:.3f})\n".format(root_1)
            out += "{:^3}".format(2 * a)
        
        else:
            remainder = rootofd % 1
            if remainder == 0:
                out += "{:^4} {}       {:^4} {}\n".format(b * -1 + int(rootofd), p, b * -1 - int(rootofd), p)
                out += "------  or  ------  ({:.3f} or {:.3f})\n".format(root_1, root_2)
                out += "{:^4}        {:^4}".format(2 * a, 2 * a)
            else:
                out += "{:>17}{:>26}\n".format('_____', '_____')
                out += "{:<3} + \/{:>7}   {}          {:<2} - \/{:>8}   {}\n".format(b * -1, discriminant, p, b * -1, discriminant, p)
                out += "--------------------  or  --------------------  ({:.3f} or {:.3f})\n".format(root_1, root_2)
                out += "{:^20}{:>26}".format(2 * a, 2 * a)
        
        #FIX LINING UP        
        msgbox(out, "ANSWER:")
        counter += 1
        answers = store(out, counter, file)
    
    #PERCENTS
    elif choice == 'Percents':
        values = multenterbox("Enter a number and then a percent: ", "QUADRATICS", ["Number: ", "Percent: "])
        
        num = float(values[0])
        percent = float(values[1])
        
        if percent >= 0:
            answer_1 = (percent / 100) * num
            out = "{:.2f}% of {:.2f} = {:.2f}".format(percent, num, answer_1)
            
        else:
            out = "Percent cannot be negative."
            
        msgbox(out, "ANSWER:")
        counter += 1
        answers = store(out, counter, file)
    
    #change with easygui    
    #BASICOPS
    elif choice == 'Basic Ops':
        out = ""
        num_1 = float(enterbox("Enter your first number: ", "BASIC OPERATIONS"))
        operation_1 = enterbox("Enter a operation (+, -, /, or *): ", "BASIC OPERATIONS")
        num_2 = enterbox("Enter your second number: ", "BASIC OPERATIONS")
        
        if num_2 == '(':
            num_3 = float(enterbox("Enter your sub-number: ", "BASIC OPERATIONS"))
            operation_2 = enterbox("Enter a sub-operator: ", "BASIC OPERATIONS")
            num_4 = float(enterbox("Enter a sub-number: ", "BASIC OPERATIONS"))
                    
            if operation_2 == '+':
                num_2 = num_3 + num_4
            elif operation_2 == '-':
                num_2 = num_3 - num_4
            elif operation_2 == '*':
                num_2 = num_3 * num_4
            else:
                num_2 = num_3 / num_4    
        
        else:
            num_2 = float(num_2)
            
        if num_1 == int(num_1):
            num_1 = int(num_1)
        if num_2 == int(num_2):
            num_2 = int(num_2)
            
        if operation_1 == '+':
            answer = num_1 + num_2
            if answer == int(answer):
                answer = int(answer)        
        elif operation_1 == '-':      
            answer = num_1 - num_2 
            if answer == int(answer):
                answer = int(answer)        
        elif operation_1 == '*':
            answer = num_1 * num_2
            if answer == int(answer):
                answer = int(answer)        
        elif operation_1 == '/':
            answer = num_1 / num_2
            if answer == int(answer):
                answer = int(answer) 
                
        if operation_1 == '+' or operation_1 == '-':        
                if num_2 < 0:
                    out = (" {} {} ({}) = {}".format(num_1, operation_1, num_2, answer))
                else:
                    out = (" {} {} {} = {}".format(num_1, operation_1, num_2, answer))
        
        else:        
                out = (" {} {} {} = {}".format(num_1, operation_1, num_2, answer))
                
        msgbox(out, "ANSWER:")
        counter += 1
        answers = store(out, counter, file)
        
    elif choice == "MEM":
        textbox("Past Calculations:", "MEMORY", answers)
        
    else:
        out = ("Invalid selection.", "ANSWER:")
        msgbox(out)
        answers = store(out, counter, file)
        
    user = buttonbox("Do you want to make another calculation?", "CALCULATOR", ["Yes", "No"])
    
clear(file)  
textbox("Your Calculations:", "MEMORY", answers)
