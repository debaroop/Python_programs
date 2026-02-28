class Flight:
    def __init__(self, flight_no, source, dest, base_fare):
        self.flight_no=flight_no
        self.source=source
        self.dest=dest
        self.base_fare=base_fare
        
    def get_flight_info(self):
        return(
            f"Flight No: {self.flight_no}\n"
            f"Source: {self.source}\n"
            f"Destination:{self.dest}"
            )
        
    def calculate_fare(self, passenger_count, discount=0):
        total_fare=self.base_fare*passenger_count
        
        if discount>0:
            total_fare-=discount
        return total_fare
    
    def update_route(self,dest,source=None):
        self.dest=dest
        if source is not None:
            self.source=source
            self.dest=dest
            
flight1=Flight("AT101","Bengaluru","Chennai", 6000)

print("Flight Info:")
print(flight1.get_flight_info())

fare1=flight1.calculate_fare(3)
print("\nTotal Fare(3 passengers):", fare1)
        
fare2=flight1.calculate_fare(2,500)
print("\nTotal Fare(2 passengers with 500 discount):",fare2) 

flight1.update_route("Pune")
print("\nAfter updating Destination")
print(flight1.get_flight_info()) 

flight1.update_route("Goa","Pune")
print("\nAfter updating Source and Destination:") 
print(flight1.get_flight_info())      