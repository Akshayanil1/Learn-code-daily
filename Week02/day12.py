# ---- Introduction to dictionaries in python ----
# A dictionary is a collection of key-value pairs.
# Each key is unique and maps to a value.
# Dictionaries are mutable, meaning you can change them after creation.
person = {
    "name": "John",
    "age": 30,
    "city": "Chennai",
    "is_programmer": True
}

person["email"] = "johnbro@gmail.com"
person["city"] = "Karichampatti"
# print(f"The person's name is {person['name']}")
# print(f"The person's age is {person['age']}")
# print(f"The person's email is {person['email']}")
# print(f"The person's city is {person['city']}")
# print(f"Is the person a programmer? {person['is_programmer']}")
for key, value in person.items():
    print(f"The key is {key} and the value is {value}")

#--- new dictionary containing dtails about a car ---

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": "2021"
}
car['color'] = "Blue"
# print(f"The car's brand is {car['brand']}")
# print(f"The car's model is {car['model']}")
# print(f"The car's year is {car['year']}")
# print(f"The car's color is {car['color']}")

print("\nCar Details:")
for key, value in car.items():
    print(f"Property: {key} ---- Value: {value}")