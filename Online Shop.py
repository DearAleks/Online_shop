import datetime
class Client:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.transactions = []
    
    def place_order(self, transactions: list):
        order_total_cost = 0
        bought_items = []
        for item, quantity in transactions:
            if item.stock >= quantity:
                bought_items.append(item.name)
                transaction = Transaction(self, item, quantity)
                item.update_stock(-quantity)
                self.transactions.append(transaction)
                order_total_cost += item.price * quantity
            else:
                print(f'The amount of {item.name} exceeds the stock')
        print(f"{transaction.time_stamp}, {self.name}; total cost: {order_total_cost} EUR; items bought: {bought_items}")
        return order_total_cost

    def view_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def total_cost_of_all_transactions(self):
        total = 0
        for transaction in self.transactions:
            total += transaction.item.price * transaction.quantity
        return total

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):
        self.stock += quantity

class Transaction:
    def __init__(self, client, item, quantity):
        self.client = client
        self.item = item
        self.quantity = quantity
        self.cost = item.price * quantity
        self.time_stamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.item.name}, {self.quantity}, {self.cost} EUR, {self.time_stamp}"

class Store:
    def __init__(self):
        self.clients = []
        self.transactions = []
        self.items = []

    def addClient(self, client):
        self.clients.append(client)

    def addItem(self, item):
        self.items.append(item)

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

store = Store()
client1 = Client('123456', 'Tiit Toomingas')
client2 = Client('567483', 'Jaan Tamm')
client3 = Client('908765', 'Mari Maasikas')
store.addClient(client1)
store.addClient(client2)
store.addClient(client3)

print("This is the list of all our clients: \n")
for client in store.clients:
    print(client.id, client.name)

item1 = Item('Cat bed', 35.90, 3)
item2 = Item('Cat tree', 189.00, 2)
item3 = Item('Bowls set', 15.90, 13)
item4 = Item('Cat interactive toy', 19.90, 12)
item5 = Item('Cat shampoo', 4.50, 23)
store.addItem(item1)
store.addItem(item2)
store.addItem(item3)
store.addItem(item4)
store.addItem(item5)

print("\nThis is the list of all our products: \n")
for item in store.items:
    print(item.name, item.price, 'EUR ', item.stock)

print("\nList of the transactions: ")
client1.place_order([(item5, 3), (item4, 1)])
client2.place_order([(item1, 1)])
client3.place_order([(item1, 1), (item5, 5), (item4, 10)])
client3.place_order([(item2, 1)])

for client in store.clients:
    print(f"\nThese are all the purchases of {client.name}: ")
    client.view_transactions()
    print(f"Total cost: {client.total_cost_of_all_transactions()} EUR")

print("\nThis is the updated list of all our products: \n")
for item in store.items:
    print(item.name, item.price, 'EUR ', item.stock)