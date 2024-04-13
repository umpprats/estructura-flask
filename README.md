# estructura-flask
Estructura básica en framework Flask

## Requerimientos previos para usar con MySQL

## Opción 1)

 Para la librería **mysqlclient** se necesita previamente tener instalado lo siguiente:

**Linux**:

`sudo apt-get install python3-dev default-libmysqlclient-dev libmysqlclient-dev build-essential`

`$ export MYSQLCLIENT_CFLAGS=pkg-config mysqlclient --cflags`

`$ export MYSQLCLIENT_LDFLAGS=pkg-config mysqlclient --libs`

Referencia: https://pypi.org/project/mysqlclient/

## Opción 2)

Si no se quiere utilizar controladores que utilicen las librerías del lenguaje C:
https://pypi.org/project/mysql-connector-python/

## Requerimientos previos para usar con PostgreSQL
**Psycopg** es un adaptador de Python para PostgreSQL. Es una biblioteca de código abierto que proporciona una interfaz Python para conectarse y trabajar con bases de datos PostgreSQL.

**Linux Distribución Ubuntu**

`sudo apt-get install python3-dev build-essential libpq-dev`

Referencia:
- https://pypi.org/project/psycopg/
- https://www.psycopg.org/psycopg3/docs/basic/install.html

## Uso de Flask-Migrate
**Flask-Migrate** es una extensión que nos permite manejar migraciones de bases de datos **SQLAlchemy** para aplicaciones desarrolladas en **Flask**.

### Instalación
Después de haber activado el entorno virtual *(venv)*, ejecutar en la terminal:
 
`$ pip install Flask-Migrate`

Para crear un repositorio de migración se debe ejecutar lo siguiente en la terminal:

`$ flask db init`

El anterior comando crea una carpeta *migrations* en proyecto en Flask. Para generar una migración inicial se debe ejecutar el siguiente comando:

`$ flask db migrate -m "Migración Inicial"`

Para generar los cambios descritos en el script de migración, hay que ejecutar:
 
`$ flask db upgrade`

Referencia:
- https://flask-migrate.readthedocs.io/en/latest/

## Estructura del Proyecto
Book Flask Web Development: https://www.oreilly.com/library/view/flask-web-development/9781491991725/

- Project Structure: Page 75

BluePrints: https://flask.palletsprojects.com/es/main/blueprints/
