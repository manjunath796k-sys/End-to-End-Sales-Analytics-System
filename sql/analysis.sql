-- SQL analysis queries
-- ==========================================
-- SALES ANALYTICS QUERIES
-- ==========================================

-- 1. Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM orders;

-- 2. Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM orders;

-- 3. Average Sales
SELECT AVG(Sales) AS Average_Sales
FROM orders;

-- 4. Top 10 Highest Sales Orders
SELECT OrderID,
       CustomerID,
       Category,
       Sales,
       Profit
FROM orders
ORDER BY Sales DESC
LIMIT 10;

-- 5. Sales by Category
SELECT Category,
       SUM(Sales) AS Total_Sales
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 6. Profit by Category
SELECT Category,
       SUM(Profit) AS Total_Profit
FROM orders
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 7. Average Discount by Category
SELECT Category,
       AVG(Discount) AS Average_Discount
FROM orders
GROUP BY Category;

-- 8. Total Orders by Category
SELECT Category,
       COUNT(*) AS Total_Orders
FROM orders
GROUP BY Category;

-- 9. Top Customers by Sales
SELECT CustomerID,
       COUNT(OrderID) AS Total_Orders,
       SUM(Sales) AS Total_Sales
FROM orders
GROUP BY CustomerID
ORDER BY Total_Sales DESC
LIMIT 10;

-- 10. Loss Making Orders
SELECT OrderID,
       CustomerID,
       Category,
       Sales,
       Profit
FROM orders
WHERE Profit < 0
ORDER BY Profit;


-- 11. JOIN Customers and Orders
SELECT
    o.OrderID,
    c.CustomerName,
    c.Region,
    o.Category,
    o.Sales,
    o.Profit
FROM customers c
INNER JOIN orders o
ON c.CustomerID = o.CustomerID;

-- 12. HAVING Clause Example: Total Sales by Category greater than 10000
SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM orders
GROUP BY Category
HAVING SUM(Sales) > 10000;


-- 13. CASE WHEN
SELECT
    OrderID,
    Sales,
    Profit,
    CASE
        WHEN Profit < 0 THEN 'Loss'
        WHEN Profit BETWEEN 0 AND 500 THEN 'Average'
        ELSE 'High Profit'
    END AS Profit_Status
FROM orders;

-- 14. Sub query
SELECT *
FROM orders
WHERE Sales >
(
    SELECT AVG(Sales)
    FROM orders
);

-- 15. CTE
WITH CategorySales AS
(
    SELECT
        Category,
        SUM(Sales) AS TotalSales
    FROM orders
    GROUP BY Category
)

SELECT *
FROM CategorySales
ORDER BY TotalSales DESC;


-- 16. Window Function (RANK)
SELECT
    OrderID,
    Category,
    Sales,
    RANK() OVER(
        ORDER BY Sales DESC
    ) AS SalesRank
FROM orders;


-- 17. ROW_NUMBER()
SELECT
    OrderID,
    Sales,
    ROW_NUMBER() OVER(
        ORDER BY Sales DESC
    ) AS RowNum
FROM orders;


-- 18. DENSE_RANK()
SELECT
    OrderID,
    Sales,
    DENSE_RANK() OVER(
        ORDER BY Sales DESC
    ) AS DenseRank
FROM orders;