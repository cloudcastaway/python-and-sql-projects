SELECT COUNT(maker) AS number_of_unique_makers
FROM (
    SELECT maker
    FROM Product
    GROUP BY maker
    HAVING COUNT(model) = 1
) AS unique_makers;