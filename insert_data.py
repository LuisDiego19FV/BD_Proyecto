import random as rand
import data_manager_module as dm        # dm = datam manager

### insertar clientes ###
dm.insert_new_client(10000, "'Diego'", "'Fernandez'")
dm.insert_new_client(10001, "'Andres'", "'Garcia'")
dm.insert_new_client(10002, "'Miguel'", "'Manuel'")
dm.insert_new_client(10003, "'Laura'", "'Valdez'")
dm.insert_new_client(10004, "'Javier'", "'Alvarado'")
dm.insert_new_client(10005, "'Andrea'", "'Miranda'")
dm.insert_new_client(10006, "'Maria'", "'Garcia'")
dm.insert_new_client(10007, "'Luis'", "'Miguel'")
dm.insert_new_client(10008, "'Carlos'", "'Fernandez'")
dm.insert_new_client(10009, "'Isabela'", "'Estrada'")

### insertar productos ###
# producto 1
dm.insert_new_producto(1, "'nombre'", "'banana'")
dm.insert_new_producto(1, "'precio'", "'3.50'")
dm.insert_new_producto(1, "'tax'", "'0.15'")
dm.insert_new_producto(1, "'marca'", "'chiquita'")
dm.insert_new_producto(1, "'categoria'", "'comida'")
dm.insert_new_producto(1, "'tamano'", "'mediano'")

# producto 2
dm.insert_new_producto(2, "'nombre'", "'manzana'")
dm.insert_new_producto(2, "'precio'", "'4.00'")
dm.insert_new_producto(2, "'tax'", "'0.15'")
dm.insert_new_producto(2, "'marca'", "'manzanal'")
dm.insert_new_producto(2, "'categoria'", "'comida'")
dm.insert_new_producto(2, "'color'", "'verde'")

# producto 3
dm.insert_new_producto(3, "'nombre'", "'manzana'")
dm.insert_new_producto(3, "'precio'", "'4.20'")
dm.insert_new_producto(3, "'tax'", "'0.15'")
dm.insert_new_producto(3, "'marca'", "'manzanal'")
dm.insert_new_producto(3, "'categoria'", "'comida'")
dm.insert_new_producto(3, "'color'", "'rojo'")

# producto 4
dm.insert_new_producto(4, "'nombre'", "'tostador'")
dm.insert_new_producto(4, "'precio'", "'200.00'")
dm.insert_new_producto(4, "'tax'", "'0.10'")
dm.insert_new_producto(4, "'marca'", "'tosty'")
dm.insert_new_producto(4, "'categoria'", "'electronicos'")
dm.insert_new_producto(4, "'lineas'", "'2'")

# producto 5
dm.insert_new_producto(5, "'nombre'", "'microondas'")
dm.insert_new_producto(5, "'precio'", "'1000.00'")
dm.insert_new_producto(5, "'tax'", "'0.10'")
dm.insert_new_producto(5, "'marca'", "'samsung'")
dm.insert_new_producto(5, "'categoria'", "'electronicos'")
dm.insert_new_producto(5, "'watts'", "'750'")

### insertar facturas y lineas de factura ###
# factura 1
fid = dm.insert_new_factura(10000, "'Zona 10'")      # se devuelve el id de factura
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))

# factura 2
fid = dm.insert_new_factura(10001, "'Zona 11'")      # se devuelve el id de factura
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))

# factura 3
fid = dm.insert_new_factura(10002, "'Zona 1'")      # se devuelve el id de factura
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))

# factura 4
fid = dm.insert_new_factura(10003, "'Zona 11'")      # se devuelve el id de factura
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))

# factura 5
fid = dm.insert_new_factura(10004, "'Zona 11'")      # se devuelve el id de factura
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))

# factura 6
fid = dm.insert_new_factura(10005, "'Zona 16'")      # se devuelve el id de factura
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))

# factura 7
fid = dm.insert_new_factura(10006, "'Zona 16'")      # se devuelve el id de factura
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))

# factura 8
fid = dm.insert_new_factura(10007, "'Zona 16'")      # se devuelve el id de factura
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))

# factura 9
fid = dm.insert_new_factura(10008, "'Zona 10'")      # se devuelve el id de factura
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))

# factura 10
fid = dm.insert_new_factura(10009, "'Zona 10'")      # se devuelve el id de factura
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))
dm.insert_new_linea_factura(fid, rand.randint(1,5))

dm.closeModule()
