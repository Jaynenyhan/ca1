# Test 1
def callme01(x):
    y = None
    try:
        y = 1/x
    except ZeroDivisionError:
        print('In exception handler')
    else:
        print('Reached end of try')
    finally:
        print('Exiting the function')
    return y

print("callme01(1)", callme01(1)) # Reached end of try, Exiting the function, 1.0
print("callme01(0)", callme01(0)) # In exception handler, Exiting the function, None
print("\n")

# Test 2
def callme02(x):
    try:
        y = 1/x
    except ZeroDivisionError:
        print('In exception handler')
    else:
        print('Reached end of try')
    finally:
        print('Exiting the function')
    return y

print("callme02(1)", callme02(1)) # Reached end of try, Exiting the function, 1.0
print("callme02(0)", callme02(0)) # In exception handler, Exiting the function, y not assigned -> error
print("\n")

# Test 3
def callme03(x):
    try:
        y = 1/x
        return y
    except ZeroDivisionError:
        print('In exception handler')
    else:
        print('Reached end of try')
    finally:
        print('Exiting the function')

print("callme03(1)", callme03(1)) # Exiting the function, 1.0
print("callme03(0)", callme03(0)) # In exception handler, Exiting the function, None
print("\n")

# Test 4
def callme04(x):
    try:
        y = 1/x
    except ValueError:
        print('In exception handler')
    else:
        print('Reached end of try')
    finally:
        print('Exiting the function')
    return y

print("callme04(1)", callme04(1)) # Reached end of try, Exiting the function, 1.0
print("callme04(0)", callme04(0)) # Exiting the function, ZeroDivisionError
print("\n")
