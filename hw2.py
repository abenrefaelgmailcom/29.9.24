# try = קוד שעלול להוביל לשגיאה
# exept = קןד מטפל כדי שהתוכנית לא תקרוס

# c

x: int = 88
y: int = 0

# 2 / 0  # ZeroDivisionError: division by zero
# int('a')  # ValueError: invalid literal for int() with base 10: 'a'
while True:
    try:
        x = int(input('enter mone:'))
        y = int(input('enter mehane:'))
        print(f"{x} / {y} = {x / y:.2f}")
    except ValueError as e:
        print('this is not a valid number')
        print(e)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception:
        print('catch all')
        break


# d
try:
    raise ValueError("This is a custom error message.")
except ValueError as e:
    print(f"Caught an error: {e}")


# e

numbers = [10, 20, 30, 40]

while True:
    try:
        index = int(input("Enter an index (0-3) or -999 to exit: "))
        if index == -999:
            break
        print(f"The value at index {index} is {numbers[index]}")
    except ValueError:
        print("Error: Please enter a valid integer.")
    except IndexError:
        print("Error: Index out of range.")
