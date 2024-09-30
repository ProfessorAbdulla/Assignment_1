from enum import Enum
from datetime import datetime
class Loyalty(Enum):
    gold=1
    silver=2
    platinum=3
    bronze=4
class RoomType(Enum):
    suite=1
    queen=2
    king =3
class Role(Enum):
    manager= 1
    front_desk= 2
#customer class to store customer details and manage loyalty points
class Customer:
    def __init__(self, customer_id,name, email,phone_number,loyalty_level=Loyalty.bronze,loyalty_points=0):
        self.__customer_id= customer_id
        self.__name= name
        self.__email=email
        self.__phone_number=phone_number
        self.__loyalty_level= loyalty_level
        self.__loyalty_points= loyalty_points

    # getters
    def get_customer_id(self):
        return self.__customer_id
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_phone_number(self):
        return self.__phone_number
    def get_loyalty_points(self):
        return self.__loyalty_points
    def get_loyalty_level(self):
        return self.__loyalty_level

    # setters
    def set_customer_id(self,customer_id):
        self.__customer_id= customer_id
    def set_name(self,name):
        self.__name= name
    def set_email(self, email):
        self.__email= email
    def set_phone_number(self, phone_number):
        self.__phone_number= phone_number
    def set_loyalty_level(self, loyalty_level):
        self.__loyalty_level= loyalty_level
    def set_loyalty_points(self, loyalty_points):
        self.__loyalty_points =loyalty_points

    def __str__(self):
        return (f"{self.get_customer_id()},{self.get_name()} ,{self.get_email()}, {self.get_phone_number()},{self.get_loyalty_level()}, {self.get_loyalty_points()}")  #returns a string showing the customer's details

    # method to add loyalty points
    def add_loyalty_points(self, points):
        if points< 0:
            print("Points cannot be negative.")
            return
        else:
            New_points= self.get_loyalty_points() +points  # adding the given points to the current points
            self.set_loyalty_points(New_points)  # set loyalty points based on new total points

    def update_loyalty_level(self):
        current_points = self.get_loyalty_points()
        if current_points >5000:
            self.set_loyalty_level(Loyalty.platinum)  # sets loyalty level to platinum if points are greater than 5000
        elif current_points >1000:
            self.set_loyalty_level(Loyalty.gold)
        elif current_points >500:
            self.set_loyalty_level(Loyalty.silver)
        else:
            self.set_loyalty_level(Loyalty.bronze)

    # method to redeem loyalty points
    def redeem_loyalty_points(self, points):
        if points <0:
            print("Points to redeem cannot be negative.")
            return
        current_points= self.get_loyalty_points()
        if current_points >= points:  #checks if the customer has enough points to redeem
            self.set_loyalty_points(current_points - points)  # deducts the redeemed points from the current points
        else:
            print("You do not have enough loyalty points")

    def display(self):
        print(f"Customer ID: {self.get_customer_id()}")
        print(f"Name: {self.get_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Phone Number: {self.get_phone_number()}")
        print(f"Loyalty Level: {self.get_loyalty_level().name}")
        print(f"Loyalty Points: {self.get_loyalty_points()}")

# room class to manage hotel rooms and their upgrades
class Room:
    def __init__(self, room_number, price_per_night, room_type=RoomType.suite, is_available=True, upgrade_cost=0):
        self.__room_number= room_number
        self.__price_per_night =price_per_night
        self.__room_type =room_type
        self.__is_available= is_available
        self.__upgrade_cost= upgrade_cost

    # getters
    def get_room_number(self):
        return self.__room_number
    def get_price_per_night(self):
        return self.__price_per_night
    def get_room_type(self):
        return self.__room_type
    def get_is_room_available(self):
        return self.__is_available
    def get_upgrade_cost(self):
        return self.__upgrade_cost

    # setters
    def set_room_number(self, room_number):
        self.__room_number =room_number
    def set_price_per_night(self, price):
        self.__price_per_night= price
    def set_room_type(self, room_type=RoomType.suite):
        self.__room_type =room_type
    def set_availability(self, is_available):
        self.__is_available= is_available
    def set_upgrade(self, upgrade_cost):
        self.__upgrade_cost= upgrade_cost

    def __str__(self):
        return ( f"{self.get_room_number()}, {self.get_room_type()},{self.get_price_per_night()},{self.get_is_room_available()},{self.get_upgrade_cost()}")

    # method to apply upgrade cost
    def apply_upgrade_cost(self, upgrade_cost):
        if not self.get_is_room_available():  # checks if the room is available for upgrade
            return f"Room {self.get_room_number()} is not available for an upgrade"  # returns a message if the room is not available
        self.set_upgrade(self.get_upgrade_cost() + upgrade_cost)  # adds the new upgrade cost to the current upgrade cost
        return f"Upgrade cost applied. New total upgrade cost is ${self.get_upgrade_cost()}."  # returns a message with the new total upgrade cost

    def display(self):
        print(f"Room Number: {self.get_room_number()}")
        print(f"Room Type: {self.get_room_type()}")
        print(f"Price per Night: ${self.get_price_per_night()}")
        print(f"Availability: {self.get_is_room_available()}")
        print(f"Upgrade Cost: ${self.get_upgrade_cost()}")


