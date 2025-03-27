
#create four function definitions, which will include specific calculations 
#it is easier to leave the first three functions in a format of integers, so could be used to calculate the total within the fourth function

def hotel_cost(num_nights):
     total_hotel_cost = num_nights * cost_per_night 
     return(total_hotel_cost)

def plane_cost(city_flight):
     total_journey = city_flight
     return(total_journey)

def car_rental(rental_days):
     car_hire = rental_days * daily_car_rate
     return(car_hire)

def holiday_cost(num_nights, city_flight, rental_days):
     total_hotel_cost = hotel_cost(num_nights)
     print("The hotel stay comes up to: ", total_hotel_cost)
     car_hire = car_rental(rental_days)
     print("The car hire comes up to: ", car_hire)
     total_journey = plane_cost(city_flight)
     print("The plane journey comes up to: ", total_journey, "\n")
     total_price = total_hotel_cost + total_journey + car_hire
     return ("The travel pacakge for your chosen destination, comes to: " + str(total_price))

#ask the user for input, the city destination

print("Current hot holiday deals: Paris, Florence, New York, Madrid\n")

city_flight = input("Please select which city, form the list above, you would like to fly to: ")

print("\n")

#ask the user to enter the duration of the hotel stay 

num_nights = int(input("Please eneter the number of nights you will be spending at a hotel: "))

print("\n")

#ask the user to enter the car hire period 

rental_days = int(input("Please enter the number of days you will be needing to rent the car for: "))

print("\n")

#create a loop, providing options based on the user's city choice
#for each city choice, create a set of specific data(e.g hotel & car price rates)
#through the earlier stated function definitions print the prices of each travel aspect(for the specific city), including the total cost of the holiday 

if city_flight == "Paris":
     cost_per_night = int(160)
     daily_car_rate = int(18)
     city_flight = int(178)
     print(holiday_cost(num_nights, city_flight, rental_days))

elif city_flight == "Florence":
     cost_per_night = int(150)
     daily_car_rate = int(14)
     city_flight = int(216)
     print(holiday_cost(num_nights, city_flight, rental_days))

elif city_flight == "New York":
     cost_per_night = int(210)
     daily_car_rate = int(28)
     city_flight = int(441)
     print(holiday_cost(num_nights, city_flight, rental_days))

elif city_flight == "Madrid":
     cost_per_night = int(150)
     daily_car_rate = int(8)
     city_flight = int(115)
     print(holiday_cost(num_nights, city_flight, rental_days))

#create a message error option 

else: 
     print("Unfortunately the city you have selected is not covered by our travel package")