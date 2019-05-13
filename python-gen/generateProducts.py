import random
import string

queries = open("queriesP.txt", "w+")
#Marcas (1 a 7)
#Categorias (1 a 7)
Atributo= ['Peso', 'accesorio', 'volumen', 'teclas', 'color']
Fecha = ['20190501', '20190502', '20190503', '20190504', '20190505']
for a in range(500):
    marca = random.randint(1,7)
    cat = random.randint(1,7)
    atrb = []
    atrbval = []
    natr = random.randint(0, 4)
    for b in range(natr): #up to 5 attributes
        atrb.append(Atributo[natr])
        atrbval.append(random.randint(0, 5000))
    #Insertar marca para cada producto
    queries.write('''INSERT INTO public.producto_marca VALUES ('''+str(a)+''','''+str(marca)+''');\n''')
    #Insertar categoria para cada producto
    queries.write('''INSERT INTO public.producto_categoria VALUES ('''+str(a)+''','''+str(cat)+''');\n''')
    #insertar cada atributo para cada producto
    for atr in range(len(atrb)):
        queries.write('''INSERT INTO public.productos VALUES ('''+str(a)+''',\''''+str(atrb[atr])+'''\',\''''+str(atrbval[atr])+'''\');\n''')

print("done")
