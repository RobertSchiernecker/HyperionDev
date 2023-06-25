# Dictionary of city-flight options with corresponding prices
city_flight_options = {'Barcelona': 500, 'Madrid': 400, 'Ibiza': 300, 'Marbella': 450}

# Function to calculate hotel cost based on number of nights
def hotel_cost(num_nights):
    return num_nights * 100

# Function to calculate plane cost based on selected city
def plane_cost(city):
    return city_flight_options[city]

# Function to calculate car rental cost based on number of rental days
def car_rental(rental_days):
    return rental_days * 50

# Function to calculate total holiday cost
def holiday_cost(city, num_nights, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city) + car_rental(rental_days)
    return total_cost

# Get user input for city and flight
city = input("Enter city name (Barcelona, Madrid, Ibiza, Marbella): ")
while city not in city_flight_options:
    city = input("Invalid city name. Please choose from (Barcelona, Madrid, Ibiza, Marbella): ")

num_nights = int(input("Enter number of nights stay: "))
rental_days = int(input("Enter number of car rental days: "))

# Calculate total holiday cost using the holiday_cost function
total_cost = holiday_cost(city, num_nights, rental_days)

# Display all details in a readable way
print("City: ", city)
print("Flight cost: £", plane_cost(city))
print("Number of nights: ", num_nights)
print("Hotel cost: £", hotel_cost(num_nights))
print("Number of car rental days: ", rental_days)
print("Car rental cost: £", car_rental(rental_days))
print("Total holiday cost: £", total_cost)