# reservation class to manage booking details
class Reservation:
    def __init__(self, reservation_id,customer_id,customer_name,room_number, room_type=RoomType.suite, price_per_night=0.0,check_in_date='2024-01-01', check_out_date='2024-01-02', total_cost=0.0):
        self.__reservation_id= reservation_id
        self.__customer_id =customer_id
        self.__customer_name= customer_name
        self.__room_number =room_number
        self.__room_type =room_type
        self.__price_per_night= price_per_night
        self.__check_in_date =datetime.strptime(check_in_date, '%Y-%m-%d')
        self.__check_out_date= datetime.strptime(check_out_date, '%Y-%m-%d')
        self.__total_cost= total_cost

    # getters
    def get_reservation_id(self):
        return self.__reservation_id
    def get_customer_id(self):
        return self.__customer_id
    def get_customer_name(self):
        return self.__customer_name
    def get_room_number(self):
        return self.__room_number
    def get_room_type(self):
        return self.__room_type
    def get_price_per_night(self):
        return self.__price_per_night
    def get_check_in_date(self):
        return self.__check_in_date
    def get_check_out_date(self):
        return self.__check_out_date
    def get_total_cost(self):
        return self.__total_cost

    # setters
    def set_reservation_id(self,reservation_id):
        self.__reservation_id= reservation_id
    def set_customer_id(self,customer_id):
        self.__customer_id= customer_id
    def set_customer_name(self, customer_name):
        self.__customer_name= customer_name
    def set_room_number(self, room_number):
        self.__room_number= room_number
    def set_room_type(self,room_type):
        self.__room_type= room_type
    def set_price_per_night(self, price_per_night):
        self.__price_per_night= price_per_night
    def set_check_in_date(self, check_in_date):
        self.__check_in_date= datetime.strptime(check_in_date, '%Y-%m-%d')
    def set_check_out_date(self, check_out_date):
        self.__check_out_date= datetime.strptime(check_out_date, '%Y-%m-%d')
    def set_total_cost(self, total_cost):
        self.__total_cost= total_cost

    def __str__(self):
        return (
            f"{self.get_reservation_id()},{self.get_customer_id()},{self.get_customer_name()},{self.get_room_number()},{self.get_room_type()},{self.get_check_in_date()},{self.get_check_out_date()},{self.get_total_cost()}")

    def display(self):
        print(f"Reservation ID: {self.get_reservation_id()}")
        print(f"Customer ID: {self.get_customer_id()}")
        print(f"Customer Name: {self.get_customer_name()}")
        print(f"Room Number: {self.get_room_number()}")
        print(f"Room Type: {self.get_room_type()}")
        print(f"Price per night: {self.get_price_per_night()}")
        print(f"Check-in Date: {self.get_check_in_date()}")
        print(f"Check-out Date: {self.get_check_out_date()}")
        print(f"Total Cost: ${self.get_total_cost()}")


