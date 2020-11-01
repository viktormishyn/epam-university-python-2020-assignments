class Rectangle:

    def __init__(self, sideA, sideB=5):
        self.__sideA = float(sideA)
        self.__sideB = float(sideB)

    def get_sideA(self):
        return self.__sideA

    def get_sideB(self):
        return self.__sideB

    def area(self):
        area = self.__sideA * self.__sideB
        return area

    def perimeter(self):
        perimeter = (self.__sideA + self.__sideB) * 2
        return perimeter

    def is_square(self):
        return self.__sideA == self.__sideB

    def replace_sides(self):
        self.__sideA, self.__sideB = self.__sideB, self.__sideA


class ArrayRectangles:
    def __init__(self, *args, add_limit=10):
        """
        :param args: Only the objects of Rectangle class will be appended to self.__array_rectangles attribute.
        If there is only one argument and it is a list of objects, the Rectangle objects of this list will be appended
        to self.__array_rectangles.
        If there are no arguments or the arguments are not Rectangle class object, self.__array_rectangles attribute
        will be an empty list.
        :param add_limit: a limit for add_rectangle method. If self.__array_rectangles >= add_limit,
        method add_rectangle will return False. Default value is 10.
        """
        self.__add_limit = add_limit
        if len(args) == 1 and isinstance(args, list):
            self.__array_rectangles = [element for element in args[0] if isinstance(element, Rectangle)]
        self.__array_rectangles = [element for element in args if isinstance(element, Rectangle)]

    @property
    def array_rectangles(self):
        return self.__array_rectangles

    def add_rectangle(self, rectangle):
        """
        :param rectangle: instance of Rectangle class
        :return: If the add_limit is not exceeded and the Rectangle class object is passed as an attribute, the method
        returns True and adds the object to the self.__array_rectangles class attribute.
        """
        if len(self.__array_rectangles) < self.__add_limit and isinstance(rectangle, Rectangle):
            self.__array_rectangles.append(rectangle)
            return True
        return False

    def number_max_area(self):
        """
        :return: index of the Rectangle object with the maximum area in self.__array_rectangles list.
        """
        max_area = 0
        index = 0
        for i, rectangle in enumerate(self.__array_rectangles):
            if rectangle.area() > max_area:
                max_area = rectangle.area()
                index = i
        return index

    def number_min_perimeter(self):
        min_perimeter = None
        index = 0
        for i, rectangle in enumerate(self.__array_rectangles):
            if min_perimeter is None:
                min_perimeter = rectangle.perimeter()
                index = i
            elif rectangle.perimeter() < min_perimeter:
                min_perimeter = rectangle.perimeter()
                index = i
        return index

    def number_square(self):
        """
        :return: number of squares in the self.__array_rectangles list of Rectangle objects
        """
        return len([i for i in self.__array_rectangles if i.is_square()])


if __name__ == '__main__':
    print('\nCreate instance of the Rectangle class: square = Rectangle(40, 40)')
    square = Rectangle(40, 40)
    print('get_sideA method: ', square.get_sideA())
    print('get_sideB method: ', square.get_sideB())
    print('area method: ', square.area())
    print('perimeter method: ', square.perimeter())
    print('is_square method:', square.is_square(), '\n')

    print('Create instance of the Rectangle class: square = Rectangle(40)')
    rectangle1 = Rectangle(40)
    print('get_sideA method: ', rectangle1.get_sideA())
    print('get_sideB method: ', rectangle1.get_sideB(), '(default value)')
    print('area method: ', rectangle1.area())
    print('perimeter method: ', rectangle1.perimeter())
    print('is_square method:', rectangle1.is_square())
    print('applying replace_sides method')
    rectangle1.replace_sides()
    print(f'New sides are: {rectangle1.get_sideA()}, {rectangle1.get_sideB()}\n')

    print('\n=================Advanced Level=====================\n')

    print(f'Create instance of the ArrayRectangles class, '
          f'later we can add objects if the array length is less than 4 (add_limit value, by default 10): \n'
          f'array_rectangles = ArrayRectangles(square, rectangle, add_limit=4)')
    array_rectangles = ArrayRectangles(square, rectangle1, add_limit=4)
    print(f'Create more instances of the Rectangle class: \n'
          f'rectangle2 = Rectangle(3, 8); rectangle3 = Rectangle(70, 160); excess_rectangle = Rectangle(5, 2);')
    rectangle2 = Rectangle(3, 8)
    rectangle3 = Rectangle(70, 160)
    excess_rectangle = Rectangle(5, 2)

    print(f'\nAdd rectangle2 to the ArrayRectangles: array_rectangles.add_rectangle(rectangle2)')
    print(array_rectangles.add_rectangle(rectangle2))
    print(f'Add rectangle3 to the ArrayRectangles: array_rectangles.add_rectangle(rectangle3)')
    print(array_rectangles.add_rectangle(rectangle3))
    print(f'Trying to add excess_rectangle to the ArrayRectangles: array_rectangles.add_rectangle(excess_rectangle)')
    print(array_rectangles.add_rectangle(excess_rectangle))

    print(f'\nThe index of the Rectangle object with the maximum area is {array_rectangles.number_max_area()}')
    print(f'The index of the Rectangle object with the mininmum perimeter is {array_rectangles.number_min_perimeter()}')
    print(f'Squares in the array: {array_rectangles.number_square()}')
