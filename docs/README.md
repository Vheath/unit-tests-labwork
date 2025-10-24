# Docs
## Solution Description
Реализованы операции для вычисления площади и периметра для следующих фигур:
- [Окружность](../circle.py)
- [Прямоугольник](../rectangle.py)
- [Квадрат](/square.py)
## Functions Description
- **area** - принимает параметры, описывающие фигуру(радиус, длины сторон), и возвращает площадь заданной фигуры.
- **perimeter** - принимает параметры, описывающие фигуру(радиус, длины сторон), и возвращает периметр заданной фигуры.
### Examples 
```py
import circle as c
import rectangle as r
import square as s
import triangle as t

r = 3
print(c.area(r)) # Выведет площадь окружности с радиусом r = 3
print(c.perimeter(r)) # Выведет периметр окружности с радиусом r = 3

a = 2
print(s.area(a)) # Выведет площадь квадрата со стороной a = 2
print(s.area(a)) # Выведет периметр квадрата со стороной a = 2

b = 3
print(r.area(a, b)) # выведет площадь прямоугольника со сторонами a = 2, b = 3
print(r.perimeter(a, b)) # выведет периметр прямоугольника со сторонами a = 2, b = 3

c = 4
h = 2.5
print(t.area(a, h)) # выведет площадь треугольника с длиной основания a, и высотой h
print(t.perimeter(a, b, c)) # выведет периметр треугольника с длиной основания a, и высотой h
```
## Commit history
```sh
9ccdd73 documentation added for examples of call
0babd5d Commit history added
608d8ce Docs added for every function
6d7609a Fixed calculations of Rectangle perimeter
0f3c956 Rectangle added
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
```                                     
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
