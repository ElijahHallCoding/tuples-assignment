# Sample order data
orders = [
    ("Elicia", "Laptop", 1),
    ("Bobby", "Camera", 2),
    ("Elijah", "Smartphone", 3),
    ("Shanteek", "Tablet", 1)
]

# Function to process and display orders
def process_orders(order_list):
    # Loop through each order in the list
    for order in order_list:
        # Unpack the tuple into separate variables
        customer_name, product, quantity = order
        
        # Format and print the order details
        print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")

# Call the function to display the orders
process_orders(orders)