# Avance del proyecto - facturacion y transaciones

## Contenido

Este proyecto simula el nucleo financiero  de una plataforma comercial. La API fue desarrollada utilizando **Python** y el framework **FastAPI**, siguiendo una arquitectura basada en modelos(clientes, facturas y transacciones) y esquemas para validar los datos mediante Pydantic.

---

## Instalacion y configuracion

Seguir los siguientes pasos:
 1. Crear una carpeta del proyecto, y abrila con Visual Studio Code

 2. Abrir una terminal  y ejecutar los sigueinte comandos:
    - Crear un entrono virtual: 
        **windows:** python -m venv .mi_env
        **linux/macos:** python3 -m venv .mi_env
    - Activar el entorno:
        **windows:** .mi_env\Scripts\activate
        **linux/macos:** source .mi_env/bin/activate

 3. Instalar FastAPI, ejecutando comandos en la terminal:
    - Pip install "fastapi[standard]
    - pip list --> ver lista de instalacion

 4. Crear el archivo main.py 

 5. Ejecutar con el comando -> fastapi dev main.py

 6. una vez ejecutado se mostararn unas lineas para poder ver la documentacion interactiva
    - SERVER http://127.0.0.1:8000
    - SERVER http://127.0.0.1:8000/docs
    - Para detener el servidos Uvicorn, se dijita el comando en la consola: ctrl + c

 7. Configuracion git: se creo un repositorio local

    1. Comprobar versiones instaladas de python y git: **pip --version** | **python --version**

    2. Inicializar le repositorio: git init

    3. Configurar tu identidad en git con los siguiente comandos:
        - git config user.name = tu_nombre
        - git config user.email = tu_correo (no necesita ser real)

    3. Crear el archivo `.gitignore` (Archivos o carpetas que NO debe subir al repositorio), se agregaron los archivos:
        - .mi_env
        - __pycache__/

    4. crear el archivo `requirements.txt`(contiene la lista de las librerías que necesita mi proyecto para funcionar)

---

## Como crear un commit

Digitar en la consola los siguientes comandos en ESE ORDEN:

1. **git status** -> Muestra qué archivos fueron modificados, creados y estan listos para el commit
        Los archivos en rojo son los modificados

2. **git add .** -> Agrega todos los archivos modificados 

3. **git commit -m "Mensaje del commit"** -> guarda los cambios (crear commit) con mensajes especificos 

4. **git log** -> Para ver el historial de los commits creados

---
    
## Como vincular con un repositorio GITGHUB:

1. Crear una cuenta en gitghub

2. Configurar la cuenta  de gitghub con el Visual Studio Code

3. Crear repositorio para subir el proyecto

4. En la consola digitar digitar el comando:
    - git push origin **main** --> la rama principal de mi proyecto es main.py


## Creacion de los endpoints , en el archivo main

Se crearon los endpoints de Listar, Listar uno, Crear, Editar y Eliminar:
    - Clientes: Listar_clientes, Listar_cliente, Crear_cliente, Editar_cliente, Eliminar_cliente
    - Facturas: Listar_facturas, Listar_factura, Crear_factura, Editar_factura, Eliminar_factura
    - Transacciones: Listar_transacciones, Listar_transaccion, Crear_transaccion, Editar_transaccion, Eliminar_transaccion.

## Organizacion de carpetas
    -Se creo la carpeta **app**
        - Guardar archivo main y crear archivo conexion_bd 
2. Crear subcarpetas dentro de la carpeta app
    - enrutadores
    - modelos
3. Dentro de las dos carpetas crear 3 archivos : clientes, facturas y transacciones

    app/
    |_enrutadores/
        |__clientes.py
        |__facturas.py
        |__transacciones.py
    |_modelos
        |__clientes.py
        |__facturas.py
        |__transacciones.py
    |_conexion_bd.py
    |_main.py


## Avance 13 
    - Se editaron los archivos de la carpeta enrutadores (instanciar la clase ROUTER)
            rutas_clientes = APIRouter()
            rutas_facturas = APIRouter()
            rutas_transacciones = APIRouter()
    - Se creo el archivo listas donde se importaron todos los modelos
    - Se comprobo el funcionamiento de los endpoints

---

## Avance 14: conexion a base de datos 

1. Se debe Instalar Dependencias sqlmodel:
    pip install sqlmodel
2. con el comando pip list, se verifica si se instalo correctamente el sgl modle y SQLAlchemy
3. En el archivo requirements se debe copiar el numero de la version instalada de sqlmodel:
    sqlmodel >=0.0.39
4. https://sqlmodel.tiangolo.com/
5. 


    
