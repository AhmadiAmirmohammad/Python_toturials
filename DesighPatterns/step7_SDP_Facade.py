# Facade pattern
# The facade pattern in structural design pattern that provides a simplified interface
# to a complex system, encapsulating the complexities of multiple subsystems into a
# unified interface for clients.

# Say that we have as eCommerce application that allows users to submit orders.
# Here are the steps Involved.

# 5step exist in process order:
#    1. Authenticate
#    2. Authenticate
#    2. Authenticate
#    2. Authenticate
#    2. Authenticate

# Create Order Request that considering all data user needed.
class OrderRequest:
    def __init__(self, order):
        self.name = "danny"
        self.card_number = "1234"
        self.amount = 20.99  # total amount
        self.address = "123 springfield way, texas"
        # item IDs user wants to order
        self.item_ids = ["123", "423", "555", "989"]


class Authenticator:  # for authenticate users
    def authenticate(self) -> bool:
        return True


class Inventory:
    def check_inventory(self, item_id: str) -> bool:
        return True  # just return true to keep the example simple

    def reduce_inventory(self, item_id: str, amount: int):
        # In real app this would reduce the amount in a database
        print(f"Reducing inventory of {item_id} by {amount}")


class Payment:
    def __init__(self, name: str, card_number: str, amount: float):
        self._name = name
        self._card_number = card_number
        self._amount = amount

    def pay(self):
        print(f"changing card with name {self._name}")


class OrderFunFillment:  # for add order to database
    def __init__(self, inventory: Inventory):
        self._inventory = inventory

    def fullfill(self, name: str, address: str, items: list[str]):
        print("Inserting order into database")
        for item in items:
            self._inventory.reduce_inventory(item, 1)


# order request contains info that user has submitted when requesting to make as order
order_req = OrderRequest()
auth = Authenticator()
inventory = Inventory()

for item_id in order_req.item_ids:
    inventory.check_inventory(item_id)

payment = Payment(order_req.name, order_req.card_number, order_req.amount)
payment.pay()

order_fulfillment = OrderFunFillment(inventory)
order_fulfillment.fullfill(order_req.name, order_req.address, order_req.item_ids)
