from pymongo import MongoClient
from twython import Twython
import random
import psycopg2

from auth import (consumer_key,consumer_secret,access_token,access_token_secret)

client = MongoClient("mongodb://localhost:27017/")
database = client["PROYECTO-DB"]
collection = database["clientes"]
twitter = Twython (consumer_key, consumer_secret, access_token, access_token_secret)

conn=psycopg2.connect("dbname=NuevoProyecto user=postgres password=1997sergito")
cur=conn.cursor()

cur.execute('''
SELECT clientes.nit, clientes.primer_nombre, clientes.apellido, count(facturas.*) as facturas
FROM clientes, facturas
WHERE clientes.nit = facturas.nit
GROUP BY clientes.nit, clientes.primer_nombre, clientes.apellido
ORDER BY facturas DESC, clientes.nit LIMIT 5;
''')

PC1=cur.fetchone()
PC1f = PC1[0]
# print(PC1f)
PC2=cur.fetchone()
PC2f = PC2[0]
# print(PC2f)
PC3=cur.fetchone()
PC3f = PC3[0]
# print(PC3f)
PC4=cur.fetchone()
PC4f = PC4[0]
# print(PC4f)
PC5=cur.fetchone()
PC5f = PC5[0]
# print(PC5f)

# query = { "primer_nombre": {"$regex": "El", "$options": "i"} }


collection = database["clientes"]
query = {"nit": PC1f}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('primer_nombre')
finally:
    client.close()
nombreC = message
print(message)
######## PARTE 2 ########

collection = database["facturas"]
query = {"nit": PC1f}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('id')
        message=str(message)
finally:
    client.close()
print("id_factura "+message)
message = int(message)

######## PARTE 3 ########

collection = database["linea_de_facturas"]
query = {"factura_id": message}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('producto_id')
        message=str(message)
finally:
    client.close()
producto=(message)
print("id_producto: "+message)

if (producto=="1"):
    producto = "teclas"
elif (producto == "2"):
    producto = "accesorios"
elif (producto == "3"):
    producto = "volumen"


print("CLIENTE PREFERENCIAL: "+nombreC+" tiene una oferta del producto "+producto)
tweet1 = ("CLIENTE PREFERENCIAL: "+nombreC+" tiene una oferta del producto "+producto)
twitter.update_status(status=tweet1)
print("Tweeted! 1")

collection = database["clientes"]
query = {"nit": PC2f}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('primer_nombre')
finally:
    client.close()
nombreC = message
print(message)
######## PARTE 2 ########

collection = database["facturas"]
query = {"nit": PC2f}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('id')
        message=str(message)
finally:
    client.close()
print("id_factura "+message)
message = int(message)

######## PARTE 3 ########

collection = database["linea_de_facturas"]
query = {"factura_id": message}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('producto_id')
        message=str(message)
finally:
    client.close()
producto=(message)
print("id_producto: "+message)

if (producto=="1"):
    producto = "teclas"
elif (producto == "2"):
    producto = "accesorios"
elif (producto == "3"):
    producto = "volumen"


print("CLIENTE PREFERENCIAL: "+nombreC+" tiene una oferta del producto "+producto)
tweet2 = ("CLIENTE PREFERENCIAL: "+nombreC+" tiene una oferta del producto "+producto)
twitter.update_status(status=tweet2)
print("Tweeted! 2")

collection = database["clientes"]
query = {"nit": PC3f}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('primer_nombre')
finally:
    client.close()
nombreC = message
print(message)
######## PARTE 2 ########

collection = database["facturas"]
query = {"nit": PC3f}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('id')
        message=str(message)
finally:
    client.close()
print("id_factura "+message)
message = int(message)

######## PARTE 3 ########

collection = database["linea_de_facturas"]
query = {"factura_id": message}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('producto_id')
        message=str(message)
finally:
    client.close()
producto=(message)
print("id_producto: "+message)

if (producto=="1"):
    producto = "teclas"
elif (producto == "2"):
    producto = "accesorios"
elif (producto == "3"):
    producto = "volumen"


print("CLIENTE PREFERENCIAL: "+nombreC+" tiene una oferta del producto "+producto)
tweet3 = ("CLIENTE PREFERENCIAL: "+nombreC+" tiene una oferta del producto "+producto)
twitter.update_status(status=tweet3)
print("Tweeted! 3")

collection = database["clientes"]
query = {"nit": PC4f}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('primer_nombre')
finally:
    client.close()
nombreC = message
print(message)
######## PARTE 2 ########

collection = database["facturas"]
query = {"nit": PC4f}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('id')
        message=str(message)
finally:
    client.close()
print("id_factura "+message)
message = int(message)

######## PARTE 3 ########

collection = database["linea_de_facturas"]
query = {"factura_id": message}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('producto_id')
        message=str(message)
finally:
    client.close()
producto=(message)
print("id_producto: "+message)

if (producto=="1"):
    producto = "teclas"
elif (producto == "2"):
    producto = "accesorios"
elif (producto == "3"):
    producto = "volumen"


print("CLIENTE PREFERENCIAL: "+nombreC+" tiene una oferta del producto "+producto)
tweet4 = ("CLIENTE PREFERENCIAL: "+nombreC+" tiene una oferta del producto "+producto)
twitter.update_status(status=tweet4)
print("Tweeted! 4")

collection = database["clientes"]
query = {"nit": PC5f}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('primer_nombre')
finally:
    client.close()
nombreC = message
print(message)
######## PARTE 2 ########

collection = database["facturas"]
query = {"nit": PC5f}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('id')
        message=str(message)
finally:
    client.close()
print("id_factura "+message)
message = int(message)

######## PARTE 3 ########

collection = database["linea_de_facturas"]
query = {"factura_id": message}
cursor = collection.find(query)
try:
    for doc in cursor:
        message=doc.get('producto_id')
        message=str(message)
finally:
    client.close()
producto=(message)
print("id_producto: "+message)

if (producto=="1"):
    producto = "teclas"
elif (producto == "2"):
    producto = "accesorios"
elif (producto == "3"):
    producto = "volumen"


print("CLIENTE PREFERENCIAL: "+nombreC+" tiene una oferta del producto "+producto)
tweet5 = ("CLIENTE PREFERENCIAL: "+nombreC+" tiene una oferta del producto "+producto)
twitter.update_status(status=tweet5)
print("Tweeted! 5")