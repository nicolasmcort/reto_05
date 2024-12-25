# reto_05

El objetivo de este reto es organizar clases de formas geométricas mediante paquetes y módulos, en dos casos: un único módulo y módulos separados para cada clase.
***

### Paquete único con todo el código de `Shape`

En este caso, todo el código relacionado con las clases `Shape`, `Point`, `Line`, y sus subclases (como `Triangle`, `Rectangle`, `Square`, etc.) está contenido en un único módulo (shape) dentro del paquete `Shape`. 

``` bash
project_rectangle1/
│
├── main.py  # Script principal con el código de prueba
└── Shape/
    ├── __init__.py  
    └── shape.py  
```
***

### Módulos individuales

En este caso, se organiza el código en módulos individuales para diferentes clases. La clase `Shape` se coloca en su módulo base.py, y las clases derivadas (`Triangle`, `Rectangle`, `Square`, etc.) están en archivos separados. 

``` bash
project_rectangle2/
│
├── main.py  # Script principal con el código de prueba
└── Shape/
    ├── __init__.py 
    ├── base.py  # Contiene la clase Shape
    ├── point.py  # Contiene la clase Point
    ├── line.py  # Contiene la clase Line
    ├── triangle.py  # Contiene las clases Triangle 
    ├── rectangle.py  # Contiene la clase Rectangle
    └── square.py  # Contiene la clase Square
```
***

### OUTPUT en ambos casos

``` bash
The type of triangle is: Equilateral
The area of the triangle is: 6.928203230275511
The area of the rectangle is: 12.0
The area of the square is: 4.0
```
