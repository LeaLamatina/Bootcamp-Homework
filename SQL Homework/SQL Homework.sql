# 1A - first and last names of all actors
SELECT first_name, last_name
FROM actor;

# 1B - single column first and last name
SELECT CONCAT(first_name, " ", last_name) AS 'Actor Name'
FROM actor;

# 2A - ID number, first name, and last name of all Actors with the first name "Joe."
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'Joe';

# 2B All actors whose last name contain the letters GEN
SELECT first_name, last_name
FROM actor
WHERE last_name
LIKE '%GEN%';

# 2C - All actors whose last names contain the letters LI
SELECT last_name, first_name
FROM actor
WHERE last_name
LIKE '%LI%';

# 2D country_id and country columns of the following countries: Afghanistan, Bangladesh, and China
SELECT country_id, country
FROM country
WHERE country IN(
	'Afghanistan', 
    'Bangladesh', 
    'China'
    );
    
# 3A - Create a column in the table actor named description and use the data type BLOB
ALTER TABLE actor
ADD description BLOB;

# 3B - Delete the description column
ALTER TABLE actor
DROP COLUMN description;

# 4A - List the last names of actors, as well as how many actors have that last name
SELECT last_name, count(last_name) AS 'Name Count'
FROM actor
GROUP BY last_name;

# 4B - List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
SELECT last_name, count(last_name) AS 'Name Count'
FROM actor
GROUP BY last_name
HAVING count(last_name) > 1;

# 4C - The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
UPDATE actor
SET first_name = "HARPO"
WHERE actor_id = 172;

# 4D - In a single query if the first name of the actor is currently HARPO, change it to GROUCHO.
UPDATE actor
SET first_name = 'GROUCHO'
WHERE first_name = 'HARPO';

# 5A - You cannot locate the schema of the address table. Which query would you use to re-create it?
SHOW CREATE TABLE address;

# 6A - Display the first and last names, as well as the address, of each staff member
SELECT first_name, last_name, address
FROM staff
JOIN address
ON staff.address_id=address.address_id;

# 6B - Use JOIN to display the total amount rung up by each staff member in August of 2005
SELECT first_name, last_name, sum(amount)
FROM staff
JOIN payment
ON staff.staff_id=payment.staff_id
WHERE payment_date 
BETWEEN '2005-08-01 00:00:00' and '2005-08-31 23:59:59';

# 6C - List each film and the number of actors who are listed for that film
SELECT title, count(actor_id) AS 'Number of Actors'
FROM film_actor
JOIN film
ON film_actor.film_id=film.film_id
GROUP BY title;

# 6D - Total copies of Hunchback Impossible
SELECT count(film_id) AS 'Copies of Hunchback Impossible'
FROM inventory
WHERE film_id IN(
	SELECT film_id
	FROM film
	WHERE title = 'Hunchback Impossible'
    );

# 6E - List the total paid by each customer alphabetically by last name:
SELECT CONCAT(c.first_name, " ", c.last_name) AS 'Customer Name', sum(p.amount) AS 'Total Paid'
FROM customer c
JOIN payment p ON c.customer_id=p.customer_id
group by p.customer_id
ORDER BY last_name;

# 7A - Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
SELECT title
FROM film
WHERE title
LIKE 'K%' or 'Q%' IN(
	SELECT language_id
    FROM language
    WHERE name='English'        
);

# 7B - All actors in Alone Trip
SELECT first_name, last_name
FROM actor
WHERE actor_id IN(
	SELECT actor_id
	FROM film_actor
	WHERE film_id IN(
		SELECT film_id
		FROM film
		WHERE title='Alone Trip')
);

# 7C - Names and email addresses of all Canadian customers.  Use joins to retrieve this information.
SELECT first_name, last_name, email
FROM customer
LEFT JOIN address ON customer.address_id=address.address_id
LEFT JOIN city ON address.city_id=city.city_id
LEFT JOIN country ON city.country_id=country.country_id
WHERE country='Canada';

# 7D - Identify all movies categorized as family films.
SELECT title
FROM film
WHERE film_id IN(
	SELECT film_id
    FROM film_category
	WHERE category_id IN(
		SELECT category_id
        FROM category 
		WHERE `name`='Family')
);

# 7E - Display the most frequently rented movies in descending order
SELECT f.title, count(r.inventory_id) as 'Rental Count'
FROM film f
INNER JOIN inventory i ON f.film_id=i.film_id
INNER JOIN rental r ON i.inventory_id=r.inventory_id
GROUP BY f.title
ORDER BY 2 DESC;

# 7F - Write a query to display how much business, in dollars, each store brought in.
SELECT 'Store 1', concat('$', format(sum(amount), 2)) AS 'Total Purchases'
FROM payment
WHERE staff_id=1
UNION
SELECT 'Store 2', concat('$', format(sum(amount), 2)) AS 'Total Purchases'
FROM payment
WHERE staff_id=2;

# 7G - Write a query to display for each store its store ID, city, and country.
SELECT store.store_id, city.city, country.country
FROM store
JOIN address ON store.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id;

# 7H - List the top five genres in gross revenue in descending order
SELECT c.name , concat('$', format(sum(p.amount), 2)) AS 'Total Revenue'
FROM payment p
JOIN rental r ON p.rental_id=r.rental_id
JOIN inventory i ON r.inventory_id=i.inventory_id
JOIN film_category ON i.film_id=film_category.film_id
JOIN category c ON film_category.category_id=c.category_id
GROUP BY c.name
ORDER BY 2 DESC;

# 8A - Create view of 7H
CREATE VIEW Top_5_Genres AS
SELECT c.name , concat('$', format(sum(p.amount), 2)) AS 'Total Revenue'
FROM payment p
JOIN rental r ON p.rental_id=r.rental_id
JOIN inventory i ON r.inventory_id=i.inventory_id
JOIN film_category ON i.film_id=film_category.film_id
JOIN category c ON film_category.category_id=c.category_id
GROUP BY c.name
ORDER BY 2 DESC;

# 8B - How would you display the view that you created in 8a?
SELECT * FROM Top_5_Genres;

# 8C - Delete top_five_genres
DROP VIEW Top_5_Genres;