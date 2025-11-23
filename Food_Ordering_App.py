import time
import sys

# --- Application Configuration ---
# Define the restaurant menu using nested dictionaries
MENU = {
    "Pizzas": {
        "1": {"name": "Margherita", "price": 12.50},
        "2": {"name": "Pepperoni Feast", "price": 15.75},
        "3": {"name": "Veggie Delight", "price": 13.00}
    },
    "Sides": {
        "4": {"name": "Garlic Bread", "price": 4.99},
        "5": {"name": "Fries", "price": 3.50}
    },
    "Drinks": {
        "6": {"name": "Cola", "price": 2.00},
        "7": {"name": "Orange Juice", "price": 2.50},
        "8": {"name": "Water", "price": 1.50}
    }
}

# Define tax rate and delivery fee
TAX_RATE = 0.08  # 8% tax
DELIVERY_FEE = 5.00

# --- Utility Functions ---

def print_separator(char="=", length=50):
    """Prints a clean separator line."""
    print(char * length)

def get_menu_item_by_code(code):
    """Finds a menu item object based on its unique code."""
    for category in MENU.values():
        if code in category:
            return category[code]
    return None

def display_menu():
    """Displays the entire menu clearly categorized."""
    print_separator("=")
    print("        Welcome to Python Pizzeria!        ")
    print_separator("=")
    
    # Create a mapping of code -> item details for easy lookup
    all_items = {} 
    
    for category_name, category_items in MENU.items():
        print(f"\n--- {category_name} ---")
        for code, item in category_items.items():
            print(f"[{code}] {item['name']:<20} ${item['price']:.2f}")
            all_items[code] = item
            
    print_separator("-")
    print("[C] Checkout | [X] Exit")
    print_separator("=")
    return all_items # Return the flat list of items for the ordering process

# --- Core Application Logic ---

def take_order(cart):
    """Handles adding items to the user's cart."""
    while True:
        all_items = display_menu()
        
        user_input = input("\nEnter item code (1-8), [C]heckout, or [X] Exit: ").strip().upper()
        
        if user_input == 'X':
            print("\nThank you for visiting! Goodbye.")
            sys.exit()
        
        if user_input == 'C':
            if not cart:
                print("Your cart is empty. Please add some items first.")
                # Continue to show menu until an item is added or user exits
                continue
            return # Exit the function and proceed to checkout
        
        item_details = get_menu_item_by_code(user_input)
        
        if item_details:
            while True:
                try:
                    quantity_input = input(f"How many '{item_details['name']}' would you like? (Enter a number): ").strip()
                    quantity = int(quantity_input)
                    if quantity <= 0:
                        print("Quantity must be a positive number.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Add item and its details to the cart
            for _ in range(quantity):
                cart.append(item_details)
            print(f"-> Added {quantity} x {item_details['name']} to your cart.")
        else:
            print("Invalid code. Please try again.")

def calculate_total(cart):
    """Calculates the subtotal, tax, and final grand total."""
    subtotal = sum(item['price'] for item in cart)
    tax_amount = subtotal * TAX_RATE
    grand_total = subtotal + tax_amount + DELIVERY_FEE
    
    return subtotal, tax_amount, grand_total

def checkout(cart):
    """Finalizes the order, displays the receipt, and processes payment."""
    if not cart:
        print("\nYour cart is empty. No order to process.")
        return

    subtotal, tax_amount, grand_total = calculate_total(cart)

    print_separator("=")
    print("              -- Your Receipt --             ")
    print_separator("-")
    
    # Group items for cleaner display (e.g., 2x Margherita)
    item_counts = {}
    for item in cart:
        name = item['name']
        item_counts[name] = item_counts.get(name, 0) + 1

    # Display ordered items
    for name, count in item_counts.items():
        # Find the price of one item (assuming all items with the same name have the same price)
        item_price = next(item['price'] for item in cart if item['name'] == name)
        line_total = item_price * count
        print(f"{count} x {name:<20} @ ${item_price:.2f} = ${line_total:.2f}")

    print_separator("-")
    print(f"Subtotal: {'':<28} ${subtotal:.2f}")
    print(f"Tax ({int(TAX_RATE * 100)}%): {'':<28} ${tax_amount:.2f}")
    print(f"Delivery Fee: {'':<28} ${DELIVERY_FEE:.2f}")
    print_separator("-")
    print(f"GRAND TOTAL: {'':<26} ${grand_total:.2f}")
    print_separator("=")
    
    # Simulate payment processing
    print("\nProcessing payment...")
    time.sleep(2) # Pause for 2 seconds to simulate processing
    
    # Simple payment confirmation loop
    while True:
        confirm = input(f"Confirm payment of ${grand_total:.2f}? (Y/N): ").strip().upper()
        if confirm == 'Y':
            print("\n*** Payment successful! ***")
            print("Your order is being prepared and will be delivered shortly.")
            print("Thank you for choosing Python Pizzeria!")
            break
        elif confirm == 'N':
            print("Order cancelled. Thank you, come again!")
            break
        else:
            print("Invalid input. Please enter Y or N.")

def run_app():
    """Main function to run the food ordering application."""
    # The cart will store a list of selected menu item objects
    customer_cart = []
    
    # 1. Take the order (loops until user selects 'C'heckout or 'X' Exit)
    take_order(customer_cart)
    
    # 2. Checkout the order
    if customer_cart:
        checkout(customer_cart)

# Start the application
if __name__ == "__main__":
    try:
        run_app()
    except KeyboardInterrupt:
        print("\nApplication stopped by user. Goodbye!")
    finally:
        sys.exit(0)
