# ModSim2020

## Modelos y Simulacion (2020) del FaMAF - UNC (FaMAFyC)

### Autor

* __@00santiagob__

## Resumen

En este repositorio se haran los codigos que sean relevantes para la materia Modelos y Simulacion (2020). Dichos codigos perteneceran a los teorico y a los practicos.

* Las unidades anteriores no requerian codigo.
* **unidad3.py** (*Aun no se hizo* - Temario 3)
* **unidad4.py** (*Aun no se hizo* - Temario 4)
* **unidad5.py** (*Aun no se hizo* - Temario 5)
* **unidad6.py** (*Aun no se hizo* - Temario 6)
* **unidad7.py** (*Aun no se hizo* - Temario 7)
* **unidad8.py** (*Aun no se hizo* - Temario 8)
* **unidad9.py** (*Aun no se hizo* - Temario 9)

Para este repositorio se uso *autopep8* para el estilo de codigo, lo cual hizo que no se pueda usar funciones lambda.
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

2) Para correr algun ejercicio entrar en algun archivo **archivo.py**.

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
Posiblemente en linux aparezcan errores al instalar la libreria *Matplotlib*, dado que depende de otras librerias: *libfreetype6*, *libpng12* y *libqhull*. Tambien puede que aparezcan con otros nombres similares, pero son las mismas librerias.
>
> **Soluciones:**
>
> * Error al instalar Matplotlib:
>
>       sudo apt install libfreetype6-dev
>       sudo apt install pkg-config
>       sudo apt install libpng12-dev
>       sudo apt install pkg-config
>       sudo apt install libqhull
>       sudo apt update && sudo apt upgrade
>       pip3 install matplotlib

**Cualquier otro error se agradece que lo comenten abriendo una issue nueva.**

Gracias y disfruten
