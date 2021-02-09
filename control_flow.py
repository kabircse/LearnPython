import time, logging

def myFunction():
    print('My first function in Python')

def getListOfFruits():
    fruits = ["Apple", "Banana", "Grapes", "Mango"]
    #for i=0; i<=5; i++:
    #    print('Name of fruits: {}'.format(fruits[i]))

    for i in range(len(fruits)):
        print('Name of fruits {}: {}'.format(i+1,fruits[i]))

    return fruits

def whileLoop():
    i = 1;
    while i<=5:
        print('{} Number is:{}'.format(i,i))
        i+=1

def ifLoop():
    i = 2
    if i%2 == 0:
        print('{} is odd number'.format(i))
    else:
        print('{} is even number'.format(i))

def tryCatch():
    try:
        x = int(input('Enter a valid number: '))
    except ValueError:
        print('Invalid number.')

def getTime():
    current_time = time.time()
    print('Current time is:{}'.format(current_time))

    localTime = time.asctime(time.localtime(current_time))
    print(localTime)

def main():
    myFunction()
    getListOfFruits()
    whileLoop()
    ifLoop()
    tryCatch()
    getTime()

if __name__ == '__main__':
    main()