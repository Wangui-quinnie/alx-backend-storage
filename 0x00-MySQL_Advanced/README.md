MySQL advanced
Creating tables with constraints in MySQL involves specifying rules and conditions that the data in the table must adhere to. Constraints help enforce data integrity and ensure that the data meets certain criteria.

Here's how to create a table with constraints in MySQL:

Primary Key Constraint: Specifies a column or set of columns that uniquely identifies each row in the table. It ensures that the values in the specified column(s) are unique and not null.

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    emp_dept VARCHAR(100)
);
Foreign Key Constraint: Establishes a relationship between two tables by referencing the primary key of one table as a foreign key in another table. It ensures referential integrity.

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    product_id INT,
    order_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
Unique Constraint: Ensures that the values in the specified column(s) are unique across all rows in the table.

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE
);
Check Constraint: Specifies a condition that must be met for the data in a column. It ensures that only valid data is inserted into the table.

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    unit_price DECIMAL(10, 2),
    quantity INT,
    CHECK (unit_price > 0),
    CHECK (quantity >= 0)
);
To optimize queries, you can add indexes to columns that are frequently used in WHERE clauses or JOIN operations. Indexes help speed up data retrieval by creating a sorted data structure that allows for faster lookup.

Here's how to add indexes to columns in MySQL:

Single Column Index:

CREATE INDEX idx_lastname ON employees (last_name);
Composite Index (Index on Multiple Columns):

CREATE INDEX idx_name_dept ON employees (emp_name, emp_dept);
Stored procedures and functions in MySQL allow you to encapsulate a sequence of SQL statements into a reusable routine that can be called and executed from within MySQL.

Here's how to create stored procedures and functions in MySQL:

Stored Procedure:

DELIMITER //
CREATE PROCEDURE get_employee(IN emp_id INT)
BEGIN
    SELECT * FROM employees WHERE employee_id = emp_id;
END //
DELIMITER ;
Function:

CREATE FUNCTION calculate_tax(amount DECIMAL(10, 2)) RETURNS DECIMAL(10, 2)
BEGIN
    DECLARE tax DECIMAL(10, 2);
    SET tax = amount * 0.1;
    RETURN tax;
END;
Views in MySQL are virtual tables that are based on the result of a SELECT query. They provide a way to simplify complex queries and encapsulate them into a reusable object.

Here's how to create a view in MySQL:

CREATE VIEW high_salary_employees AS
SELECT * FROM employees WHERE salary > 50000;
Triggers in MySQL are stored programs that are automatically executed in response to certain events on a table, such as INSERT, UPDATE, or DELETE operations.

Here's how to create a trigger in MySQL:

CREATE TRIGGER before_insert_employee
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    SET NEW.created_at = NOW();
END;
These are some of the key concepts and techniques for working with MySQL databases, which can help optimize performance, maintain data integrity, and simplify database operations.
