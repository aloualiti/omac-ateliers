from hotel import Hotel 
#import notification
from reservation import Reservation
#import tester
from customer import Customer

def start_app():
    #اضافة الفنادق
    rotana_hotel = Hotel(20,"Rotana","Abu Dhabi",200, 40)
    sheraton_hotel = Hotel(21,"Sheraton","Abu Dhabi", 300, 100)
    mercur_hotel = Hotel(19, "Mercure","Nador", 100, 50)
    royalhotel=Hotel(1, 'The Royal Hotel', 'Toronto', 200, 30)
    ryadnador=Hotel(2, 'Hotel RYAD', 'Nador', 200, 1)
    mercure=Hotel(3, 'Mercure', 'Nador', 200, 10)
    print "*" * 20
    print Hotel.hotels
    print "*" * 20

    print "List hotels in Nador city"
    print mercure.list_hotels_in_city('Nador')
    #اضافة الزبناء
    mounir = Customer('Mounir AL OUALITI')
    asmae = Customer('Asmae SAKSAK')
    print "*" * 20
    #اضافة الحجوزات
    reservation2 =Reservation("Hotel RYAD", "Mohamed SAKSAK")
    reservation1 =Reservation("Hotel RYAD", "Mounir AL OUALITI")
    reservation2 =Reservation("Hotel RYAD", "Asmae SAKSAK")
    reservation3 =Reservation("Mercure", "Asmae SAKSAK")
    reservation4 =Reservation("Mercure", "Mounir AL OUALITI")
    print "*" * 20
    print "List reservations for hotel Mercure"
    print reservation1.list_reservations_for_hotel('Mercure')
    print "*" * 20
    print "List Hotels"
    print Hotel.hotels
    print "*" * 20

start_app()

