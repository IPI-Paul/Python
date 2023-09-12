INSERT INTO products_17_product (title, content, price, user_id)
	SELECT title, content, price, user_id
	-- increment by last product number
	from products_15_product
