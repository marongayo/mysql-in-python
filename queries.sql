-- Sample Query 1: Select all orders with their pizzas
SELECT  Orders.order_date, Orders.order_time, Pizza.pizza_name
FROM Orders
LEFT JOIN Pizza ON Orders.order_id = Pizza.order_id;

-- Sample Query 2: List pizzas with their ingredients
SELECT Pizza.pizza_name, PizzaIngredients.ingredients
FROM Pizza
LEFT JOIN PizzaIngredients ON Pizza.pizza_id = PizzaIngredients.pizza_id
LIMIT 5;

-- Sample Query 3: Find orders with a specific pizza category
SELECT Orders.order_id, Orders.order_date, Orders.order_time, Pizza.pizza_name, Pizza.pizza_category
FROM Orders
LEFT JOIN Pizza ON Orders.order_id = Pizza.order_id
WHERE Pizza.pizza_category = 'Vegetarian';

-- Sample Query 4: Calculate the total cost of each order
SELECT Orders.order_id, Orders.order_date, Orders.order_time, SUM(Pizza.unit_price) AS total_cost
FROM Orders
LEFT JOIN Pizza ON Orders.order_id = Pizza.order_id
GROUP BY Orders.order_id;

-- Sample Query 6: List orders with the number of pizzas in each order
SELECT Orders.order_id, Orders.order_date, Orders.order_time, COUNT(Pizza.pizza_id) AS num_pizzas
FROM Orders
LEFT JOIN Pizza ON Orders.order_id = Pizza.order_id
GROUP BY Orders.order_id;
