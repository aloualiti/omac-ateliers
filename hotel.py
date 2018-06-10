class Hotel():
    hotels=[]
    def __init__(self, number, hotel_name, city, total_rooms, empty_rooms):
        if not isinstance(number, int):
            raise ValueError("first argument most to be numeric")
        elif not isinstance(hotel_name, str) :
            raise ValueError("second argument 'hotel_name' is incorrect")
        elif not isinstance(city, str):
            raise ValueError("'city' argument is incorrect")
        elif not isinstance(total_rooms, int):
            raise ValueError("'total_rooms' argument must to be numeric")
        elif not isinstance(empty_rooms, int):
            raise ValueError("'empty_rooms' argument must to be numeric")
        hotel_in_list=False
        for hotel in Hotel.hotels:
            if hotel[1] == hotel_name and hotel[2] == city:
                hotel_in_list = True
        if hotel_in_list==False:
            self.number = number       
            self.hotel_name = hotel_name
            self.city = city
            self.total_rooms = total_rooms
            self.empty_rooms = empty_rooms
            Hotel.hotels.append([number, hotel_name,city,total_rooms,empty_rooms])
        else:
            print "this hotel already exists in this city"

    def list_hotels_in_city(self, city):
        return [hotel for hotel in Hotel.hotels if hotel[2]==city]
    