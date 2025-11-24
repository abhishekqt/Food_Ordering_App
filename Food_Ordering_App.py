import tkinter as tk
from tkinter import messagebox

# Sample menu
menu = {
    "Burger(Price = 5.99)": 5.99,
    "Pizza(Price = 8.99)": 8.99,
    "Salad(Price = 4.49)": 4.49,
    "Fries(Price = 2.99)": 2.99,
    "Soda(Price = 1.99)": 1.99
}

# Cart as a dictionary for item counts
cart = {}

def add_to_cart():
    selected = menu_listbox.get(tk.ACTIVE)
    if selected:
        if selected in cart:
            cart[selected] += 1
        else:
            cart[selected] = 1
        update_cart_display()
        messagebox.showinfo("Added", f"Added {selected} to cart.")

def update_cart_display():
    cart_text.delete(1.0, tk.END)
    total = 0
    for item, qty in cart.items():
        price = menu[item] * qty
        cart_text.insert(tk.END, f"{item} x{qty} - ${price:.2f}\n")
        total += price
    cart_text.insert(tk.END, f"\nTotal: ${total:.2f}")

def place_order():
    if not cart:
        messagebox.showwarning("Empty Cart", "Your cart is empty!")
        return
    confirm = messagebox.askyesno("Confirm Order", "Place the order?")
    if confirm:
        messagebox.showinfo("Order Placed", "Thank you! Your order has been placed.")
        cart.clear()
        update_cart_display()

# Create main window
root = tk.Tk()
root.title("Food Ordering App")
root.geometry("400x400")

# Menu section
tk.Label(root, text="Menu").pack()
menu_listbox = tk.Listbox(root, height=5)
for item in menu:
    menu_listbox.insert(tk.END, item)
menu_listbox.pack()

tk.Button(root, text="Add to Cart", command=add_to_cart).pack()

# Cart section
tk.Label(root, text="Your Cart").pack()
cart_text = tk.Text(root, height=10, width=40)
cart_text.pack()

tk.Button(root, text="Place Order", command=place_order).pack()

# Run the app
root.mainloop()
