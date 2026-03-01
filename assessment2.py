class FlightNotFoundError(Exception):
    pass

class Flight:
    def __init__(self, flight_no,source, destination, total_seats):
        self.flight_no=flight_no
        self.source=source
        self.destination=destination
        self.total_seats=total_seats
        
    
    def book_seat(self):
        try:
            flight_no=input("Enter flight no:")
            
            if flight_no !=self.flight_no:
                raise FlightNotFoundError("Flight not found")
            
        except FlightNotFoundError as fe:
            print("FlightnotfoundError:",fe)
            return
        
        except Exception as e:
            print("Excepetion:",e)
            return
            
        try:
            seats_to_book=int(input("Enter the number of seats to book:"))
                                   
            if seats_to_book<=0:
                raise ValueError("Seats must be greater than 0")
            
            if seats_to_book>self.total_seats:
                raise RuntimeError("Not enough seats available")
            
            self.total_seats-=seats_to_book
            print("Seats booked successfully")
                
                
            
        except ValueError as ve:
            print("Value Error:", ve)
            
        except RuntimeError as re:
            print("RuntimeError:",re)    
            
        except Exception as e:
            print("Exception:", e)
    
    
f1 = Flight("AI101", "Delhi", "Mumbai", 50)
f1.book_seat()
    
