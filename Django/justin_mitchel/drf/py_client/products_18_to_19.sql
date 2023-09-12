INSERT INTO products_19_product (title, content, price, user_id, public)
	SELECT title, content, price, user_id, false as public
	-- increment by last product number
	from products_18_product
