# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print('-' * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

# Print some states
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

# Do it by using the state then cities dict
print('-' * 10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# Print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for key, value in list(states.items()):
    print(f"{key} is the key for the value {value}")

# Do both at the same time
print('-' * 10)
print("Abbr. \t State \t\t City")
for state, abbrev in list(states.items()):
    print(f"{abbrev} \t {state} \t {cities[abbrev]}")

# Safely get an abbreviation by state that might not be there
print('-' * 10)
state_abbrev = states.get('Texas')

if state_abbrev:
    print(f"Texas has abbreviation: {state_abbrev}")
else:
    print("Sorry, no Texas.")

# Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
