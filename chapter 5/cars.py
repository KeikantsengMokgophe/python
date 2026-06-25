# The code loops through a list of car brands, printing "BMW" in uppercase and all others in title case.
# Inside the else block, it demonstrates case-sensitive string comparison by showing that "Audi" == "audi" returns False.
# It then shows how using .lower() allows for case-insensitive comparison, returning True.



cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

        # IGNORING CASE WHEN CHECKING FOR EQUALITY

        car = "Audi"
        print(car == "audi")

        print(car.lower() == "audi")
