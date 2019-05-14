    CREATE OR REPLACE FUNCTION add_product(marca INTEGER, categoria INTEGER) 
    RETURNS void AS $$
    DECLARE
			newID INT;
		BEGIN
			newID = (SELECT id_producto
			FROM producto_marca
			ORDER BY id_producto DESC
			LIMIT 1) + 1;
			
			INSERT INTO producto_marca VALUES(newid, marca);
			INSERT INTO producto_categoria VALUES(newid, marca);
			
		END;
    $$ LANGUAGE plpgsql
		
		
