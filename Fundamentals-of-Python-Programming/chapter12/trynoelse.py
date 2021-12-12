# Listing 12.18
# Illustrates the different behaviour between using a try/else combination to 
# shifting the code from the else block in to the try block.
# Author: Rick Halterman
# Last modified: 

def fun1():
    try:
        print('try code')
    except:
        print('exception handling code')
    else:
        print('no exception raised code')
        x = int('a')    # Raises an exception

def fun2():
    try:
        print('try code')
        print('no exception raised code')
        x = int('a')    # Raise an exception
    except:
        print('exception handling code')

print('Calling fun2')
fun2()
print('-------------')
print('Calling fun1')
fun1()