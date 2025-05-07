SELECT p.maker, m.model, m.type, m.speed, 
       CASE 
           WHEN m.type = 'PC' THEN MIN(pc.price) 
           ELSE MIN(l.price) 
       END as price
FROM Product p
JOIN (
    SELECT model, 'PC' as type, speed
    FROM PC
    WHERE speed = (SELECT MIN(speed) FROM PC)
    UNION
    SELECT model, 'Laptop' as type, speed
    FROM Laptop
    WHERE speed = (SELECT MIN(speed) FROM Laptop)
) m ON p.model = m.model
LEFT JOIN PC pc ON m.model = pc.model AND m.type = 'PC'
LEFT JOIN Laptop l ON m.model = l.model AND m.type = 'Laptop'
GROUP BY p.maker, m.model, m.type, m.speed;