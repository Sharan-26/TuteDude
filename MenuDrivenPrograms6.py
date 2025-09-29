# E-Commerce Platform Prototype
class ECommercePlatform:
    def __init__(self,products,carts,orders):
        self.products =products
        self.carts =carts
        self.orders =orders
        
    def add_product(self,product_id,product_name,price):
        self.products[product_id] = {"name": product_name, "price": price} # Add product to catalog
        print(f"Product {product_name} added with ID {product_id} at price ${price:.2f}")
        
    def view_products(self):
        print("Available Products:")
        for pid, details in self.products.items(): # Iterate through products
            print(f"ID: {pid}, Name: {details['name']}, Price: ${details['price']:.2f}")# Display product details
    
    def add_to_cart(self,user_id,product_id,quantity):
        if user_id not in self.carts: # Initialize cart for user if not exists
            self.carts[user_id] = {} # Dictionary to hold product_id and quantity
        if product_id in self.products: # Check if product exists
            if product_id in self.carts[user_id]: # If product already in cart, update quantity
                self.carts[user_id][product_id] += quantity # Update quantity
            else:
                self.carts[user_id][product_id] = quantity # Add new product to cart
            print(f"Added {quantity} of {self.products[product_id]['name']} to cart for user {user_id}.") # Confirm addition
        else:
            print("Product not found!")
        
    def view_cart(self,user_id):
        if user_id in self.carts and self.carts[user_id]: # Check if cart exists and is not empty
            print(f"Cart for user {user_id}:") # Display cart contents
            total = 0
            for pid, qty in self.carts[user_id].items(): # Iterate through cart items
                product = self.products[pid] # Get product details
                subtotal = product['price'] * qty # Calculate subtotal
                total += subtotal # Update total
                print(f"{product['name']} (x{qty}): ${subtotal:.2f}") # Display item details
            print(f"Total: ${total:.2f}") # Display total amount
        else:
            print("Cart is empty.")
            
    def place_order(self,user_id):
        if user_id in self.carts and self.carts[user_id]: # Check if cart exists and is not empty
            order_total = 0
            order_details = []
            for pid, qty in self.carts[user_id].items(): # Iterate through cart items
                product = self.products[pid] # Get product details
                subtotal = product['price'] * qty # Calculate subtotal
                order_total += subtotal # Update order total
                order_details.append((product['name'], qty, subtotal)) # Collect order details
            order_id = len(self.orders) + 1 # Generate order ID
            self.orders[order_id] = {"user_id": user_id, "details": order_details, "total": order_total} # Store order
            self.carts[user_id] = {} # Clear cart after placing order
            print(f"Order {order_id} placed for user {user_id}. Total: ${order_total:.2f}") # Confirm order placement
        else:
            print("Cart is empty. Cannot place order.")
            
# Example usage
platform = ECommercePlatform(products={}, carts={}, orders={})
platform.add_product(1, "Laptop", 999.99)
platform.add_product(2, "Smartphone", 499.99)
platform.view_products()
platform.add_to_cart("user1", 1, 1)
platform.add_to_cart("user1", 2, 2)
platform.view_cart("user1")
platform.place_order("user1")
platform.view_cart("user1")  # Should show empty cart after order placement
platform.place_order("user1")  # Should indicate cart is empty
