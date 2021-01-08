def bin_to_dec(binary_number):
    """
    This changes the binary number to decimal number
    """
    binary_number = str(binary_number)
    exponent = 0
    result = 0

    while exponent < len(binary_number):
        if int(binary_number[exponent]) != 1 and int(binary_number[exponent]) != 0:
            raise ValueError('The bytes only has number 1 and 0')

        elif type(binary_number) not in [str]:
            raise TypeError('TypeError. We expect a number')

        elif int(binary_number[exponent]) == 1:
            result += int(binary_number[exponent]) * 2 ** exponent
        exponent += 1
    return result


if __name__ == "__main__":
    print(''' Remember! one bytes is 8 bits.
    if you type more than eight digits, the program will show you the error \n ''' )
    binary_number = input('Write a binary number: ')
    print(f'The result is {bin_to_dec(binary_number)} ')