# Avance del proyecto - facturacion y transaciones

## Contenido

Este proyecto simula el nucleo financiero  de una plataforma comercial. La API fue desarrollada utilizando **Python** y el framework **FastAPI**, siguiendo una arquitectura basada en modelos(clientes, facturas y transacciones) y esquemas para validar los datos mediante Pydantic.

---

## Avance 1: Instalacion y configuracion

Como primer paso para la creacion de este proyecto se debe:
 1. Crear una carpeta del proyecto, y abrir con Visual Studio Code

 2. Abrir una terminal  y ejecutar los sigueinte comandos:
    - Crear un entrono virtual: 
        **windows:** python -m venv .mi_env
    - Activar el entorno:
        **windows:** .mi_env\Scripts\activate (debe aparecer (.mi_env) PS C:......) 

 3. Instalar FastAPI, ejecutando comandos en la terminal:
    - Pip install "fastapi[standard]
    - pip list --> ver lista de instalacion

 4. Crear el archivo main.py 
    - Ejecutar con el comando -> fastapi dev main.py

 6. una vez ejecutado se mostararn unas lineas para poder ver la documentacion interactiva
    - SERVER http://127.0.0.1:8000
    - SERVER http://127.0.0.1:8000/docs
    - Para detener el servidor Uvicorn, se dijita el comando en la consola: ctrl + c
    - Para limpiar la consola usar el comando **clear**

 7. Se hace una Configuracion git: se crea un repositorio local

    1. Se debe comprobar versiones instaladas de python y git: **pip --version** | **python --version**

    2. Inicializar le repositorio: git init

    3. Configurar tu identidad en git con los siguiente comandos:
        - git config user.name = tu_nombre
        - git config user.email = tu_correo (no necesita ser real)

    3. Crear el archivo `.gitignore` (Archivos o carpetas que NO debe subir al repositorio), se agregaron los archivos:
        - .mi_env
        - __pycache__/

    4. crear el archivo `requirements.txt`(contiene la lista de las librerías que necesita mi proyecto para funcionar)

---

## Avance 2: Creacion de los commits
En la consola ejecutar los siguientes comandos:

1. **git status** -> Muestra qué archivos fueron modificados, creados y estan listos para el commit
        Los archivos en rojo son los modificados

2. **git add .** -> Agrega todos los archivos modificados 

3. **git commit -m "Mensaje del commit"** -> guarda los cambios (crear commit) con mensajes especificos 

4. **git log** -> Para ver el historial de los commits creados

---
    
## Avance 3: Como vincular con un repositorio GITGHUB:

1. Crear una cuenta en gitghub

2. Configurar la cuenta  de gitghub con el Visual Studio Code

3. Crear repositorio para subir el proyecto

4. En la consola digitar digitar el comando:
    - git push origin **main** --> la rama principal de mi proyecto es main.py

---

## Avance 4: Creacion de los Endpoints

Se crearon los endpoints de Listar, Listar uno, Crear, Editar y Eliminar:
    - Clientes: Listar_clientes, Listar_cliente, Crear_cliente, Editar_cliente, Eliminar_cliente
    - Facturas: Listar_facturas, Listar_factura, Crear_factura, Editar_factura, Eliminar_factura
    - Transacciones: Listar_transacciones, Listar_transaccion, Crear_transaccion, Editar_transaccion, Eliminar_transaccion.

## Avance 5: Organizacion de carpetas
1. Se creo la carpeta **app**
    - Guardar archivo main y crear archivo conexion_bd 
2. Crear subcarpetas: Enrutadores - Modelos
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


## Avance 6: Enrutar
    - Se editaron los archivos de la carpeta enrutadores (instanciar la clase ROUTER)
            rutas_clientes = APIRouter()
            rutas_facturas = APIRouter()
            rutas_transacciones = APIRouter()
    - Se creo el archivo listas donde se importaron todos los modelos
    - Se comprobo el funcionamiento de los endpoints

---

## Avance 7: Conexion y Creacion a base de datos 

1. Se debe Instalar Dependencias sqlmodel:
    pip install sqlmodel
2. con el comando pip list, se verifica si se instalo correctamente el sgl modle y SQLAlchemy
3. En el archivo requirements se debe copiar el numero de la version instalada de sqlmodel:
    sqlmodel >=0.0.39
4. https://sqlmodel.tiangolo.com/
5. Se edito el archivo conexion_bd.py
    - se crea el motor para la base de datos
    - Se define el metodo para crear las tablas y la sesion
    - Se creo inyeccion depentencias

    - Se edito el archivo **enrutadores/cliente.py** = se editaron los enpoints de listar_cliente(FastAPI entrega una sesión de la base de datos) y 
        crear_clientes(se añade un cliente, se guarda y refresca automaticamente) mi_sesion.add        (cliente_val)
                     mi_sesion.commit()
                     mi_sesion.refresh(cliente_val)
    Se agrega lista_cli = sesion.exec(select(Cliente)).all() en el enpoint de listar todos los clientes para que ocnuslte todos los clienets que se han guardado en la base de datos 

    - Se edito el archivo **modelos/clientes.py** = Se importo la conixon a sqlmodel, se le asigna un field a los campos de las tablas para que los datos que se envien se guarden **id: None = field(default)=None**, 

    - Se edito el archivo main.py: Dentro de la variable app se pone lifespan=crear_tablas, es decir que ejecuta crear_tablas antes de recibir una peticion

    - Una vez corregido los archivos se creara automaticamente el archivo de base de datos con el nombre asignado en **conexion_bd.py**

6. Para abrir la base de datos se pueden de dos formas:
    - En la Terminal
    - Descargando SQLlite viewer 
7. Se comprobo el funcionamiento de crear cliente y listar todos los clientes


## Avance 8: Crud completo de cliente, facturas y transacciones

1. Se edito el archivo modulos/cliente.py:
        - Se añadieron Field en ClienteBase, Cliente: id con llave primaria
   Se edito el archivo enrutadores/cliente.py:
        - Se añadio una sesion(mi_sesion) de base de datos a listar un solo cliente, Editar un cliente y Elimiar un cliente

2. Se edito el archivo modulos/factura.py:
        - Se añadieron Field en FacturaBase, Factura: id con llave primaria y se añadio una llave foranea con cliente_id
   Se edito el archivo enrutadores/factura.py:
        - Se añadio una sesion(mi_sesion) de base de datos a listar una sola factura, Editar una factura y Elimiar una factura

3. Se edito el archivo modulos/transacciones.py:
        - Se añadieron Field en TransaccionBase, Transaccion: id con llave primaria y se añadio una llave foranea con Factur_id
   Se edito el archivo enrutadores/transacciones.py:
        - Se añadio una sesion(mi_sesion) de base de datos a listar una sola Transaccion, Editar una transaccion y Elimiar una transaccion




    
