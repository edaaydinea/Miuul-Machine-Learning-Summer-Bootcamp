def factorial(number):
    a = 1
    for i in range(1, number + 1):
        a = a * i

    return a


if __name__ == '__main__':
    num = int(input("Enter the number: "))
    print(factorial(num))
