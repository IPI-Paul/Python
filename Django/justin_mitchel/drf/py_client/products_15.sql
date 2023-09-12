INSERT INTO products_17_product (title, content, price, user_id)
	SELECT title, content, price, 1 as user_id
	from products_16_product
