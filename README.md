# Geometric Lib
## Solution Description
Реализованы операции для вычисления площади и периметра для следующих фигур:
- [Окружность](../circle.py)
- [Прямоугольник](../rectangle.py)
- [Квадрат](/square.py)

Для отрицательных входных данных, функции считают значение по модулю.
## Testing 
Библиотека включает в себя набор unit-тестов, проверяющих корректность работы всех функций написанных модулей (всего 51 тест):
Команда для запуска всех тестов:
```zsh
python -m unittest discover ./tests/ -p '*_test.py'  
```

Команды для запуска тестов отдельно:
```zsh
python -m unittest ./tests/circle_test.py 
python -m unittest ./tests/rectangle_test.py
python -m unittest ./tests/square_test.py
python -m unittest ./tests/triangle_test.py
```
## Functions Description
### Cicle
#### circle.area\(r\)
- Принимает число r - радиус окружности
- Возвращает площадь окружности с радиусом r
Пример:
```python
import circle as c
print(c.area(5)) # 78.53981633974483
```
#### circle.perimeter\(r\)
- Принимает число r - радиус окружности
- Возвращает длину окружности с радиусом r
Пример:
```python
import circle as c
print(c.perimeter(5)) # 31.41592653589793 
```
### Rectangle
#### rectangle.area\(a, b\)
- Принимает число a, b - длины высоты и ширины прямоугольника
- Возвращает площадь прямоугольника с высотой прямоугольника - a, с шириной - b.
Пример:
```python
import rectangle as r
print(r.area(5, 4)) # 20
```
#### rectangle.perimeter\(a, b\)
- Принимает число a, b - длины высоты и ширины прямоугольника
- Возвращает периметр прямоугольника с высотой прямоугольника - a, с шириной - b.
Пример:
```python
import rectangle as r
print(r.permiter(5, 4)) # 18 
```
### Square
#### square.area\(a\)
- Принимает число a - длина стороны квадрата
- Возвращает площадь квадрата со стороной a.
Пример:
```python
import square as s
print(s.area(4)) # 16
```
#### square.perimeter\(a\)
- Принимает число a - длина стороны квадрата
- Возвращает периметр квадрата со стороной a.
Пример:
```python
import square as s
print(s.permiter(5)) # 20 
```
### Triangle
#### triangle.area\(a, h\)
- Принимает h - длина высоты треугольника, a - длина основания, в которую направлена высота h
- Возвращает площадь треугольника с длиной высоты h, и длиной основания a
Пример:
```python
import triangle as t
print(t.area(2.5, 3)) # 3.75
```
#### triangle.perimeter\(a, b, c\)
- Принимает a, b, c - длины трех сторон треугольника
- Возвращает периметр треугольника с длинами сторон a, b, c
Пример:
```python
import triangle as t
print(perimeter(2, 3, 4)) # 9
```
## Examples 
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
f58a41d Delete tests/__pycache__ directory
6d4778a Delete __pycache__ directory
a095259 Merge pull request #1 from Vheath/new_features                                                                                                        
0036f3c negative values handling added
47c3f02 docs improved        
321d005 tests added 
234d5c6 documentation improved
fa74e64 Documentation for functions added
243d37c Commit history updated
14b3fe4 Triangle
4405f96 Commit history updated
9ccdd73 documentation added for examples of call
0babd5d Commit history added
608d8ce Docs added for every function
6d7609a Fixed calculations of Rectangle perimeter
0f3c956 Rectangle
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
