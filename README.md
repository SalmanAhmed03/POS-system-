Kivy POS System
This repository contains a Point of Sale (POS) system built using the Kivy framework for Python. It includes functionalities for user authentication, managing products, and CRUD operations using MySQL as the database.

Features
User Authentication:

Allows users to sign in with predefined credentials (currently supports 'admin'/'admin' login).
Operator Window:

Provides a simple interface for adding products to a cart-like system. Each product addition updates a receipt preview.
Admin Panel:

Manages users and products through CRUD operations:
Add, update, and remove users.
Add, update, and remove products with details like name, stock, and purchase history.
Dependencies
Python: Developed using Python 3.8.
Kivy: UI framework for Python applications.
MySQL Connector: Python interface for MySQL databases.
Setup
Clone the repository:

perl
Copy code
git clone https://github.com/yourusername/kivy-pos-system.git
cd kivy-pos-system
Install dependencies:

Copy code
pip install kivy mysql-connector-python
Database setup:

Ensure MySQL is installed and running.
Create a database named pos.
Import pos.sql provided in the repository to set up tables.
Usage
Run the application:

css
Copy code
python main.py
Sign in:

Use 'admin' as both the username and password to access the admin panel.
Alternatively, log in with other credentials (currently not implemented in the provided code).
Admin Panel:

Manage users: Add, update, or remove user details.
Manage products: Add, update, or remove product information.
Operator Window:

Enter product codes to add them to a cart-like interface.
View a live preview of the receipt with each product addition.
Screenshots

<img width="598" alt="Screenshot 2024-06-13 065023" src="https://github.com/SalmanAhmed03/POS-system-/assets/124187700/9f5d9543-b511-4850-aa04-be9faac2f45f">

<img width="598" alt="Screenshot 2024-06-13 065049" src="https://github.com/SalmanAhmed03/POS-system-/assets/124187700/608c9e87-0419-48f4-871d-ff6d86c6fe44">

<img width="602" alt="Screenshot 2024-06-13 065206" src="https://github.com/SalmanAhmed03/POS-system-/assets/124187700/1b931ba0-b7a6-4313-b9f9-03ecc0a8e75b">



License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to Kivy for providing an open-source Python framework.
Inspiration and initial guidance from online tutorials and documentation
