from pizzapy import Customer, StoreLocator, Menu, Order, CreditCard
import requests

customer = Customer("Saul", "Tobias", "email@email.com", "7138150697", "4823 Bayou Ln, Rosharon, TX, 77583")

service = 'Carryout'

print(customer)
try:
    myLocalDominos = StoreLocator.find_closest_store_to_customer(customer, service)
except Exception:
    print("No stores open at this moment")
    print("Exiting Program.....")
    exit()

print(myLocalDominos)
details = myLocalDominos.get_details()
print(details['ServiceHoursDescription'])

#menu = myLocalDominos.get_menu()

#print(menu)

#menu.search(Name="Coke")

#order = Order.begin_customer_order(customer, myLocalDominos)
#order.add_item('P12IPAZA')

#print(order)
