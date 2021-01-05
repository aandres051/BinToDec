

def longitud(X):
    if len(X) > 8:
        print('Only write 8 digits')
        X = input('') 
        confirmar_numeros(X)
    elif len(X) == 0:
        print('Write a binary number')
        X = input('') 
        confirmar_numeros(X)

def confirmar_numeros(X):
    longitud(X)
    for i in X:
        if i == '1' or i == '0':
            continue
        else: 
            print('You write a error digit. Try again')


def base_2():
    pass

if __name__ == "__main__":
    print(''' Remember! one bytes is 8 bits.
    if you type more than eight digits, the program will show you the error \n ''' )

    binary_number = input('Write a binary number: ')
    binary_number = list(binary_number)
    confirmar_numeros(binary_number)

