def suma(a, b):
    return a + b

def substr(a, b):
    return a - b


def power(a, b):
    return a ** b

def mult(a, b):
    return a * b

def calc (operand_A, operand_B, operation):
    if operation not in ['+', '-', '*', '^']:
        print('bilinmeyen işlem')
    else:
        # Python 3.10 (2021) introduced the match-case statement
        # which provides a first-class implementation of a "switch" for Python
        '''   
        match operation:
            case '+':
                result = suma(operand_A, operand_B)
            case '-':
                result = substr(operand_A, operand_B)
            case '*':
                result = mult(operand_A, operand_B)
            case '^':
                result = power(operand_A, operand_B)
        '''
        if(operation == '+'):
            result = suma(operand_A, operand_B)
        elif(operation == '-'):  
            result = substr(operand_A, operand_B)
        elif(operation == '*'):
            result = mult(operand_A, operand_B)
        else:
            result = power(operand_A, operand_B)
        
        print(operand_A, operation, operand_B, '=', result)
    
a, operator, b = input().split()
calc(int(a), int(b), operator)