# discount class to manage discounts applied to reservations
class Discount:
    def __init__(self, discount_name,discount_percentage,start_date, end_date, min_amount_required):
        self.__discount_name= discount_name
        self.__discount_percentage= discount_percentage
        self.__start_date= datetime.strptime(start_date, '%Y-%m-%d')
        self.__end_date =datetime.strptime(end_date, '%Y-%m-%d')
        self.__min_amount_required= min_amount_required

    # getters
    def get_discount_name(self):
        return self.__discount_name
    def get_discount_percentage(self):
        return self.__discount_percentage
    def get_start_date(self):
        return self.__start_date
    def get_end_date(self):
        return self.__end_date
    def get_min_amount_required(self):
        return self.__min_amount_required

    # setters
    def set_discount_name(self, discount_name):
        self.__discount_name= discount_name
    def set_discount_percentage(self, discount_percentage):
        self.__discount_percentage= discount_percentage
    def set_start_date(self,start_date):
        self.__start_date= datetime.strptime(start_date, '%Y-%m-%d')
    def set_end_date(self, end_date):
        self.__end_date= datetime.strptime(end_date, '%Y-%m-%d')
    def set_min_amount_required(self, min_amount_required):
        self.__min_amount_required =min_amount_required

    # apply discount to a reservation
    def apply_discount_to_reservation(self, reservation):
        current_date = datetime.now()
        # Check if the discount is valid within the date range
        if self.__start_date <= current_date <= self.__end_date: #check if the current date is within the discount's valid period
            if reservation.get_total_cost() >= self.get_min_amount_required(): #check if the reservation total meets the minimum required for the discount
                discount_amount= reservation.get_total_cost()* (self.get_discount_percentage()/ 100) #calculate the discount amount based on the percentage
                new_total= reservation.get_total_cost() - discount_amount #subtract the discount from the total reservation cost
                reservation.set_total_cost(new_total) #update the reservation with the new total cost after the discount
                return f"Discount of {self.get_discount_percentage()}% applied. New total cost is ${new_total}"  #return a message showing the applied discount and new total
            else:
                return f"Reservation total does not meet the minimum amount required for the discount." #return a message if the total doesn't meet the required minimum
        else:
            return "The discount is not valid during the reservation period." #return a message if the current date is outside the discount's valid period

#hotelStaff class to manage staff roles and actions
class HotelStaff:
    def __init__(self,staff_id,name, role=Role.front_desk):
        self.__staff_id= staff_id
        self.__name= name
        self.__role= role

    #getters
    def get_staff_id(self):
        return self.__staff_id
    def get_name(self):
        return self.__name
    def get_role(self):
        return self.__role

    #setters
    def set_staff_id(self,staff_id):
        self.__staff_id= staff_id
    def set_name(self,name):
        self.__name =name
    def set_role(self, role=Role.front_desk):
        self.__role= role
    def __str__(self):
        return (f"{self.get_staff_id()},{self.get_name()} ,{self.get_email()}, {self.get_role()}")

    #confirms the reservation and returns a confirmation message
    def confirm_reservation(self, reservation):
        return f"Reservation {reservation.get_reservation_id()} confirmed by {self.__name}"  #returns a message confirming the reservation with the staff member's name

    #processes room upgrade by applying the extra cost
    def process_upgrade_cost(self,room,upgrade_cost):
        room.apply_upgrade_cost(upgrade_cost)  # calls the room method to apply the upgrade cost
        return f"Room {room.get_room_number()} upgraded with extra cost {upgrade_cost}"  #returns a message confirming the upgrade with the room number and the extra cost

    def display(self):
        print(f"Staff ID: {self.get_staff_id()}")
        print(f"Name: {self.get_name()}")
        print(f"Role: {self.get_role().name}")


#test Customer class
customer1= Customer(1,"Abdulla","Shi5_ad@hotmial.com","025841899")
customer1.display()
print("") #to make the output clearer

#add loyalty points and test loyalty level update
customer1.add_loyalty_points(600)  #Should upgrade to Silver
customer1.display()
print("")

customer1.redeem_loyalty_points(200)  #deduct points
customer1.display()
print("")

#test Room class
room1= Room(101,200.5,RoomType.queen)
room1.display()
print("")

#apply upgrade cost
print(room1.apply_upgrade_cost(50))  #apply an upgrade cost of $50
room1.display()
print("")


#set room as unavailable
room1.set_availability(False)
print(room1.apply_upgrade_cost(30))  #it will not allow upgrade due to room unavailability
print("")

#test Reservation class
reservation1= Reservation(1,customer1.get_customer_id(),customer1.get_name(), room1.get_room_number(), room1.get_room_type(),room1.get_price_per_night(), "2024-09-26", "2024-09-27", 750.0)
reservation1.display()
print("")

#test Discount class
discount1 =Discount("Holiday Special",10,"2024-09-26","2024-09-27",500.0)
print(discount1.apply_discount_to_reservation(reservation1))  #apply a 10% discount
reservation1.display()

print("")

#test HotelStaff class
staff1 = HotelStaff(1,"Safe Saleh",Role.manager)
print(staff1.confirm_reservation(reservation1))  #confirm the reservation
print("")

#test room upgrade by staff
print(staff1.process_upgrade_cost(room1,100))  #apply an additional upgrade cost
room1.display()

#display staff info
staff1.display()