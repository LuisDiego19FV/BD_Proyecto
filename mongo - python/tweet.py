import psycopg2
import random
from twython import Twython
from pymongo import MongoClient
from auth import (consumer_key, consumer_secret, access_token, access_token_secret)

conn=psycopg2.connect("dbname=NuevoProyecto user=postgres password=1997sergito")
twitter=Twython(consumer_key, consumer_secret, access_token, access_token_secret)
cur=conn.cursor()

# BUSQUEDA DE CLIENTES PREFERENCIALES (PCs). CLIENTES CON MAS VOLUMEN DE FACTURACION
cur.execute('''
SELECT clientes.nit, clientes.primer_nombre, clientes.apellido, count(facturas.*) as facturas 
FROM clientes, facturas 
WHERE clientes.nit = facturas.nit 
GROUP BY clientes.nit, clientes.primer_nombre, clientes.apellido 
ORDER BY facturas DESC, clientes.nit LIMIT 5;
''')

PC1=cur.fetchone()
# print(PC1)
PC2=cur.fetchone()
# print(PC2)
PC3=cur.fetchone()
# print(PC3)
PC4=cur.fetchone()
# print(PC4)
PC5=cur.fetchone()
# print(PC5)

# BUSQUEDA DE FACTURAS HECHAS POR UN CLIENTE PREFERENCIAL

nitCP1=str((PC1[0]))
nitCP2=str((PC2[0]))
nitCP3=str((PC3[0]))
nitCP4=str((PC4[0]))
nitCP5=str((PC5[0]))

number=random.randint(0, 804564563149)
ran_id=str(number)

cur.execute("SELECT * FROM facturas WHERE nit = " + nitCP1 + "and id > " + ran_id + ";")
res1=cur.fetchone()
# print(res1)
idFac1=str(res1[0])
cur.execute("SELECT * FROM facturas WHERE nit = " + nitCP2 + "and id > " + ran_id + ";")
res2=cur.fetchone()
# print(res2)
idFac2=str(res2[0])
cur.execute("SELECT * FROM facturas WHERE nit = " + nitCP3 + "and id > " + ran_id + ";")
res3=cur.fetchone()
# print(res3)
idFac3=str(res3[0])
cur.execute("SELECT * FROM facturas WHERE nit = " + nitCP4 + "and id > " + ran_id + ";")
res4=cur.fetchone()
# print(res4)
idFac4=str(res4[0])
cur.execute("SELECT * FROM facturas WHERE nit = " + nitCP5 + "and id > " + ran_id + ";")
res5=cur.fetchone()
# print(res5)
idFac5=str(res5[0])


# BUSQEUDA DE LOS PRODUCTOS MAS APROPIADOS PARA EL CLIENTE PREFERENCIAL
cur.execute('''
SELECT lineas_de_facturas.factura_id, lineas_de_facturas.producto_id, COUNT(lineas_de_facturas.producto_id) as n 
FROM facturas, lineas_de_facturas 
WHERE lineas_de_facturas.factura_id = ''' + idFac1 + ''' 
GROUP BY lineas_de_facturas.factura_id, lineas_de_facturas.producto_id
ORDER BY lineas_de_facturas.factura_id ASC, n DESC LIMIT 10;''')
tc11=cur.fetchone()
pf11=str(tc11[1])
tc12=cur.fetchone()
pf12=str(tc12[1])

cur.execute('''
SELECT lineas_de_facturas.factura_id, lineas_de_facturas.producto_id, COUNT(lineas_de_facturas.producto_id) as n 
FROM facturas, lineas_de_facturas 
WHERE lineas_de_facturas.factura_id = ''' + idFac2 + ''' 
GROUP BY lineas_de_facturas.factura_id, lineas_de_facturas.producto_id
ORDER BY lineas_de_facturas.factura_id ASC, n DESC LIMIT 10;''')
tc21=cur.fetchone()
pf21=str(tc21[1])
tc22=cur.fetchone()
pf22=str(tc22[1])

cur.execute('''
SELECT lineas_de_facturas.factura_id, lineas_de_facturas.producto_id, COUNT(lineas_de_facturas.producto_id) as n 
FROM facturas, lineas_de_facturas 
WHERE lineas_de_facturas.factura_id = ''' + idFac3 + ''' 
GROUP BY lineas_de_facturas.factura_id, lineas_de_facturas.producto_id
ORDER BY lineas_de_facturas.factura_id ASC, n DESC LIMIT 10;''')
tc31=cur.fetchone()
pf31=str(tc31[1])
tc32=cur.fetchone()
pf32=str(tc32[1])

cur.execute('''
SELECT lineas_de_facturas.factura_id, lineas_de_facturas.producto_id, COUNT(lineas_de_facturas.producto_id) as n 
FROM facturas, lineas_de_facturas 
WHERE lineas_de_facturas.factura_id = ''' + idFac4 + ''' 
GROUP BY lineas_de_facturas.factura_id, lineas_de_facturas.producto_id
ORDER BY lineas_de_facturas.factura_id ASC, n DESC LIMIT 10;''')
tc41=cur.fetchone()
pf41=str(tc41[1])
tc42=cur.fetchone()
pf42=str(tc42[1])

