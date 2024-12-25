# reto_05

El objetivo de este reto es organizar clases de formas geométricas mediante paquetes y módulos, en dos casos: un único módulo y módulos separados para cada clase.
***

### Paquete único con todo el código de `Shape`

En este caso, todo el código relacionado con las clases `Shape`, `Point`, `Line`, y sus subclases (como `Triangle`, `Rectangle`, `Square`, etc) está contenido en un único módulo dentro del paquete `Shape`. 

``` bash
project_rectangle1/
│
├── main.py  # Script principal que ejecuta el código de prueba
└── hola_mundo/
    ├── __init__.py  # Marca el directorio como un paquete
    └── shape.py  # Contiene todas las clases (Shape, Point, Line, etc.)

```
