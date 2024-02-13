for num in range(31):
    if num % 15 ==  0:
        print("Fizz")
    elif num % 3 == 0:
        print("Buzz")
    elif num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)
        