# 2.2.1
# Volume of a sphere with radius 5
r = 5 #radius of the sphere
volume = 4/3*3.14159*r**3
print("2.2.1 Volume of sphere:", volume)

# 2.2.2
# Textbook price
cover_price = 24.95
discount = 0.4
shipping_book_one = 3
shipping_extra_book = 0.75
num_books = 60
total_shipping = shipping_book_one + shipping_extra_book*(num_books-1)
total_wholesale = num_books*(cover_price*(1-discount)) + total_shipping
print("2.2.2: Textbook price:", total_wholesale)

# 2.2.3
# Breakfast time
easy_pace = 8 + 15/60
tempo = 7 + 12/60
easy_miles = 1
tempo_miles = 3
easy_miles += 1
start_hour = 6
start_minute = 52
run_time = easy_pace*easy_miles + tempo*tempo_miles
run_hours = run_time//60 # floor division, default with integers in python2
run_minutes = run_time - run_hours*60
breakfast_minute = start_minute + run_minutes
breakfast_hour = start_hour + run_hours + breakfast_minute//60
breakfast_minute = breakfast_minute - 60*(breakfast_minute//60)
print("2.2.3 Breakfast time:", breakfast_hour,":",breakfast_minute)
