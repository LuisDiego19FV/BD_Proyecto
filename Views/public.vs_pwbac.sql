CREATE VIEW vw_ProductWithBrandAndCategory AS 
SELECT mp.id_producto ProductID, mp.nombre Marca, cp.nombre Categoria
FROM
(SELECT id_producto, nombre FROM producto_marca INNER JOIN marcas on producto_marca.id_marca = marcas.id) mp
INNER JOIN
(SELECT id_producto, nombre FROM producto_categoria INNER JOIN categorias on producto_categoria.id_categoria = categorias.id) cp
ON mp.id_producto = cp.id_producto