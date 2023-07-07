## To Run
Download all files and run main.py

# Seeam Khan

## Application 
The website displays products being sold in several categories. A user visiting the web store can search for products or display all items in a certain category. The website displays the available quantity and price for each product.

Only a logged in user can add products to a shopping cart and then checkout to complete a purchase and buy the products. To "buy" a product means to reduce the quantity from that product with the quantity that was "bought". 

A logged in user's shopping cart can be viewed, edited, checked out or deleted. A logged in user can also see their order history which should include the list of items purchased and total cost of the order.

## Implementation
- Python Flask will be used for all the server side scripting.
- The cart is implemented with Session variables.
- Check user input: do not allow me to buy -2 boxes of detergent or, 100 boxes if you only have 1 in stock.
- Keep minimum information about customers: username and password, first and last name. We are not interested in addresses at this point.

## Description

This project showcases a comprehensive e-commerce store with various implemented features. At the bare minimum level, users can browse through a collection of 10 products across 3 categories, facilitated by a basic web interface. The database schema and population scripts are provided in the `store_schema.sql` file. Moving up to the base level, users gain the ability to search for specific items by name, login with an existing account (such as the sample user "testuser" with password "testpass"), and manage their cart by adding, editing, checking out, or deleting items. The cart is stored as a session variable, and the database is updated accordingly upon checkout. To achieve the medium level, new users can sign up, logged-in users can view their order history, and the user interface becomes more user-friendly with intuitive navigation and user-friendly error messages. Furthermore, product listings are enhanced with visuals in the form of pictures. Lastly, at the prime level, client-side validation is implemented using JavaScript to ensure input form data is valid. Logged-in users gain the ability to sort their orders by date and search for products within their previous orders. The website is polished with a professional look, incorporating a logo, detailed product descriptions, and other elements that inspire a professional shopping experience.
