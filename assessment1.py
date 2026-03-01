class FlightNotFoundError(Exception):
    pass

class Flight:
    def __init__(self, flight_no,source, destination, total_seats):
        self.flight_no=flight_no
        self.source=source
        self.destination=destination
        self.total_seats=total_seats
        
    
    def add_flight(self,flight_no,source, destination, total_seats):
        
        try:
            
            if not isinstance(flight_no,str):
                raise FlightNotFoundError("Invalid Flight Number.Must be a String")
            
            seats=int(total_seats)
            
            if seats<=0:
                raise ValueError("Seats must be greater than 0")
            
            
                
            self.flight_no=flight_no
            self.source=source
            self.destination=destination
            self.total_seats=total_seats
            
            print("Flight added sucessfully")
            
            
        except ValueError as ve:
            print("Value Error:", ve)
            
        except Exception as e:
            print("Exception:", e)
    
    
    
    
f1 = Flight("", "", "", 0)

# Valid input
f1.add_flight("AI101", "Delhi", "Mumbai", "90")

# Invalid seat cases
f1.add_flight("AI102", "Delhi", "Goa", "-90")      # seats <= 0
f1.add_flight("AI103", "Delhi", "Chennai", "90abc") # invalid integer

# Invalid flight number (numeric)
f1.add_flight(0.0, "Delhi", "Goa", "50")
