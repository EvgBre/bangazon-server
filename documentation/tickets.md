# Ticket Descriptions - E-commerce Site Project

The following ticket descriptions have been created based on the discussions held with the client regarding the development of an e-commerce site. These tickets outline specific functionalities and requirements for the project and serve as a guide for the engineers working on the implementation.

**Ticket Descriptions - E-commerce Site Project**

These tickets have been written to capture the key features and functionalities discussed during the client meetings. Each ticket provides a clear description of the desired behavior, including the given conditions, expected actions, and resulting outcomes. The potential implementation ideas offer suggestions for the technical approach that can be considered.

These tickets will serve as a reference for the engineers, ensuring accurate implementation of the discussed features. The product manager will work closely with the engineering team to prioritize and track the progress of each ticket.

Please review these ticket descriptions to gain a comprehensive understanding of the project's scope and objectives as conveyed by the client.

## Title: Customer should be able to view products that a seller is selling

- **Given** that a seller has a store with products available
- **When** a customer is viewing a seller's store
- **Then** they will see all the products that the seller has available

### Potential Implementation Ideas

- Potentially create a new endpoint that includes product information with the seller
- Potentially refactor the existing seller endpoint to include product information
- Potentially create a query string parameter `?include=products` to optionally include product information with the seller

## Title: Allow a user to register for Bangazon

- **Given** that a user wants to buy or sell products and does not already have an account
- **When** they navigate to the app
- **Then** they are given the option to register a new user

## Title: Customers can view shopping cart

- **Given** a user has products in their shopping cart
- **When** viewing their cart
- **Then** they should see the product name and price of each product they are ordering
- **And** they should be able to see the total amount of their order

## Title: Allow sellers to see orders with their products on them

- **Given** a seller has sold items
- **When** a seller navigates to the order history page
- **Then** there should be a section dedicated to orders with their products
- **And** they should be able to see the customers that placed each order

### API Routes

- `api/order/history/seller` should return the orders where the logged-in user has a product on the order

## Title: User Can View Product Detail

- **Given** the user is viewing any page that contains a hyperlink for a product
- **When** the user clicks on the product hyperlink
- **Then** the user will be shown the product detail page containing the title, description, quantity available, price per unit, and a button labeled *Add to Cart*

## Title: Customer should be able to view product information when viewing order details

- **Given** a customer has purchased items
- **When** the customer views their order history
- **Then** product details should be viewable with each order

## Title: Customer should be able to view their completed orders

- **Given** a customer has purchased items
- **When** the customer navigates to the Orders view
- **Then** they should see a list of their completed orders

### Potential Implementation Ideas:

- Potentially create a new endpoint that includes only completed Orders
- Potentially create a query string parameter `?completed=true` to optionally include completed orders

## Title: Customer can search for products

- **Given** sellers have items to purchase
- **When** the user clicks on the search input field in the navigation bar
- **And** the user types the name of a product
- **When** the enter key is pressed
- **Then** products matching the keyword will be shown on the page

## Title: Customer should be able to view order history

- **When** a user navigates to the order history page
- **Then** order details should be displayed
- **And** a user should be able to see the seller's info for a given order

### Order API Routes:

- `api/orders` should return the orders for the logged-in user
- `api/orders/sellers` should return the orders for the logged-in user, along with the seller's info for each product on each order

## Title: Seller should have a dashboard

- **Given** a seller has sold items
- **When** they navigate to the seller area
- **Then** they should arrive at a dashboard

### Dashboard data to display:
- Total Sales
    - Total this month
    - Average per item
- Total Inventory by Category
- Orders that require shipping

## Title: Customer can view latest products on home page

- **Given** a user visits the home page of Bangazon
- **When** the page renders
- **Then** the last 20 products that have been added to the system will be displayed as hyperlinks to their respective detail pages

## Title: Allow a user to place an order

- **Given** the user is authenticated
- **And** the user is viewing their cart
- **When** the user clicks the *Order* button
- **Then** the user should be presented with a view that allows them to select a payment type for the order

- **Given** the user selects a payment option
- **When** the user clicks the *Done* button
- **Then** the payment type must be added to the order
- **And** the user will be presented with a confirmation/thank you screen

## Title: Customer can click on a seller's name on a product page to view all products sold by that seller

- **Given** a customer is on a product detail page
- **When** clicking on a seller's name
- **Then** they should be taken to a Seller's store

## Title: Search for Seller by text

- **Given** A user is logged in
- **Then** they should be able to search for a seller

- If the query string parameter of `q` is provided when querying the list of customers, then any customer that has a property value that matches the pattern should be returned.
- If `/customers?q=mic` is requested, then any customer whose first name is Michelle, or Michael, or Domicio should be returned. Any customer whose last name is Michaelangelo, Omici, or Dibromic should be returned. Every property of the customer object should be checked for a match.

## Title: Customer can add products to a cart

- **Given** the customer is on a product detail page
- **When** clicking on an add to cart button
- **Then** the product should be added to their cart

## Title: Seller should be able to view their past sales

- **Given** a seller has sold items
- **When** the seller navigates to the Orders view
- **Then** they should see a list of their completed orders

## Title: Customer can view their profile information

- **Given** a customer has registered an account
- **When** they click on their username
- **Then** they can view their profile information.

## Title: Customer can delete an item from their cart

- **Given** that a customer has an item in their cart
- **When** they click the *Delete* button
- **Then** the product is removed from their cart

## Title: User Can View All Product Categories

- **Given** a user is viewing any page on the Bangazon site
- **When** the user clicks on the *Product Categories* hyperlink
- **Then** the user will see a view containing a list of all product categories
- **And** next to the category name, the number of products in that category will be displayed
- **And** the first three products in the category will be displayed beneath each category, which are hyperlinks to the product detail

### Sample

```
Electronics (15)
    Dryer
    HD Television
    Sony Walkman

Sporting Goods (7)
    Football
    Ice skates
    Basketball hoop
```

## Title: Customers can choose one of their payment types when purchasing their shopping cart

- **Given** a customer with a shopping cart with products in it
- **When** placing their order
- **Then** they should be asked for a payment type
- **And** they should select a payment type that they have defined
- **Given** a customer with a shopping cart with products in it
- **And** the customer does not have a payment method defined
- **When** placing their order
- **Then** they should be asked to define a payment method
