hotels_list=[]
customers_list=[]
reservation_list=[]

def add_hotel(number, hotel_name, city, total_rooms, empty_rooms):
    hotel={'number':number, 'hotel_name':hotel_name, 'city':city, 'total_rooms':total_rooms, 'empty_rooms':empty_rooms}
    for elem in hotels_list:
        if elem.get("hotel_name")==hotel_name:
            return "this hotel already exists in the list"
    hotels_list.append(hotel)
    return hotel_name + " added to the list"
        
def add_customer(customer_name):
    for elem in customers_list:
        if elem == customer_name:
            return "this customer already exists in the list"         
    customers_list.append(customer_name)
    return customer_name + " added to the list"
   

def reserve_room(hotel_name, customer_name):
    for hotel in hotels_list:
        if hotel['hotel_name']==hotel_name:
            if hotel['empty_rooms']>0:
                add_new_reservation(hotel_name, customer_name)
                hotel['empty_rooms']-=1
                print "confirmation"
                return True
    print "sorry no rooms available"
    return False
          
def add_new_reservation(hotel_name,customer_name):
    reservation_list.append({'hotel_name':hotel_name,'customer_name':customer_name})

def list_hotels_in_city(city_name):
    liste=[]
    for hotel in hotels_list:
        if hotel['city']==city_name:
            liste.append([hotel['hotel_name'],hotel['empty_rooms']])
    print liste
        
def list_reservations_for_hotel(hotel_name):
    customers=[]
    for elem in reservation_list:
        if elem['hotel_name']==hotel_name:
            customers.append(elem['customer_name'])
    print customers

print add_hotel(1, 'The Royal Hotel', 'Toronto', 200, 30)
print add_hotel(2, 'Hotel RYAD', 'Nador', 200, 1)
print add_hotel(3, 'Mercure', 'Nador', 200, 10)
print add_customer('Mounir AL OUALITI')
print add_customer('Asmae SAKSAK')

reserve_room("Hotel RYAD", "Mounir AL OUALITI")
reserve_room("Hotel RYAD", "Asmae SAKSAK")
reserve_room("Mercure", "Asmae SAKSAK")
reserve_room("Mercure", "Mounir AL OUALITI")

list_reservations_for_hotel('Mercure')
list_hotels_in_city('Nador')
print add_hotel(3, 'Mercure', 'Nador', 200, 10)
print add_customer('Mounir AL OUALITI')
