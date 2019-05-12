# data_manager.py
import os
import math
import time
import datetime
import psycopg2

# Coneccion y cursor
con = psycopg2.connect("dbname=ventas user=postgres password=1234")
cur = con.cursor()

# showTable(string)
# returns 0 on success
# Muestra la data contenida en una tabla especificada
def showTable(table):
    cur.execute("SELECT * FROM "+ str(table))
    row = cur.fetchone()

    if row is None:
        print("La tabla esta vacia o no existe")
        return 0

    print("Resultado: Tabla " + str(table))
    while row is not None:
        print(row)
        row = cur.fetchone()

    return 0

# insert_new_client(int, string, string)
# returns 0 on success
# Inserta un nuevo valor en la tabla clientes
def insert_new_client(nit, nombre, apellido):

    cur.execute("SELECT nit FROM clientes WHERE nit = " + str(nit))
    row = cur.fetchone()

    if row is None:
        cur.execute("INSERT INTO clientes VALUES (" \
                    + str(nit) + "," + str(nombre) + "," + str(apellido) + \
                    ")")
    else:
        print("cliente ya ingresado")
        return -1

    con.commit()
    return 0

# insert_new_factura(int, int)
# returns factura_id para ser usada en insertar las lineas de la factura
# Inserta un nuevo valor en la tabla clientes
def insert_new_factura(nit, lugar):

    timestamp = datetime.datetime.fromtimestamp(time.time())

    # El bloque revisa si se tiene registrado el nit, si es necesario registrarlo,
    # o si es consumidor final (nit = 0)
    if nit != 0:
        cur.execute("SELECT nit FROM clientes WHERE nit = " + str(nit))
        row = cur.fetchone()

        if row is None:
            print("NIT no se encuentra registrado, es necesario registrar el" + \
            "cliente")

    cur.execute("SELECT COUNT(*) FROM facturas")
    row = cur.fetchone()

    id = int(row[0])

    cur.execute("INSERT INTO facturas VALUES (" \
                + str(id) + "," + str(nit) + "," + str(lugar) + ",'" + \
                str(timestamp) +
                "')")
    if nit != 0:
        cur.execute("INSERT INTO cliente_factura VALUES(" + \
        str(nit) + "," + str(id) + ")")

    con.commit()
    return id

# insert_new_linea_factura(int, int, float, float)
# returns 0 on success
# Inserta un nuevo valor en la tabla lineas_de_facturas
def insert_new_linea_factura(factura_id, producto_id):
    cur.execute("SELECT * FROM productos WHERE id = " + \
                str(producto_id) + " AND atributo = 'precio'")
    row = cur.fetchone()

    precio = float(row[2])

    cur.execute("SELECT * FROM productos WHERE id = " + \
                str(producto_id) + " AND atributo = 'tax'")
    row = cur.fetchone()

    total_con_tax = precio + precio*float(row[2])


    cur.execute("INSERT INTO lineas_de_facturas VALUES (" \
                + str(factura_id) + "," + str(producto_id) + "," \
                + str(precio) + "," + str(total_con_tax) + ")")

    con.commit()
    return 0

# insert_new_producto(int, string, string)
# returns 0 on success
# Inserta un nuevo valor en la tabla produtos y si es necesario en: marcas,
# producto_marca, categorias y producto_categoria
def insert_new_producto(id, atributo, valor):
    cur.execute("INSERT INTO productos VALUES (" \
                + str(id) + "," + str(atributo) + "," + str(valor) + ")")
    con.commit()

    # se busca si la marca esta registrada, sino se registra
    if atributo == "'marca'":
        cur.execute("SELECT * FROM marcas WHERE nombre = " + str(valor))
        row = cur.fetchone()
        marca_id = 0
        if row is None:
            cur.execute("SELECT COUNT(id) FROM marcas")
            row = cur.fetchone()

            marca_id = row[0]

            cur.execute("INSERT INTO marcas VALUES (" \
                        + str(marca_id) + "," + str(valor) + ")")
        else:
            marca_id = row[0]

        cur.execute("INSERT INTO producto_marca VALUES (" \
                    + str(id) + "," + str(marca_id) + ")")
        con.commit()

    # se busca si la categoria esta registrada, sino se registra
    if atributo == "'categoria'":
        cur.execute("SELECT id FROM categorias WHERE nombre = " + str(valor))
        row = cur.fetchone()
        categoria_id = 0
        if row is None:
            cur.execute("SELECT COUNT(id) FROM categorias")
            row = cur.fetchone()

            categoria_id = row[0]

            cur.execute("INSERT INTO categorias VALUES (" \
                        + str(categoria_id) + "," + str(valor) + ")")
        else:
            categoria_id = row[0]

        cur.execute("INSERT INTO producto_categoria VALUES (" \
                    + str(id) + "," + str(categoria_id) + ")")
        con.commit()

    return 0

def closeModule():
    cur.close()
    con.close()
