#Order Management System

import pandas as pd # Use pandas for efficient data handling.
from datetime import datetime
import uuid # Used for Random id generaition

class OrderManagement:
    def __init__(self):  #most imp
        self.orders = pd.DataFrame(columns=["Order ID", "Customer Name", "Item", "Quantity", "Order Date"])

    def add_order(self):
        customer_name = input("Enter customer name: ")
        item = input("Enter item ordered: ")
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer for quantity.")

        order_id = str(uuid.uuid4())[:8]
        order_date = datetime.now().strftime("%Y-%m-%d")
        new_order = pd.DataFrame([[order_id, customer_name, item, quantity, order_date]],
                                 columns=["Order ID", "Customer Name", "Item", "Quantity", "Order Date"])
        
        self.orders = pd.concat([self.orders, new_order], ignore_index=True)
        print("Order added successfully!")
        print(f"Order ID: {order_id}, Customer: {customer_name}, Item: {item}, Quantity: {quantity}, Date: {order_date}")

    def view_orders(self):
        order_id_to_view = input("Enter the Order ID to view details (leave empty to view all orders): ")

        if order_id_to_view:
            if order_id_to_view in self.orders['Order ID'].values:
                order_details = self.orders[self.orders['Order ID'] == order_id_to_view]
                print("Order details:")
                print(order_details.to_string(index=False))
            else:
                print("No order found.")
        else:
            if not self.orders.empty:
                print("All Orders:")
                print(self.orders.to_string(index=False))
            else:
                print("No orders found.")

    def update_order(self):
        order_id_to_update = input("Enter the Order ID to update: ")
        if order_id_to_update in self.orders['Order ID'].values:
            print("Order found. Please provide updated information.")
            new_customer_name = input("Enter updated customer name: ")
            new_item = input("Enter updated item: ")
            while True:
                try:
                    new_quantity = int(input("Enter updated quantity: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid integer for quantity.")

            self.orders.loc[self.orders['Order ID'] == order_id_to_update, 'Customer Name'] = new_customer_name
            self.orders.loc[self.orders['Order ID'] == order_id_to_update, 'Item'] = new_item
            self.orders.loc[self.orders['Order ID'] == order_id_to_update, 'Quantity'] = new_quantity

            print("Order updated successfully!")
        else:
            print("Order not found.")

    def save_to_excel(self, filepath='/content/Data Base.xlsx'): #don't forgot to add the xlsx file named with this name mentioned here
        self.orders.to_excel(filepath, index=False)
        print(f"Orders saved to {filepath}")

order_system = OrderManagement()

while True:
    print("\n1. Add Order\n2. View Orders\n3. Update Order\n4. Save to Excel\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        order_system.add_order()
    elif choice == '2':
        order_system.view_orders()
    elif choice == '3':
        order_system.update_order()
    elif choice == '4':
        order_system.save_to_excel()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

# Here the Code Ends , Enjoy the backend Design.