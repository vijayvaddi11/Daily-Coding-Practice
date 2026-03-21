# class ParkingSlot:
#     def __init__(self,bike_slots,car_slots):
#         self.bike_slots = bike_slots
#         self.car_slots=car_slots
    
#     def park(self, vechile_type):
#         if vechile_type == "bike":
#             if self.bike_slots >0:
#                 self.bike_slots -= 1
#                 return "bike parked sucessfully!"
#             return "parking slots for bikes are full"
#         elif vechile_type =="car":
#             if self.car_slots>0:
#                 self.car_slots -= 1
#                 return f"car parked sucessfully!{self.car_slots}"
#             return "parking slots for cars are full"
#         else:
#             return "only park cars and bike has slots here to park!"
#     def leave(self,vechile_type):
#         if vechile_type == "bike":
#             self.bike_slots += 1
#             return f"available bike slots {self.bike_slots}"
#         else:
#             self.car_slots += 1
#             return f"available bike slots {self.car_slots}"

# parking = ParkingSlot(20,1)
# print(parking.park("car"))
# print(parking.leave("car"))





# class Library:
#     def __init__(self,books_count):
#         self.books_count = books_count
    
#     def borrow_books(self,no_of_books_borrow):
#         if no_of_books_borrow <= self.books_count:
#             self.books_count -= no_of_books_borrow
#             return "books borrowed sucefully!"
#         else:
#             return "sorry books not available (X)"
    
#     def return_books(self, no_of_books_return):
#         if no_of_books_return >0:
#             self.books_count += no_of_books_return
#             return "thanks of returning books!"
#         else:
#             return "returning books count must >0 (X)"
        
    
#     def get_books(self):
#         return self.books_count

# lib = Library(20)

# print(lib.borrow_books(5))
# print(lib.get_books())

# print(lib.borrow_books(30))
# print(lib.return_books(10))

# print(lib.get_books())


#inti,withdrawl,deposit,available_balance
#user_amount,withdrawl_amount,deposit_amount



# class ATM:
#     def __init__(self,user_amount):
#         self.user_amount = user_amount
    
#     def withdrawl(self,withdrawl_amount):
#         if withdrawl_amount <= self.user_amount:
#             self.user_amount -= withdrawl_amount
#             return f"{withdrawl_amount} withdraw successfully!"
#         else:
#             return "in sufficiant balance (X)"
    
    
#     def deposite(self,deposit_amount):
#         if deposit_amount >= 100:
#             self.user_amount += deposit_amount
#             return f"{deposit_amount} amount deposited successfully!"
#         else:
#             return "min amount for deposite is 100"
    
#     def available_balance(self):
#         return self.user_amount

# a = ATM(500)
# print(a.withdrawl(5001))
# print(a.available_balance())



# print(a.deposite(100))
# print(a.available_balance())





# class Cart:
#     def __init__(self):
#         self.items ={}
    
#     def add_item(self,item,cost):
#         self.items[item]=cost
        
#     def total(self):
#         return sum(self.items.values())
        
# cart = Cart()

# cart.add_item("coke", 20)
# cart.add_item("biriyani", 250)

# print(cart.total())





class URL:
    def __init__(self):
        self.map ={}
    
    def shorten(self,shorter,longer):
        self.map[shorter]=longer
    
    def get(self,shorter):
        return self.map.get(shorter)

u=URL()
u.shorten('yt','www.youtube.com')
print(u.get('yt'))

