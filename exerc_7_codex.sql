#7) Entity Relationship Diagram
#Simple order management for a delivery company like "Ifood" or "Rappi"

CREATE TABLE Clients(
    Order_ID INT,
    ID_Client INT PRIMARY KEY,
    NameClient VARCHAR(40),
    Email VARCHAR(40),
    Payment VARCHAR(40),
    Location VARCHAR(40),
);

CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Product VARCHAR(20),
    Quantity INT,
    Price DECIMAL,
    Motoboy_ID INT,
    Restaurant VARCHAR(40)
);

CREATE TABLE Motoboy(
    Motoboy_ID INT PRIMARY KEY,
    MotoboyName VARCHAR(40),
    Order_ID INT,
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID) ON DELETE CASCADE
);

INSERT INTO clients VALUES(3428771, 536781473, 'Jonathas', 'jturner@gmail.com', 'PIX','-21.919741/-47.624415');
INSERT INTO clients VALUES(6564321, 565778235, 'Mario', 'm2234l@gmail.com', 'CREDIT CARD','-21.901698/-47.638568');
INSERT INTO clients VALUES(4212345, 665219576, 'Anne'	,'r52wxy@gmail.com'	, 'PIX', '-21.915455/-47.631962');
INSERT INTO clients VALUES(4860112, 169341674,'Samira'	,'sa_mira@sitbam.com', 'CREDIT CARD', '-21.905112/-47.630770');
INSERT INTO clients VALUES(8978564, 678852213,'Bridget', 'bridget@charm.com', 'CASH', '-21.900109/-47.639676');
INSERT INTO clients VALUES(4421209, 458100931, 'Caleb', 'cc432@dash.com', 'CREDIT CARD', '-21.876997/-47.588411');
INSERT INTO clients VALUES(1216767, 567324998, 'Kathleen', 'kt247220@lola.com', 'CREDIT CARD', '-21.895338/-47.632084');
INSERT INTO clients VALUES(2209865, 743190512, 'Iris', 'I34566@yahoo.com', 'CASH', '-21.918626/-47.625284');
INSERT INTO clients VALUES(3216789, 226701211, 'Miranda', 'miranda_aniston@gmail.com', 'PIX', '-21.897616/-47.616867');


INSERT INTO ORDERS VALUES(3216789, 'Meal of the day', 6, 130.9, 9, 'Beaf and snake');
INSERT INTO ORDERS VALUES (6564321,'Tacos', 4, 70.85, 1, 'Laroc');
INSERT INTO ORDERS VALUES(4421209, 'Sushi',	1,	33.6, 3, 'Miracle');
INSERT INTO ORDERS VALUES(8978564,'Potato pie', 2, 56.2, 4, 'Lissa and cia');
INSERT INTO ORDERS VALUES(4860112,'Bear burger', 4, 94.5, 7, 'Burgers joint');
INSERT INTO ORDERS VALUES(4212345,'Ravioli', 1, 64.8, 8, 'Nonna pina');
INSERT INTO ORDERS VALUES(3428771,'Steak and chips', 2, 47.8, 2, 'Aleroi');
INSERT INTO ORDERS VALUES(2209865, 'Burger veg', 1, 22, 6, 'Mc Donalds');
INSERT INTO ORDERS VALUES(1216767, 'Risotto', 3, 60, 5, 'Olivers');

INSERT INTO motoboy VALUES(1, 'Alison', NULL);
INSERT INTO motoboy VALUES(2, 'Steven', NULL);
INSERT INTO motoboy VALUES(3, 'Drake',	NULL);
INSERT INTO motoboy VALUES(4, 'Jenner',	NULL);
INSERT INTO motoboy VALUES(5, 'Victor', NULL);
INSERT INTO motoboy VALUES(6, 'Finn', NULL);
INSERT INTO motoboy VALUES(7, 'Geronimo', NULL);
INSERT INTO motoboy VALUES(8, 'Zake', NULL);

# List of orders ordered by the number of orders 
SELECT *
FROM orders
ORDER BY quantity ASC;

# Find the number of orders
SELECT COUNT(Order_ID)
FROM orders;

# Find the sum of all orders considering quantity
SELECT SUM(quantity)
FROM orders;

# Find the avarege of money spent by all clients
SELECT AVG(price)
FROM (orders);

# Find the restaurant 
SELECT orders.restaurant
FROM orders
Where orders.price > 50
ORDER BY price DESC;
