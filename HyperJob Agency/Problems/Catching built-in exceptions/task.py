def exception_check(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("The Error!")