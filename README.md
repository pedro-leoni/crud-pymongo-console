# Pymongo CRUD console
Una consola simple que permite ejecutar operaciones CRUD sobre una lista de tareas guardadas en una coleccion de mongodb.

## Requerimientos para probar
- Python 3.10.8 en adelante
- MongoDB 6.0.0
## Instrucciones para probar
1. Crear una base de datos en mongo con el nombre todo_console
2. Crear una coleccion en esa base de datos con el nombre tasks
3. Existe la posibilidad de que tengas que insertar un elemento manualmente dentro de dicha coleccion para que esta db pueda ser detectada
4. Crear un entorno virtual de python
5. Clonar el repositorio
6. Escribir el siguiente comando para instalar los requirements

    ```
    pip install -r requirements.txt
    ```
7. Ejecutar el archivo main.py (asegurarse de tener activado el venv)

    ```
    python ./main.py
    ```
