class Rectangle:
    """
    Класс для представления прямоугольника.

    Attributes:
    width (float): Ширина прямоугольника.
    height (float): Высота прямоугольника.
    """

    def __init__(self, width: float, height: float):
        """
        Инициализация нового экземпляра Rectangle.

        Args:
        width (float): Ширина прямоугольника.
        height (float): Высота прямоугольника.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Вычисляет площадь прямоугольника.

        Returns:
        float: Площадь прямоугольника.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Вычисляет периметр прямоугольника.

        Returns:
        float: Периметр прямоугольника.
        """
        return 2 * (self.width + self.height)


class Circle:
    """
    Класс для представления круга.

    Attributes:
    radius (float): Радиус круга.
    """

    def __init__(self, radius: float):
        """
        Инициализация нового экземпляра Circle.

        Args:
        radius (float): Радиус круга.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Вычисляет площадь круга.

        Returns:
        float: Площадь круга.
        """
        import math
        return math.pi * (self.radius ** 2)

    def circumference(self) -> float:
        """
        Вычисляет длину окружности круга.

        Returns:
        float: Длина окружности круга.
        """
        import math
        return 2 * math.pi * self.radius


class Triangle:
    """
    Класс для представления треугольника.

    Attributes:
    side_a (float): Длина стороны a.
    side_b (float): Длина стороны b.
    side_c (float): Длина стороны c.
    """

    def __init__(self, side_a: float, side_b: float, side_c: float):
        """
        Инициализация нового экземпляра Triangle.

        Args:
        side_a (float): Длина стороны a.
        side_b (float): Длина стороны b.
        side_c (float): Длина стороны c.
        """
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self) -> float:
        """
        Вычисляет площадь треугольника по формуле Герона.

        Returns:
        float: Площадь треугольника.
        """
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    def perimeter(self) -> float:
        """
        Вычисляет периметр треугольника.

        Returns:
        float: Периметр треугольника.
        """
        return self.side_a + self.side_b + self.side_c


if __name__ == "__main__":
    import doctest

    # Примеры тестов для Rectangle
    r = Rectangle(4, 3)
    print(r.area())         # 12
    print(r.perimeter())    # 14

    # Примеры тестов для Circle
    c = Circle(5)
    print(c.area())         # Узнать площадь круга
    print(c.circumference()) # Узнать длину окружности

    # Примеры тестов для Triangle
    t = Triangle(3, 4, 5)
    print(t.area())        # 6.0
    print(t.perimeter())   # 12

    # Запуск doctest
    doctest.testmod()
