# any client need to order
#client to be dependent 4class such as:
    # 1.Authenticate,
    # 2.Inventory,
    # 3.Payment,
    # 4.orderfulfillment

# The customer talks to the host, not to the chef, cashier, stock, and waiter separately.
# The customer talks to the host, not to the chef, cashier, stock, and waiter separately.

# Create Order Request that considering all data user needed.
class Authenticate:
    def login(self, user, pwd):
        print(f"Authenticating {user}...")
        return True

class Inventory:
    def check_ingredients(self, order_items):
        print(f"Checking inventory for {order_items}...")
        return True  # همه مواد موجود است

class Payment:
    def pay(self, amount):
        print(f"Processing payment of ${amount}...")
        return True

class OrderFulfillment:
    def prepare_order(self, order_items):
        print(f"Preparing {order_items} in kitchen...")
        print("Order is ready for pickup/delivery.")


class RestaurantFacade:
    def __init__(self):
        self.auth = Authenticate()
        self.inv = Inventory()
        self.payment = Payment()
        self.fulfill = OrderFulfillment()

    def place_order(self, username, password, items, amount):
        print("\n--- Starting order via Facade ---")

        # 1. Authenticate
        if not self.auth.login(username, password):
            return "Authentication failed"

        # 2. Check Inventory
        if not self.inv.check_ingredients(items):
            return "Out of stock"

        # 3. Payment
        if not self.payment.pay(amount):
            return "Payment failed"

        # 4. Fulfillment
        self.fulfill.prepare_order(items)

        return "Order completed successfully!"


# Client code - فقط با Facade کار می‌کند
restaurant = RestaurantFacade()

result = restaurant.place_order(
    username="ali",
    password="123",
    items=["Pizza", "Salad"],
    amount=25
)

print(result)
