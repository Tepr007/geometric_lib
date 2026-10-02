# Документация к geometric_lib
Это решение для рассчетов параметров геометрических фигур.

## circle.py
В этом файле находятся функции для рассчёта параметров круга.

### area():
* **Принимает:** 
    * _r_ (int | float) - радиус окружности;

* **Возвращает:** (float) Площадь круга с радиусом _r_.

* **Пример вызова:**
    
    ```
    area(5) -> 78.53981633974483
    area(1.3) -> 5.3092915845667505
    ```

### perimeter():
* **Принимает:** 
    * _r_ (int | float) - радиус окружности;

* **Возвращает:** (float) Периметр окружности с радиусом _r_.

* **Пример вызова:**
    ```
    perimeter(5) -> 31.41592653589793
    perimeter(1.3) -> 8.168140899333462
    ```



## square.py
В этом файле находятся функции для рассчёта параметров квадрата.

### area():
* **Принимает:** 
    * _a_ (int | float) - сторона квадрата;

* **Возвращает:** (int | float) Площадь квадрата со стороной _a_.

* **Пример вызова:**
    
    ```
    area(5) -> 25
    area(1.3) -> 1.6900000000000002
    ```

### perimeter():
* **Принимает:** 
    * _a_ (int | float) - сторона квадрата;

* **Возвращает:** (int | float) Периметр квадрата со стороной _a_.

* **Пример вызова:**
    ```
    perimeter(5) -> 20
    perimeter(1.3) -> 5.2
    ```



## rectangle.py
В этом файле находятся функции для рассчёта параметров прямоугольника.

### area():
* **Принимает:** 
    * _a_ (int | float) - ширина прямоугольника, 

    * _b_ (int | float) - высота прямоугольника;

* **Возвращает:** (int | float) Площадь прямоугольника со сторонами _a_ и _b_.

* **Пример вызова:**
    
    ```
    area(5, 3) -> 15
    area(1.3, 2.5) -> 3,25
    ```

### perimeter():
* **Принимает:** 
    * _a_ (int | float) - ширина прямоугольника, _b_ (int | float) - высота прямоугольника;

* **Возвращает:** (int | float) Периметр прямоугольника со сторонами _a_ и _b_.

* **Пример вызова:**
    ```
    perimeter(5, 3) -> 16
    perimeter(1.3, 2.5) -> 7.6
    ```



## triengle.py
В этом файле находятся функции для рассчёта параметров треугольника.

### area():
* **Принимает:** 
    * _a_ (int | float) - основание треугольника, 
    * _h_ (int | float) - высота треугольника;

* **Возвращает:** (int | float) Площадь триугольника с основанием _a_ и высотой _h_.

* **Пример вызова:**
    
    ```
    area(5, 3) -> 7.5
    area(1.3, 2.5) -> 1.625
    ```
    


### perimeter():
* **Принимает:** _a_, _b_, _c_ (int | float) - стороны триугольника;

* **Возвращает:** (int | float) Периметр триугольника со сторонами _a_, _b_, _c_.

* **Пример вызова:**
    ```
    perimeter(5, 3, 2) -> 10
    perimeter(1.3, 2.5, 3.1) -> 6.9
    ```



## История изменения geometric_lib

<font color="yellow">5374fde (<font color="29b8db">**HEAD**</font> -> <font color="23d18b">**main**</font>)</font> add function declarations for rectangle.py and triangle.py

<font color="yellow">8492044</font> Fix rectangle.py

<font color="yellow">d58927c</font> Add triangle.py

<font color="yellow">92c9a44</font> Add rectangle.py

<font color="yellow">043a134 (<font color="f14c4c">**origin/main**</font>, <font color="f14c4c">**origin/deadline_0**</font>, <font color="23d18b">**deadline_0**</font>)</font> Add report

<font color="yellow">568a7b2</font> Create Docwmentation.md

<font color="yellow">a6a13ff</font> add function declarations

<font color="yellow">86edb1c (<font color="f14c4c">**upstream/release**</font>)</font> L-05: Update Docs. Add user agreement info

<font color="yellow">438b89a</font> L-05: Add user agreement

<font color="yellow">6adb962</font> L-03: Docs added

<font color="yellow">3049431 (<font color="f14c4c">**upstream/feature**</font>)</font> L-04: Add rectangle.py

<font color="yellow">b5b0fae (<font color="f14c4c">**upstream/develop**</font>)</font> L-04: Update docs for calculate.py

<font color="yellow">d76db2a</font> L-04: Add calculate.py

<font color="yellow">51c40eb</font> L-04: Doc updated for triangle

<font color="yellow">d080c78</font> L-04: Triangle added

