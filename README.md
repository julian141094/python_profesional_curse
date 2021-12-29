Creando un ambiente virtual de PYTHON con VENV

  Creación de ambiente Virtual:

    python3 -m venv nombre_venv

  Usualmente el nombre del ambiente virtual es venv.
  
  Activación del ambiente virtual:

    Windows:
      .\venv\Scripts\activate

    Unix o MacOS:
      source venv/bin/activate

  Desactivar el ambiente virtual:

    deactivate

  Crear un alias en linux/mac:

    alias nombre-alias="comando"

    Ejemplo: `alias avenv=“source venv/bin/activate”``

Verificar el tipado estatico de un script de python3

  Instalar libreria Mypy

    pip install mypy

  Correr el script con:

    mypy palindrome.py --check-untyped-defs
