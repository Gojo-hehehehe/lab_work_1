a, b, c = input().split()

def check_numb():
    try:
        float(a)
        float(b)
        float(c)
        return True
    except ValueError:
        return False

if check_numb():
    a = float(a)
    b = float(b)
    c = float(c)
    d = b**2 - 4*a*c
    if d < 0:
        print("radicals not found")
    elif d == 0:
        x = -b/2*a
        print("One radical found -", x)
    else:
        x1 = (-b + d**0.5)/2*a
        x2 = (-b - d**0.5)/2*a
        print("Two radicals found -", x1,"and", x2)
else:
    print("Please, enter the numbers")