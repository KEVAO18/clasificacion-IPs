# Nombre del Proyecto

Este proyecto es una aplicación de Python que permite a los usuarios ingresar direcciones IP y obtener información detallada sobre ellas.

## Requisitos

- Python 3.10
- Pytesseract
- Tesseract OCR
- Tkinter
- Tabulate

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias con el siguiente comando:

```bash
pip install pytesseract tkinter tabulate
```

3. Descarga e instala Tesseract OCR desde el [repositorio oficial de GitHub](https://github.com/UB-Mannheim/tesseract/wiki).
4. Asegúrate de que la ubicación del ejecutable de Tesseract (normalmente `C:\Program Files\Tesseract-OCR`) esté en tu variable de entorno PATH.

## Uso

Ejecuta el archivo `main.py` para iniciar la aplicación. Se te presentará un menú con varias opciones:

- Ejecutar instrucción individual: te permite ingresar una dirección IP y obtener información detallada sobre ella.
- Ejecutar instrucción por lotes: te permite seleccionar un archivo con una lista de direcciones IP y obtener información detallada sobre todas ellas.
- Ejecutar instrucción individual sin tabla: te permite ingresar una dirección IP y obtener información detallada sobre ella sin guardar la información en una tabla.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir lo que te gustaría cambiar.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)