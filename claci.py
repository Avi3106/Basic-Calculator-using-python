class Calculator:
    def __init__(self):
        return print("here is your advance calci!!")
    def add(self,a,b):
        return print(a+b)
    
    def sub(self,a,b):
        return print(a-b)
    def mul(self,a,b):
        return print(a*b)
    def div(self,a,b):
        if b!=0:
            return print(a/b)
        else:
            print("divisor can't be 0")
            
            
            
            
            
Calci=Calculator()

a=int(input("enter a number: "))
b=int(input('enter a number: '))

while True:
    print('enter your choice: ')
    print('1.add')
    print('2.subtract')
    print('3.multiply')
    print('4.division')
    print('5.exit')
    
    user_choice= int(input('enter your choice: '))
    
    match user_choice:
        case 1: 
            Calci.add(a,b)
        case 2:             
            Calci.sub(a,b)
        case 3:
            Calci.mul(a,b)
        case 4:
            Calci.div(a,b)
        case 5:
            print("thank you")
            exit()
        case _:
            print("choose correct option!!")