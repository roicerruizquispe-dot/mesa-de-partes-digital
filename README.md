# Mesa de partes digital

Programa en Python para registrar, buscar y ordenar expedientes de la
I.E. Andrés Avelino Cáceres (Baños del Inca, Cajamarca).

Usa arreglos paralelos, un archivo de texto separado por `|`,
búsqueda secuencial y ordenamiento por selección.

## Estructura

```
mesa_de_partes/          ← carpeta del repositorio
├── mesa_de_partes/      ← paquete (biblioteca)
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py          menú principal
│   ├── datos.py         constantes y arreglos paralelos
│   ├── validacion.py    entrada de datos validada
│   ├── archivo.py       leer/guardar expedientes.txt
│   ├── expedientes.py   registrar y buscar
│   ├── ordenamiento.py  ordenamiento por selección
│   └── reportes.py      ficha y reporte en pantalla
├── ejecutar.py          para correrlo con ▶ en VS Code
├── pyproject.toml
└── README.md
```

## Cómo ejecutarlo

Desde la carpeta del repositorio:

```bash
python -m mesa_de_partes
```

o abre `ejecutar.py` en VS Code y presiona ▶ Run.

Opcional, instalarlo como biblioteca:

```bash
pip install -e .
mesa-de-partes
```

Los datos se guardan en `expedientes.txt`, en la carpeta desde donde se ejecuta.
