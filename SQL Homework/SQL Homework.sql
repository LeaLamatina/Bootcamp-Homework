# 1A - first and last names of all actors
SELECT first_name, last_name
FROM actor;

# 1B - single column first and last name
SELECT CONCAT(first_name, " ", last_name) AS 'Actor Name'
FROM actor;

# 2A - You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe."
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'Joe';

# 2B All actors whose last name contain the letters GEN
SELECT first_name, last_name
FROM actor
WHERE last_name
LIKE '%GEN%';

# 2C - Find all actors whose last names contain the letters LI
SELECT last_name, first_name
FROM actor
WHERE last_name
LIKE '%LI%';

# 2D Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country
FROM country
WHERE country IN(
	'Afghanistan', 
    'Bangladesh', 
    'China'
    );
    
# 3A - You want to keep a description of each actor. You don't think you will be performing queries on a description, 
# so create a column in the table actor named description and use the data type BLOB
# (Make sure to research the type BLOB, as the difference between it and VARCHAR are significant).


# 3B - Delete the description column

# 4A - List the last names of actors, as well as how many actors have that last name
SELECT last_name, count(last_name) AS 'Name Count'
FROM actor
GROUP BY last_name;

# 4B - List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT last_name, count(last_name) AS 'Name Count'
FROM actor
WHERE count(last_name) > 1
GROUP BY last_name;

# 4C - The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
UPDATE actor
SET first_name = "HARPO"
WHERE actor_id = 172;

# 4D - In a single query if the first name of the actor is currently HARPO, change it to GROUCHO.
UPDATE actor
SET first_name = 'GROUCHO'
WHERE first_name = 'HARPO';

# 5A - You cannot locate the schema of the address table. Which query would you use to re-create it?


# 6A - Display the first and last names, as well as the address, of each staff member
SELECT first_name, last_name, address
FROM staff
JOIN address
ON staff.address_id=address.address_id;

# 6B - Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT first_name, last_name, sum(amount)
FROM staff
JOIN payment
ON staff.staff_id=payment.staff_id
WHERE payment_date 
BETWEEN '2005-08-01 00:00:00' and '2005-08-31 23:59:59';

# 6C - List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT title, count(actor_id) AS 'Number of Actors'
FROM film_actor
JOIN film
ON film_actor.film_id=film.film_id
GROUP BY title;

# 6D - How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT count(film_id) AS 'Copies of Hunchback Impossible'
FROM inventory
WHERE film_id IN(
	SELECT film_id
	FROM film
	WHERE title = 'Hunchback Impossible'
    );

# 6E - Using the tables payment and customer and the JOIN command, list the total paid by each customer.
# List the customers alphabetically by last name:
SELECT CONCAT(first_name, " ", last_name) AS 'Customer Name', sum(amount) AS 'Total Paid'
FROM payment
JOIN customer
ON payment.customer_id=customer.customer_id
group by 'Actor Name';
# ^^ groupby only returns a single customer...

# 7A - The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, 
# films starting with the letters K and Q have also soared in popularity.
# Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.

