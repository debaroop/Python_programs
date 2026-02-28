flight_no="AI203"
base_fare="4500.75"
tax_percent="5"
seat_numbers="12A,12B,14C,15D"
is_international="True"

base_fare_num=float(base_fare)
tax_percent_num=float(tax_percent)

final_fare=base_fare_num+(base_fare_num*tax_percent_num/100)
print("Final fare for one passenger:", final_fare)

seat_list=seat_numbers.split(',')
print("Seat list:",seat_list)

seat_set=set(seat_list)
print("Seat set:",seat_set)

is_international_bool=True if is_international=="True" else False
print("Is international:", is_international_bool)

flight_summary={
    "flight_no":flight_no,
    "final_fare":int(final_fare),
    "seat_numbers":tuple(seat_list)
}

print("Flight Summary", flight_summary)

