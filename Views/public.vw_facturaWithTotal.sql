CREATE VIEW vw_facturaWithTotal
AS
SELECT id, nit, lugar, tiempo, totfact.total 
FROM facturas INNER JOIN  
(SELECT factura_id, sum(precio) total FROM public.lineas_de_facturas GROUP BY factura_id) totfact
ON facturas.id = totfact.factura_id