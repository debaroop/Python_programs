class Flight:
    def __init__(self,flight_no,base_price,total_seats):
        self.flight_no=flight_no
        self.base_price=base_price
        self.total_seats=total_seats
    
    def display_flight_info(self):
        print("Flight no", self.flight_no)
        print("Base price:", self.base_price)
        print("Total no of seats:",self.total_seats)
        
class DomesticFlight(Flight):
    def __init__(self, flight_no, base_price, total_seats, tax_percent):
        super().__init__(flight_no, base_price, total_seats)
        self.tax_percent = tax_percent
        
    def calculate_price(self):
        return self.base_price + self.tax_percent
    
class BookingFlight(DomesticFlight):
    def __init__(self, flight_no, base_price, total_seats, tax_percent, booked_seats):
        super().__init__(flight_no, base_price, total_seats,tax_percent)
        self.booked_seats = booked_seats
        
    def check_seat_availability(self, seats_requested):
        return seats_requested <= (self.total_seats - self.booked_seats)

    def book_seats(self, seats_requested):
        if self.check_seat_availability(seats_requested):
            self.booked_seats += seats_requested
            print("Seats booked successfully!")
            print("Remaining seats:", self.total_seats - self.booked_seats)
        else:
            print("Not enough seats available.")


    def get_final_price(self, seats_requested):
        price_after_tax = self.calculate_price()
        return price_after_tax * seats_requested
    
    def get_final_price(self, seats_requested):
        price_after_tax=super().calculate_price()
        final_price=price_after_tax*seats_requested
        return final_price
        
        

flight1 = BookingFlight("AI101", 5000, 100, 10, 25)

# Display flight info
flight1.display_flight_info()

# Take user input
seats = int(input("Enter number of seats to book: "))

# Check availability and book
if flight1.check_seat_availability(seats):
    total_price = flight1.get_final_price(seats)
    flight1.book_seats(seats)
    print("Total price to pay:", total_price)
else:
    print("Seats not available.")
