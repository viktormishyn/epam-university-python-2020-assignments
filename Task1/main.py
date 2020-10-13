def triangle_area(a, b, c):
    s = (a+b+c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area


if __name__ == "__main__":
    try:
        a = float(input('Enter first side: '))
        b = float(input('Enter second side: '))
        c = float(input('Enter third side: '))
    except ValueError:
        print("Should be a number. Try again..")
        exit()
    area = triangle_area(a, b, c)
    print(f"The area of the triangle is {area:.2f}")
