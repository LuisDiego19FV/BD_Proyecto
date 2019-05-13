import random
import string
from faker import Faker

fake = Faker()


queries = open("queriesClientes.txt", "w+")
#Marcas (1 a 7)
#Categorias (1 a 7)
#Atributo= ['Peso', 'accesorio', 'volumen', 'teclas', 'color']
Fecha = ['20190501', '20190502', '20190503', '20190504', '20190505']
#generar 500 clientes
lugar = 'tiendaDiego'
for a in range(500):    
    nombre = fake.name()
    apellido = fake.name()
    nit = ''.join(random.choice(string.digits) for _ in range(8))
    queries.write('''INSERT INTO public.clientes VALUES ('''+str(nit)+''',\''''+str(nombre)+'''\',\''''+str(apellido)+'''\');\n''')
    ##cada cliente tiene la posibilidad de hacer 1 a 3 facturas diarias
    for b in range(random.randint(1,2)):
        idFactura = ''.join(random.choice(string.digits) for _ in range(8))
        tiempo = Fecha[random.randint(0, 4)]
        queries.write('''INSERT INTO public.facturas VALUES ('''+str(idFactura)+''','''+str(nit)+''',\''''+str(lugar)+'''\',\''''+str(tiempo)+'''\');\n''')
        ##Cada factura puede tener entre 1 y 50 productos
        for c in range(random.randint(1,49)):
            productID = random.randint(0, 472)
            precio= random.randint(0, 5000)
            tax=precio+(precio*.1)
            queries.write('''INSERT INTO public.lineas_de_facturas VALUES ('''+str(idFactura)+''','''+str(productID)+''','''+str(precio)+''','''+str(tax)+''');\n''')
print("done")
