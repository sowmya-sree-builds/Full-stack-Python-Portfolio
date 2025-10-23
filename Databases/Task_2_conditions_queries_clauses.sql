CREATE TABLE Orders (
	OrderID INT PRIMARY KEY,
	CustomerName VARCHAR(50),
	Product VARCHAR(50),
	Category VARCHAR(30),
	Quantity INT,
	Price INT,
	OrderDate DATE,
	City VARCHAR(30)
);
INSERT INTO Orders (OrderID, CustomerName, Product, Category, Quantity, Price, OrderDate, City) VALUES
(101, 'Ravi Kumar', 'Laptop', 'Electronics', 1, 55000, '2023-01-15', 'Hyderabad'),
(102, 'Priya Sharma', 'Mobile Phone', 'Electronics', 2, 18000, '2023-02-20', 'Bangalore'),
(103, 'Arjun Reddy', 'Headphones', 'Accessories', 3, 1500, '2023-03-05', 'Chennai'),
(104, 'Sneha Gupta', 'T-shirt', 'Fashion', 4, 700, '2023-03-25', 'Mumbai'),
(105, 'Manish Verma', 'Shoes', 'Fashion', 2, 2500, '2023-04-10', 'Delhi'),
(106, 'Kavya Iyer', 'Smartwatch', 'Electronics', 1, 12000, '2023-04-22', 'Pune'),
(107, 'Rohit Yadav', 'Refrigerator', 'HomeAppliance', 1, 30000, '2023-05-01', 'Hyderabad'),
(108, 'Ananya Singh', 'WashingMachine', 'HomeAppliance', 1, 22000, '2023-05-15', 'Bangalore'),
(109, 'Karan Patel', 'Microwave', 'HomeAppliance', 1, 9000, '2023-06-12', 'Chennai'),
(110, 'Neha Joshi', 'Jeans', 'Fashion', 2, 1800, '2023-07-05', 'Mumbai'),
(111, 'Suresh Raina', 'TV', 'Electronics', 1, 40000, '2023-07-18', 'Delhi'),
(112, 'Aditi Mehra', 'Dress', 'Fashion', 3, 3500, '2023-08-02', 'Pune'),
(113, 'Harish Kumar', 'Mobile Phone', 'Electronics', 1, 20000, '2023-08-20', 'Hyderabad'),
(114, 'Divya Nair', 'Mixer Grinder', 'HomeAppliance', 2, 5000, '2023-09-10', 'Bangalore'),
(115, 'Vivek Sharma', 'Jacket', 'Fashion', 1, 3000, '2023-09-22', 'Chennai');
-- 1. Find all orders placed from the city Hyderabad
SELECT *
FROM Orders
WHERE City = 'Hyderabad';

-- 2. List all products whose price is greater than 20000
SELECT Product, Price
FROM Orders
WHERE Price > 20000;

-- 3.Display all orders sorted by Price in descending order.
SELECT *
FROM Orders
ORDER BY Price DESC;

-- 4. Show the list of customers sorted by OrderDate in ascending order.
SELECT CustomerName, OrderDate, Product, Price, City
FROM Orders
ORDER BY OrderDate ASC;

-- 5. Find the total number of orders placed in each City
SELECT City, COUNT(*) AS TotalOrders
FROM Orders
GROUP BY City;


-- 6. Find categories where the total sales amount is more than 30000
SELECT Category, SUM(Price * Quantity) AS TotalSales
FROM Orders
GROUP BY Category
HAVING SUM(Price * Quantity) > 30000;

-- 7. Get the list of unique Cities from which orders were placed
SELECT DISTINCT City
FROM Orders;

-- 8. Find all unique Product Categories
SELECT DISTINCT Category
FROM Orders;

-- 9. Display the 5 most recent orders
SELECT *
FROM Orders
ORDER BY OrderDate DESC
LIMIT 5;

-- 10. Show the top 3 most expensive products ordered
SELECT Product, Price, CustomerName, OrderDate
FROM Orders
ORDER BY Price DESC
LIMIT 3;


