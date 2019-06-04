import random
import string
from faker import Faker
import psycopg2

fake = Faker()

password_ = input("Enter Password: ")


def begin_transaction():    
    transaction = psycopg2.connect(user="postgres",
                                  password=password_,
                                  host="127.0.0.1",
                                  port="5432",
                                  database="PROYECTO23")
    return transaction
queries = open("queriesmillon.txt", "w+")
#Marcas (1 a 7)
#Categorias (1 a 7)
#Atributo= ['Peso', 'accesorio', 'volumen', 'teclas', 'color']
Fecha = input("Fecha: ")
#generar 500 clientes
lugar = 'tiendaDiego'
for a in range(100):
    transaction = begin_transaction()
    transaction.autocommit=False
    cursor=transaction.cursor()
    nombre = fake.name()
    apellido = fake.name()
    nit = ''.join(random.choice(string.digits) for _ in range(8))
    query=('''INSERT INTO public.clientes VALUES ('''+str(nit)+''',\''''+str(nombre)+'''\',\''''+str(apellido)+'''\')''')
    cursor.execute(query)
    ##cada cliente tiene la posibilidad de hacer 1 a 3 facturas diarias
    for b in range(10000):
        idFactura = ''.join(random.choice(string.digits) for _ in range(12))
        tiempo = Fecha
        query=('''INSERT INTO public.facturas VALUES ('''+str(idFactura)+''','''+str(nit)+''',\''''+str(lugar)+'''\',\''''+str(tiempo)+'''\')''')
        cursor.execute(query)
        ##Cada factura puede tener entre 1 y 50 productos
        for c in range(2):
            productID = random.randint(0, 472)
            precio= random.randint(0, 5000)
            tax=precio+(precio*.1)
            query=('''INSERT INTO public.lineas_de_facturas VALUES ('''+str(idFactura)+''','''+str(productID)+''','''+str(precio)+''','''+str(tax)+''');\n''')
            cursor.execute(query)
    transaction.commit()
    cursor.close()
    transaction.close()

queries.close()
print("done")
