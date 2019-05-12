DROP TABLE IF EXISTS clientes CASCADE;
DROP TABLE IF EXISTS productos CASCADE;
DROP TABLE IF EXISTS marcas CASCADE;
DROP TABLE IF EXISTS categorias CASCADE;
DROP TABLE IF EXISTS facturas CASCADE;
DROP TABLE IF EXISTS lineas_de_facturas;
DROP TABLE IF EXISTS cliente_factura;
DROP TABLE IF EXISTS producto_marca;
DROP TABLE IF EXISTS producto_categoria;

CREATE TABLE clientes(
  nit INT,
  primer_nombre VARCHAR(255),
  apellido VARCHAR(255),
  PRIMARY KEY (nit)
);

CREATE TABLE productos(
  id INT,
  atributo VARCHAR(255),
  valor VARCHAR(255)
);

CREATE TABLE marcas(
  id INT,
  nombre VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE categorias(
  id INT,
  nombre VARCHAR(255),
  PRIMARY KEY (id)
);

CREATE TABLE facturas(
  id INT,
  nit INT,
  lugar VARCHAR(255),
  tiempo TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE lineas_de_facturas(
  factura_id INT,
  producto_id INT,
  precio FLOAT,
  total_con_tax FLOAT,
  FOREIGN KEY (factura_id) REFERENCES facturas(id)
);

CREATE TABLE cliente_factura(
  nit_cliente INT,
  id_factura INT,
  FOREIGN KEY (nit_cliente) REFERENCES clientes(nit),
  FOREIGN KEY (id_factura) REFERENCES facturas(id)
);

CREATE TABLE producto_marca(
  id_producto INT,
  id_marca INT,
  FOREIGN KEY (id_marca) REFERENCES marcas(id)
);

CREATE TABLE producto_categoria(
  id_producto INT,
  id_categoria INT,
  FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);
