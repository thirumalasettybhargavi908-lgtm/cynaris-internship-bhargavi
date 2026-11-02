SELECT product_name, category, price 
FROM sales;

SELECT * 
FROM sales 
WHERE category = 'Electronics' AND price > 500;

SELECT * 
FROM sales 
WHERE category = 'Furniture' OR category = 'Appliances';

SELECT * 
FROM sales 
WHERE NOT category = 'Electronics';

SELECT * 
FROM sales 
WHERE product_name LIKE 'Laptop%';

SELECT * 
FROM sales 
WHERE category IN ('Electronics', 'Footwear', 'Furniture');

SELECT * 
FROM sales 
WHERE price BETWEEN 50 AND 200;

SELECT * 
FROM sales 
WHERE discount IS NULL;