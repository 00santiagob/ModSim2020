# ModSim2020

## Modelos y Simulacion (2020) del FaMAF - UNC (FaMAFyC)

### Autor

* __@00santiagob__

## Resumen

En este repositorio se haran los codigos que sean relevantes para la materia Modelos y Simulacion (2020). Dichos codigos perteneceran a los teorico, practicos y examens.

En la carpeta *codigos/*:

* **unidad3.py** (*Completo* - Temario 3)
* **unidad4.py** (*Completo* - Temario 4)
* **unidad5.py** (*Completo* - Temario 5)
* **unidad6.py** (*Completo* - Temario 6)
* **unidad7.py** (*Completo* - Temario 7)
* **unidad8.py** (*Completo* - Temario 8)
* **examen.py** (*Completo* - Examen)
* **examen2.py** (*Completo, pero sin corregir* - Examen)

> Las unidades 1 y 2 no requerian codigo, y la unidad 9 no se dicto en la cursada.

En la carpeta *codigos/Parcial/*:

* **ej1.py**
* **ej2.py**
* **ej3.py**

En la carpeta *codigos/TrabajoPractico/*

* **TrabajoPractico.py** (*Incompleto* - Contempla los ejercicios 1 y 2)

En la carpeta codigos/practico3/

* Solo hay algunos codigos.

> **Nota:** Se agradece a los compañeros que compartieron los codigos de los practicos, pero por motivos de privacidad no los puedo divulgar.

Ademas se han usado librerias como ***Numpy***, ***Scipy***, ***Matplotlib*** y ***Math*** para la realizacion de algunos ejercicios.

### Temario

1. Conceptos basicos de probabilidad
2. Procesos de Poisson
3. Numeros aleatorios
4. El metodo de Monte Carlo
5. Generacion de variables aleatorias discretas
6. Generacion de variables aleatorias continuas
7. Analisis estadistico de datos simulados
8. Tecnicas de validacion estadistica
9. Cadenas de Markov

## Requisitos

Tener instalado *__Git__* y  *__Python__* (en lo posible Python3 cualquier version).
Ademas se recomienda tener instaladas las librerias anteriormente instaladas (Si no sabe hacerlo, mas abajo se lo explicamos).

## Instrucciones

Primero descargar el repositorio __ModSim2020__:

1) Abrir una terminal:

    git clone https://github.com/00santiagob/ModSim2020.git

   2) Para correr algun ejercicio entrar en algun archivo **unidadX.py**.
   3) En la parte inferior comentar y/o descomentar alguna funcion para usarla.
### Como Instalar

Hara falta tener instalado Git en su dispositivo, pero no es parte de este repositorio enseñarles a hacerlo, asi que queda en sus manos hacerlo.

#### Python en Windows

Descargar [Python 3.x.x](https://www.python.org/downloads/) de la pagina oficial.

#### Python en Ubuntu

Abrir la terminal y correr el siguiente comando:

    sudo apt install python3 python3-dev python3-pip
    pip3 install --upgrade pip
    sudo apt update && sudo apt upgrade
#### Python en ALGUN-OTRO-OS

Queda pendiente. Si sos usuario de algun sistema operativo distinto a los anteriormente mencionados, te pido que ayudes a completar este instructivo.

#### Evitar errores

Chequear que esten instaladas las librerias *Numpy*, *Matplotlib* y *SciPy*, en caso de no estarlo correr lo siguiente en la terminal (powershell en caso de usar Windows):

    pip3 install numpy
    pip3 install matplotlib
    pip3 install scipy
> **Nota:** en caso de ya tenerlos instalados es suficientes (no importa la version).
>
> **Errores:**
> Posiblemente en linux aparezcan errores al instalar la libreria *Matplotlib*, dado que depende de otras librerias: *libfreetype6*, *libpng12* y *libqhull*. Tambien puede que aparezcan con otros nombres similares, pero son las mismas librerias.
>
> **Soluciones:**
>
> * Error al instalar Matplotlib:
>
>   sudo apt install libfreetype6-dev
>   sudo apt install pkg-config
>   sudo apt install libpng12-dev
>   sudo apt install pkg-config
>   sudo apt install libqhull
>   sudo apt update && sudo apt upgrade
>   pip3 install matplotlib
>
> **Cualquier otro error se agradece que lo comenten abriendo una issue nueva.**
>
> Gracias y disfruten
>
