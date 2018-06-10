from hotel import Hotel
from customer import Customer
class Reservation():
    reservations=[]
    def __init__(self, hotel_name, customer_name):
        hotel = [hotel for hotel in Hotel.hotels if hotel_name == hotel[1]]
        if hotel == []:
            raise ValueError("this hotel not exist in the list")
        customer1 = False
        for elem in Customer.customers:
            if elem==customer_name:
                customer1 = True
        if customer1 == False:
            print ("this customer not exist in the list")
        else:
            if hotel[0][4]==0:
                print "sorry no rooms available"
            else:
                self.hotel_name = hotel_name
                self.customer_name = customer_name
                Reservation.reservations.append([hotel_name, customer_name])
                hotel[0][4] -= 1
                print "confirmation"
        
    def list_reservations_for_hotel(self, hotel_name):
        return [reservation for reservation in Reservation.reservations if reservation[0]==hotel_name]

