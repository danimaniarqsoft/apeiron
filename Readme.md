# Reporte de cvu reporte

#### Pre requisitos

Instalar python 3.x `https://www.python.org/downloads/`

#### instalación del proyecto

1. clonar el repositorio `cvu-reporte-client.git`

`git clone https://scm.ccd.conacyt.mx/devtools/cvu-reporte-client.git`

3. Instalar las dependencias que requiere el proyecto

`python setup.py install`

4. Ejectuar el reporte

`python cvu.py`

#### Opciones del comando

```bash
Options:
  --path TEXT      ruta en la que se generarán los reportes de cvu
  --user TEXT      usuario cvu con el que se iniciará sesión
  --help           Show this message and exit.
```

Ejemplos:

```bash
python cvu.py -- path /home/conacyt --user gochihh@gmail.com
```

#### Configurar los cvu que se desean descargar

Agregar los números de cvu que se desean descargar en el `archivo data.csv`


**nota*: Los resultados de la operación aparecerán en la salida de la consola, los resultados se guardan en el archivo `result.cvs`
