# Food_Ordering_App


## Overview

The Food Ordering App is a simple graphical desktop application built using Python and Tkinter.
It allows users to browse a menu, add items to a cart, view total cost, and place an order.
This project demonstrates GUI development, event-driven programming, and basic data handling.

The system simulates the workflow of a real-world food ordering interface with an easy-to-use layout.




## Features

   Functional Features:

1. Menu Display:
   Shows available food items with their prices.


2. Add to Cart:
   Users can select an item from the list and add it to the cart.


3. Cart Management:
   Displays selected items,
   Shows quantity,
   Updates total amount automatically.



4. Place Order
   Confirms and completes the order using message boxes.




## Technologies / Tools Used

Python 3

Tkinter (Python GUI Toolkit)

Messagebox module for pop-ups and alerts

Dictionary-based data storage for menu and cart




## Folder Structure (Recommended for GitHub)
<pre>
FoodOrderingApp/
│
├── src/
│   ├── app.py
│
├── README.md
└── statement.md
</pre>



## Steps to Install & Run the Project

1. Install Python

   Ensure Python 3.x is installed.
   Check with:
            python --version

2. Clone the Repository

   git clone <your-repository-link>
   cd FoodOrderingApp

3. Run the Application

   python src/app.py

   The GUI window will open automatically.




## Instructions for Testing

   You can test the app through the following steps:

1. Open the app
   Verify that menu items appear in the listbox.


2. Select a menu item and click ‘Add to Cart’

   A message box should confirm the addition

   The cart should update with the selected item and quantity


3. Add multiple items

   Quantities should increase

   Total cost should update correctly


4. Click ‘Place Order’

   If the cart is empty → warning message appears

   If items exist → confirmation dialog appears

   After confirmation → success message appears and cart resets


5. Check GUI responsiveness
   Ensure all buttons and text areas behave correctly.




## Future Enhancements

Add a database to store orders.

Add a login/signup module.

Include images for menu items.

Add quantity selector instead of multiple clicks.

Implement billing receipt download.




## Project Status

Fully functional basic prototype
Can be extended with advanced modules (Billing, Database, User Management)




## License

This project is free to use for academic purposes.