cur.execute('''
SELECT lineas_de_facturas.factura_id, lineas_de_facturas.producto_id, COUNT(lineas_de_facturas.producto_id) as n 
FROM facturas, lineas_de_facturas 
WHERE lineas_de_facturas.factura_id = ''' + idFac5 + ''' 
GROUP BY lineas_de_facturas.factura_id, lineas_de_facturas.producto_id
ORDER BY lineas_de_facturas.factura_id ASC, n DESC LIMIT 10;''')
tc51=cur.fetchone()
pf51=str(tc51[1])
tc52=cur.fetchone()
pf52=str(tc52[1])


# BUSQEUDA DE LA DESCRIPCION DE LOS PRODUCTOS PARA EL CLIENTE PREFERENCIAL

cur.execute("SELECT * FROM productos WHERE id = " + pf11 + " OR id = " + pf12 + ";")
at11=cur.fetchone()
at11=str(at11[1])
at12=cur.fetchone()
at12=str(at12[1])

cur.execute("SELECT * FROM productos WHERE id = " + pf21 + " OR id = " + pf22 + ";")
at21=cur.fetchone()
at21=str(at21[1])
at22=cur.fetchone()
at22=str(at22[1])

cur.execute("SELECT * FROM productos WHERE id = " + pf31 + " OR id = " + pf32 + ";")
at31=cur.fetchone()
at31=str(at31[1])
at32=cur.fetchone()
at32=str(at32[1])

cur.execute("SELECT * FROM productos WHERE id = " + pf41 + " OR id = " + pf42 + ";")
at41=cur.fetchone()
at41=str(at41[1])
at42=cur.fetchone()
at42=str(at42[1])

cur.execute("SELECT * FROM productos WHERE id = " + pf51 + " OR id = " + pf52 + ";")
at51=cur.fetchone()
at51=str(at51[1])
at52=cur.fetchone()
at52=str(at52[1])

# ENVIO DEL MENSAJE A CADA CLIENTE PREFERENCIAL CON OFERTAS POR TWITTER

if (at11 == at12):
    tweet1 = ("Cliente Preferencial: " + PC1[1] + " tenemos ofertas para ti, " + at11 + " esta en promocion este mes!")
    message=tweet1
    twitter.update_status(status=tweet1)
    print("Tweeted 1!")
else:
    tweet1 = ("Cliente Preferencial: " + PC1[1] + " tenemos ofertas para ti, " + at11 + " y " + at12 + " estan en promocion este mes!")
    message=tweet1
    twitter.update_status(status=tweet1)
    print("Tweeted 1!")

if (at21 == at22):
    tweet2 = ("Cliente Preferencial: " + PC2[1] + " tenemos ofertas para ti, " + at21 + " esta en promocion este mes!")
    message=tweet2
    twitter.update_status(status=tweet2)
    print("Tweeted 2!")
else:
    tweet2 = ("Cliente Preferencial: " + PC2[1] + " tenemos ofertas para ti, " + at21 + " y " + at22 + " estan en promocion este mes!")
    message=tweet2
    twitter.update_status(status=tweet2)
    print("Tweeted 2!")

if (at31 == at32):
    tweet3 = ("Cliente Preferencial: " + PC3[1] + " tenemos ofertas para ti, " + at31 + " esta en promocion este mes!")
    message=tweet3
    twitter.update_status(status=tweet3)
    print("Tweeted 3!")
else:
    tweet3 = ("Cliente Preferencial: " + PC3[1] + " tenemos ofertas para ti, " + at31 + " y " + at32 + " estan en promocion este mes!")
    message=tweet3
    twitter.update_status(status=tweet3)
    print("Tweeted 3!")

if (at41 == at42):
    tweet4= ("Cliente Preferencial: " + PC4[1] + " tenemos ofertas para ti, " + at41 + " esta en promocion este mes!")
    message=tweet4
    twitter.update_status(status=tweet4)
    print("Tweeted 4!")
else:
    tweet4 = ("Cliente Preferencial: " + PC4[1] + " tenemos ofertas para ti, " + at41 + " y " + at42 + " estan en promocion este mes!")
    message=tweet4
    twitter.update_status(status=tweet4)
    print("Tweeted 4!")

if (at51 == at52):
    tweet5 = ("Cliente Preferencial: " + PC5[1] + " tenemos ofertas para ti, " + at51 + " esta en promocion este mes!")
    message=tweet5
    twitter.update_status(status=tweet5)
    print("Tweeted 5!")
else:
    tweet5 = ("Cliente Preferencial: " + PC5[1] + " tenemos ofertas para ti, " + at51 + " y " + at52 + " estan en promocion este mes!")
    message=tweet5
    twitter.update_status(status=tweet5)
    print("Tweeted 5!")

