# Reporte de cvu reporte

1. Agregar los números de cvu dentro del archivo `data.csv`

2. Instalar las dependencias que requiere el proyecto

`python setup.py install`

3. Ejectuar el reporte

`python cvu.py`

**nota*: Los resultados de la operación aparecerán en la salida de la consola, los resultados se guardan en el archivo `result.cvs`


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