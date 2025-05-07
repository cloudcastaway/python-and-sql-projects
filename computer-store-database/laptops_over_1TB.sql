SELECT
	p.maker,
	p.model,
	l.hd,
	l.speed,
	l.price
FROM
	Product AS p
LEFT JOIN 
	Laptop AS l
ON 
	l.model = p.model
WHERE
	l.hd >= 1000
ORDER BY
	l.hd,
	l.speed DESC,
	l.price;