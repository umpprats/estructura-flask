# estructura-flask
Estructura básica en framework Flask
## Requerimientos previos para usar con MySQL

## Opción 1)

 Para la librería **mysqlclient** se necesita previamente tener instalado lo siguiente:
**Linux**:
sudo apt-get install python3-dev default-libmysqlclient-dev libmysqlclient-dev build-essential
$ export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
$ export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`
Referencia: https://pypi.org/project/mysqlclient/

## Opción 2)

Si no se quiere utilizar controladores que utilicen las librerías del lenguaje C:
https://pypi.org/project/mysql-connector-python/

## Requerimientos previos para usar con PostgreSQL
**Psycopg** es un adaptador de Python para PostgreSQL. Es una biblioteca de código abierto que proporciona una interfaz Python para conectarse y trabajar con bases de datos PostgreSQL.
Referencia:
https://pypi.org/project/psycopg/
https://www.psycopg.org/psycopg3/docs/basic/install.html
