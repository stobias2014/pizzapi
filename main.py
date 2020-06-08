from pizzapy import Customer, StoreLocator, Menu, Order, CreditCard

customer = Customer("Saul", "Tobias", "email@email.com", "7138150697", "4823 Bayou Ln, Rosharon, TX, 77583")

print(customer)
try:
    myLocalDominos = StoreLocator.find_closest_store_to_customer(customer)
except Exception:
    print("No stores open at this moment")
    print("Exiting Program.....")
    exit()

print(myLocalDominos)

menu = myLocalDominos.get_menu()

print(menu)

menu.search("Pizza")

order = Order.begin_customer_order(customerm, myLocalDominos)
order.add_item('P12IPAZA')

print(order)
