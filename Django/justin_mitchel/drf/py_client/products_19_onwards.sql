INSERT INTO products_20_product (title, content, price, user_id, public)
	SELECT title, content, price, user_id, public
	-- increment by last product number
	from products_19_product
