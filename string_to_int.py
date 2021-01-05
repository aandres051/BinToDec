from math import pow
def changes_to_int(numbers):
    for i in numbers:
        print(pow(2, i))


if __name__ == "__main__":

    numbers = list(input('Write a number: '))
    changes_to_int(numbers)